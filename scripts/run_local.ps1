$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$env:PYTHONPATH = Join-Path $Root "src"

Write-Host ""
Write-Host "=== PBSA local tests ===" -ForegroundColor Cyan
python -m unittest discover -s tests

Write-Host ""
Write-Host "=== PBSA single benchmark ===" -ForegroundColor Cyan
python -m pba.cli run-benchmark --domain ".\configs\domains\temperature_like.json"

Write-Host ""
Write-Host "=== PBSA suite benchmark ===" -ForegroundColor Cyan
python -m pba.cli run-suite --config ".\configs\suite_v1_0.json"

Write-Host ""
Write-Host "PBSA local run complete. No GitHub push performed." -ForegroundColor Green