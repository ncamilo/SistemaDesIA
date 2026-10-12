import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.api import router
from app.database import Base, build_database
from app.services import Conflict, NotFound

STATIC = Path(__file__).parent / "static"


def create_app(database_url: str | None = None):
    url = database_url or os.getenv("DATABASE_URL", "sqlite:///./montagem.db")
    engine, session_factory = build_database(url)

    @asynccontextmanager
    async def lifespan(app):
        Base.metadata.create_all(engine)
        yield
        engine.dispose()

    app = FastAPI(title="Montagem · Projetos e tarefas", version="0.1.0", lifespan=lifespan)
    app.state.session_factory = session_factory

    @app.exception_handler(NotFound)
    async def not_found(_request: Request, error: NotFound):
        return JSONResponse(status_code=404, content={"detail": str(error)})

    @app.exception_handler(Conflict)
    async def conflict(_request: Request, error: Conflict):
        return JSONResponse(status_code=409, content={"detail": str(error)})

    app.include_router(router)
    if STATIC.exists():
        app.mount("/static", StaticFiles(directory=STATIC), name="static")

        @app.get("/", include_in_schema=False)
        def home():
            return FileResponse(STATIC / "index.html")

    return app


app = create_app()
