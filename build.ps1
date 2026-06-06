$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$srcDir = Join-Path $projectRoot "src"
$assetsDir = Join-Path $projectRoot "assets"
$buildDir = Join-Path $projectRoot "build"
$releaseBuildDir = Join-Path $projectRoot "release-build"
$specDir = Join-Path $projectRoot "build-spec"
$entryFile = Join-Path $srcDir "typetally_gui.pyw"
$iconFile = Join-Path $assetsDir "typetally_icon.ico"
$iconPng = Join-Path $assetsDir "typetally_icon.png"

New-Item -ItemType Directory -Force $buildDir, $releaseBuildDir, $specDir | Out-Null

$pyInstallerScript = Join-Path $env:APPDATA "Python\Python313\Scripts\pyinstaller.exe"
if (Test-Path $pyInstallerScript) {
    & $pyInstallerScript `
        --noconfirm `
        --clean `
        --onefile `
        --windowed `
        --name TypeTally `
        --icon $iconFile `
        --add-data "$iconPng;assets" `
        --distpath $releaseBuildDir `
        --workpath $buildDir `
        --specpath $specDir `
        $entryFile
    exit $LASTEXITCODE
}

python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name TypeTally `
    --icon $iconFile `
    --add-data "$iconPng;assets" `
    --distpath $releaseBuildDir `
    --workpath $buildDir `
    --specpath $specDir `
    $entryFile
