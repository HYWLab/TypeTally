# TypeTally

![TypeTally social preview](assets/social-preview.png)

TypeTally is a lightweight Windows desktop app that counts files in any folder and shows a clean breakdown by file type.

It is designed for people who need a fast answer to questions like:

- How many PDFs are in this folder?
- How many different file types are mixed into this download?
- What is actually inside this shared archive or classwork folder?

## Why people may want it

- Instant folder analysis
- Clear file-type breakdown
- Works with or without subfolders
- Single-window desktop app
- No terminal window
- Portable standalone `.exe`

## Download

If you are browsing the repository directly, use the packaged Windows build here:

- [`release/TypeTally-Windows-x64.zip`](release/TypeTally-Windows-x64.zip)

After the GitHub repository is created, the recommended setup is:

1. Open the latest GitHub Release
2. Download `TypeTally-Windows-x64.zip`
3. Extract it
4. Run `TypeTally.exe`

## Features

- Count all files in a folder
- Optionally include subfolders
- Group results by extension such as `.pdf`, `.docx`, `.jpg`, and `.zip`
- Clean English interface for sharing publicly
- Custom app icon and GitHub-ready branding

## Screenshots and branding

The repository uses a privacy-safe demo path in its visuals:

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

Build the app:

```powershell
./build.ps1
```

The packaged executable will be created in `release-build/`.

## Repository suggestions

To help the project get more attention on GitHub, set these when creating the repo:

- Description: `A tiny Windows app that counts files and shows a clean file-type breakdown.`
- Topics: `windows`, `desktop-app`, `python`, `tkinter`, `file-manager`, `productivity`, `folder-analysis`, `utility`
- Social preview: `assets/social-preview.png`

## License

MIT
