const $ = (id) => document.getElementById(id);
const labels = {pending: "Pendente", in_progress: "Em andamento", done: "Concluído"};
let selectedId = null;
let projects = [];
let editingProject = null;
let editingTask = null;
let refreshVersion = 0;

function node(tag, text, className) {
  const element = document.createElement(tag);
  if (text !== undefined) element.textContent = text;
  if (className) element.className = className;
  return element;
}

async function api(path, method = "GET", data) {
  const response = await fetch(`/api${path}`, {
    method,
    headers: data === undefined ? {} : {"Content-Type": "application/json"},
    body: data === undefined ? undefined : JSON.stringify(data),
  });
  if (!response.ok) {
    const body = await response.json();
    const detail = body.detail;
    throw new Error(Array.isArray(detail)
      ? "Verifique os campos: título e cliente não podem estar vazios; respeite os limites de tamanho."
      : detail || "Não foi possível concluir a operação.");
  }
  return response.status === 204 ? null : response.json();
}

function errorMessage(error) {
  $("message").textContent = error.message || "Falha de comunicação com o servidor.";
  $("message").hidden = false;
}

async function refresh() {
  const version = ++refreshVersion;
  const loaded = await api("/projects");
  if (version !== refreshVersion) return false;
  projects = loaded;
  if (!projects.some(p => p.id === selectedId)) selectedId = projects[0]?.id ?? null;
  $("count-all").textContent = projects.length;
  $("count-active").textContent = projects.filter(p => p.status === "in_progress").length;
  $("count-done").textContent = projects.filter(p => p.status === "done").length;
  $("projects").replaceChildren();
  for (const project of projects) {
    const card = node("button", undefined, `project-card${project.id === selectedId ? " selected" : ""}`);
    card.setAttribute("aria-pressed", String(project.id === selectedId));
    card.setAttribute("aria-controls", "project-detail");
    card.append(node("span", labels[project.status], `badge ${project.status}`));
    card.append(node("strong", project.title), node("span", project.customer, "client"));
    const progress = node("div", undefined, "card-progress");
    progress.append(node("span", `${project.completed_tasks}/${project.total_tasks} tarefas`), node("span", `${project.progress}%`));
    card.append(progress, node("span", "Abrir tarefas →", "open-tasks"));
    card.onclick = async () => {
      selectedId = project.id;
      $("status-filter").value = "";
      try {
        const updated = await refresh();
        if (updated && selectedId === project.id) {
          $("project-title").focus({preventScroll: true});
          $("project-title").scrollIntoView({block: "start"});
        }
      } catch (error) { errorMessage(error); }
    };
    $("projects").append(card);
  }
  if (!projects.length) $("projects").append(node("p", "Nenhum projeto cadastrado.", "empty-list"));
  const project = projects.find(p => p.id === selectedId);
  $("no-project").hidden = !!project;
  $("project-detail").hidden = !project;
  if (!project) return false;
  $("project-title").textContent = project.title;
  $("project-customer").textContent = `${project.customer}${project.order_reference ? ` · Pedido ${project.order_reference}` : ""}`;
  $("project-description").textContent = project.description;
  $("project-status").textContent = labels[project.status];
  $("project-status").className = `badge ${project.status}`;
  $("progress").value = project.progress;
  $("progress").setAttribute("aria-label", `Progresso: ${project.progress}%`);
  $("progress-text").textContent = `${project.completed_tasks} de ${project.total_tasks} tarefas · ${project.progress}%`;
  const status = $("status-filter").value;
  const tasks = await api(`/projects/${project.id}/tasks${status ? `?status=${status}` : ""}`);
  if (version !== refreshVersion) return false;
  $("tasks").replaceChildren();
  if (!tasks.length) $("tasks").append(node("p", status ? "Nenhuma tarefa neste status." : "Adicione a primeira etapa desta montagem.", "empty-list"));
  for (const task of tasks) renderTask(task);
  return true;
}

