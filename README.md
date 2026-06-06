# TypeTally
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![TypeTally social preview](assets/social-preview.png)

TypeTally is a Windows desktop app that scans a folder and shows how many files it contains, with a clear breakdown by file type.

It is useful when you want quick answers to questions like:

- How many PDFs are in this folder?
- What file types are mixed into this download?
- What is actually inside this shared folder before I sort it manually?

## What it does

- Counts files in a selected folder
- Groups results by extension such as `.pdf`, `.docx`, `.jpg`, and `.zip`
- Optionally includes files from subfolders
- Shows the results in a simple desktop interface

## Download

- [`release/TypeTally-Windows-x64.zip`](release/TypeTally-Windows-x64.zip)

1. Open the latest GitHub Release
2. Download `TypeTally-Windows-x64.zip`
3. Extract it
4. Run `TypeTally.exe`

## Use cases

- Checking student submission folders before review
- Looking through large download folders with mixed file types
- Inspecting shared work folders before cleanup or archiving
- Getting a quick inventory of documents, images, and other files without using the command line

## Privacy note

The preview images in this repository use a privacy-safe demo path:

- `D:\Downloads\Sample_Folder`

No personal folder names or local user information are included in the public assets.

## Build from source

Requirements:

- Windows
- Python 3.13 or newer recommended
- `PyInstaller`

Install PyInstaller:

```powershell
python -m pip install --user pyinstaller
```

Then build the app:

```powershell
./build.ps1
```

The built executable is created in `release-build/`.

## License

MIT
