$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host "=== PBSA LIGHT REPO DUMP ==="
Write-Host "Root: $Root"
Write-Host ""

Get-ChildItem -Recurse -Force |
    Where-Object {
        $_.FullName -notmatch "\\\.git\\" -and
        $_.FullName -notmatch "\\\.venv\\" -and
        $_.FullName -notmatch "\\__pycache__\\"
    } |
    ForEach-Object {
        $_.FullName.Replace($Root, ".")
    }