async function mutation(button, operation) {
  button.disabled = true;
  $("message").hidden = true;
  try { await operation(); await refresh(); }
  catch (error) { errorMessage(error); }
  finally { button.disabled = false; }
}

function renderTask(task) {
  const row = node("div", undefined, `task ${task.status}`);
  const copy = node("div", undefined, "task-copy");
  copy.append(node("div", task.title, "task-title"));
  if (task.description) copy.append(node("p", task.description, "description"));
  const controls = node("div", undefined, "task-controls");
  const select = node("select");
  select.setAttribute("aria-label", `Status de ${task.title}`);
  for (const [value, label] of Object.entries(labels)) {
    const option = node("option", label); option.value = value; select.append(option);
  }
  select.value = task.status;
  select.onchange = () => mutation(select, async () => {
    try { await api(`/tasks/${task.id}`, "PATCH", {status: select.value}); }
    catch (error) { select.value = task.status; throw error; }
  });
  const edit = node("button", "Editar", "subtle");
  edit.onclick = () => openTask(task);
  const remove = node("button", "Excluir", "subtle danger");
  remove.onclick = () => {
    if (confirm(`Excluir a tarefa "${task.title}"?`)) mutation(remove, () => api(`/tasks/${task.id}`, "DELETE"));
  };
  controls.append(select, edit, remove); row.append(copy, controls); $("tasks").append(row);
}

function prepareForm(form, data) {
  form.reset(); form.querySelector(".form-error").textContent = "";
  if (data) for (const field of ["title", "customer", "order_reference", "description"]) {
    if (form.elements.namedItem(field)) form.elements.namedItem(field).value = data[field];
  }
}

function openProject(project = null) {
  editingProject = project?.id ?? null;
  $("project-form-title").textContent = project ? "Editar projeto" : "Novo projeto";
  prepareForm($("project-form"), project); $("project-dialog").showModal();
}

function openTask(task = null) {
  editingTask = task?.id ?? null;
  $("task-form-title").textContent = task ? "Editar tarefa" : "Nova tarefa";
  prepareForm($("task-form"), task); $("task-dialog").showModal();
}

async function submitForm(event, kind) {
  event.preventDefault();
  const form = event.target;
  const button = form.querySelector('[type="submit"]');
  const data = Object.fromEntries(new FormData(form));
  button.disabled = true;
  form.querySelector(".form-error").textContent = "";
  try {
    if (kind === "project") {
      const result = await api(editingProject ? `/projects/${editingProject}` : "/projects", editingProject ? "PATCH" : "POST", data);
      selectedId = result.id;
    } else {
      await api(editingTask ? `/tasks/${editingTask}` : `/projects/${selectedId}/tasks`, editingTask ? "PATCH" : "POST", data);
    }
    $("status-filter").value = "";
    $(`${kind}-dialog`).close(); $("message").hidden = true;
    await refresh();
  } catch (error) {
    if ($(`${kind}-dialog`).open) form.querySelector(".form-error").textContent = error.message;
    else errorMessage(error);
  } finally { button.disabled = false; }
}

$("new-project").onclick = () => openProject();
$("edit-project").onclick = () => openProject(projects.find(p => p.id === selectedId));
$("new-task").onclick = () => openTask();
$("project-form").onsubmit = event => submitForm(event, "project");
$("task-form").onsubmit = event => submitForm(event, "task");
$("status-filter").onchange = () => refresh().catch(errorMessage);
$("delete-project").onclick = () => {
  const id = selectedId;
  if (confirm("Excluir este projeto? Projetos com tarefas não podem ser excluídos.")) {
    mutation($("delete-project"), () => api(`/projects/${id}`, "DELETE"));
  }
};
document.querySelectorAll("[data-close]").forEach(button => button.onclick = () => $(button.dataset.close).close());
refresh().catch(errorMessage);
