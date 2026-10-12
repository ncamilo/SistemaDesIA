param(
    [ValidateSet('install', 'run', 'demo', 'test', 'check', 'format', 'browser-install', 'browser-test')]
    [string]$Command = 'check'
)
$ErrorActionPreference = 'Stop'
$projectPython = Join-Path $PSScriptRoot '..\.venv\Scripts\python.exe'
if (Test-Path -LiteralPath $projectPython) {
    & $projectPython (Join-Path $PSScriptRoot 'dev.py') $Command
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3.14 (Join-Path $PSScriptRoot 'dev.py') $Command
} else {
    & python (Join-Path $PSScriptRoot 'dev.py') $Command
}
exit $LASTEXITCODE
