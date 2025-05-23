# Build.ps1 for ShowMiiWADs-Py

# Default option is to run build, like a Makefile
param(
    [string]$Task = "build"
)

$buildShowMiiWADsPy = {
    Write-Host "Building ShowMiiWADs-Py..."
    # python build_translations.py
    cd rust_modules && python -m maturin develop --release
    python -m nuitka --show-progress --assume-yes-for-downloads ShowMiiWADs-Py.py
}

$cleanShowMiiWADsPy = {
    Write-Host "Cleaning..."
    Remove-Item -Recurse -Force ShowMiiWADs-Py.exe, ./ShowMiiWADs-Py.build/, ./ShowMiiWADs-Py.dist/, ./ShowMiiWADs-Py.onefile-build/
}

switch ($Task.ToLower()) {
    "build" {
        & $buildShowMiiWADsPy
        break
    }
    "clean" {
        & $cleanShowMiiWADsPy
        break
    }
    default {
        Write-Host "Unknown task: $Task" -ForegroundColor Red
        Write-Host "Available tasks: build, clean"
        break
    }
}
