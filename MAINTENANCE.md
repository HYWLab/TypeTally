# TypeTally Maintenance

This file is a quick guide for future updates.

## Project layout

- `src/typetally.py`: main desktop application
- `src/typetally_gui.pyw`: GUI entry point without console window
- `assets/`: icon and GitHub social preview image
- `build.ps1`: one-command Windows build script
- `release/`: public downloadable files committed to the repository

## Typical update flow

1. Edit the app in `src/`
2. Test locally
3. Rebuild the `.exe`
4. Replace files in `release/`
5. Commit and push

## Rebuild command

```powershell
./build.ps1
```

The rebuilt executable will be written to:

- `release-build/TypeTally.exe`

After checking it works, copy the final deliverables into:

- `release/TypeTally.exe`
- `release/TypeTally-Windows-x64.zip`

## Suggested release steps

```powershell
git status
./build.ps1
Copy-Item .\release-build\TypeTally.exe .\release\TypeTally.exe -Force
Compress-Archive -Path .\release\TypeTally.exe -DestinationPath .\release\TypeTally-Windows-x64.zip -Force
git add .
git commit -m "Describe the update"
git push
```

## GitHub tips

- Keep the repository description focused on the app value
- Keep `assets/social-preview.png` updated when branding changes
- Use GitHub Releases if you want clearer download buttons for each version
