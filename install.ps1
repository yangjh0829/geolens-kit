# GeoLens installer - Windows PowerShell 5.1+
# NOTE: deliberately ASCII-only. Windows PowerShell 5.1 reads .ps1 as ANSI
# unless a BOM is present, and CJK text would break the parser.
# Installs this package to the user-level skills folder. Then just tell your
# agent: "use geolens on this photo".

$ErrorActionPreference = 'Stop'
$src  = Split-Path -Parent $MyInvocation.MyCommand.Definition
$dest = Join-Path $env:USERPROFILE '.workbuddy\skills\geolens'

if (Test-Path $dest) {
    Write-Warning "Target already exists: $dest"
    Write-Warning "Back it up or remove it first; this script never overwrites."
    exit 1
}

$parent = Split-Path -Parent $dest
New-Item -ItemType Directory -Force -Path $parent | Out-Null
Copy-Item -Path $src -Destination $dest -Recurse -Force
Remove-Item -Path (Join-Path $dest '.git') -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path (Join-Path $dest '__pycache__') -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Installed: $dest"
Write-Host "Self-check: python `"$dest\scripts\check.py`""
Write-Host 'Usage: tell your agent "use geolens on this photo: <path>"'
