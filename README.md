# PyQt Calculator (Lab 24)

Simple four-function calculator built with PyQt5 and packaged as a Windows executable.

## What’s here
- `calculator.py`: PyQt5 UI and controller.
- `calculator.ico`: window/app icon.
- `calculator.spec`: PyInstaller spec used to build the executable.
- `dist/calculator.exe`: packaged executable (no console window).
- `build/`: PyInstaller build artifacts.

## Run from source
1) Install Python 3.10+ and pip.
2) `pip install PyQt5`
3) `python calculator.py`

## Use the packaged EXE
Run `dist/calculator.exe` (double-click or run from terminal). No additional installs required.

## Build the EXE yourself
From the repo root:
```
pip install PyQt5 pyinstaller
pyinstaller --noconsole --onefile --icon calculator.ico calculator.py
```
The executable will appear in `dist/` (matching the provided `calculator.spec`).
