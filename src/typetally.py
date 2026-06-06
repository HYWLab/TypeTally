from __future__ import annotations

from collections import Counter
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


def collect_files(folder: Path, include_subfolders: bool) -> list[Path]:
    if include_subfolders:
        return [item for item in folder.rglob("*") if item.is_file()]
    return [item for item in folder.iterdir() if item.is_file()]


def get_file_type(file_path: Path) -> str:
    if file_path.suffix:
        return file_path.suffix.lower()
    return "(无扩展名)"


def summarize_types(files: list[Path]) -> list[tuple[str, int]]:
    counter = Counter(get_file_type(file_path) for file_path in files)
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def resource_path(name: str) -> Path:
    if getattr(sys, "frozen", False):
        base_path = Path(getattr(sys, "_MEIPASS", Path(sys.executable).resolve().parent))
        direct_path = base_path / name
        if direct_path.exists():
            return direct_path
        return base_path / "assets" / name

    source_dir = Path(__file__).resolve().parent
    direct_path = source_dir / name
    if direct_path.exists():
        return direct_path
    return source_dir.parent / "assets" / name


class FolderCounterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("TypeTally")
        self.root.geometry("720x520")
        self.root.resizable(False, False)

        self.folder_var = tk.StringVar()
        self.include_subfolders_var = tk.BooleanVar(value=True)
        self.result_var = tk.StringVar(value="Choose a folder to begin.")
        self.detail_var = tk.StringVar(value="The breakdown will appear in the table below.")

        self.build_ui()
        self.set_window_icon()

    def build_ui(self) -> None:
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        title = ttk.Label(
            frame,
            text="TypeTally",
            font=("Microsoft YaHei UI", 16, "bold"),
        )
        title.pack(anchor="w", pady=(0, 16))

        subtitle = ttk.Label(
            frame,
            text="Count files and see how many of each file type are inside a folder.",
            foreground="#555555",
        )
        subtitle.pack(anchor="w", pady=(0, 16))

        row = ttk.Frame(frame)
        row.pack(fill="x")

        path_entry = ttk.Entry(row, textvariable=self.folder_var)
        path_entry.pack(side="left", fill="x", expand=True)

        browse_button = ttk.Button(row, text="Browse Folder", command=self.choose_folder)
        browse_button.pack(side="left", padx=(8, 0))

        option = ttk.Checkbutton(
            frame,
            text="Include files in subfolders",
            variable=self.include_subfolders_var,
        )
        option.pack(anchor="w", pady=(16, 10))

        count_button = ttk.Button(frame, text="Analyze Folder", command=self.run_count)
        count_button.pack(anchor="w")

        result_label = ttk.Label(
            frame,
            textvariable=self.result_var,
            font=("Microsoft YaHei UI", 13),
            foreground="#0f5c2e",
        )
        result_label.pack(anchor="w", pady=(20, 0))

        detail_label = ttk.Label(
            frame,
            textvariable=self.detail_var,
            foreground="#555555",
        )
        detail_label.pack(anchor="w", pady=(8, 12))

        table_frame = ttk.Frame(frame)
        table_frame.pack(fill="both", expand=True)

        columns = ("file_type", "count")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        self.tree.heading("file_type", text="File Type")
        self.tree.heading("count", text="Count")
        self.tree.column("file_type", width=420, anchor="w")
        self.tree.column("count", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        hint_label = ttk.Label(
            frame,
            text="Example: if a folder contains PDFs, Word files, and images, TypeTally will list each type separately.",
            foreground="#555555",
            wraplength=640,
        )
        hint_label.pack(anchor="w", pady=(12, 0))

    def set_window_icon(self) -> None:
        icon_png = resource_path("typetally_icon.png")
        if not icon_png.exists():
            return

        try:
            self.icon_image = tk.PhotoImage(file=str(icon_png))
            self.root.iconphoto(True, self.icon_image)
        except tk.TclError:
            pass

    def choose_folder(self) -> None:
        selected = filedialog.askdirectory(title="Choose a folder")
        if selected:
            self.folder_var.set(selected)
            self.result_var.set("Click Analyze Folder to see the results.")

    def run_count(self) -> None:
        folder_text = self.folder_var.get().strip()
        if not folder_text:
            messagebox.showwarning("TypeTally", "Please choose a folder first.")
            return

        folder = Path(folder_text)
        if not folder.exists() or not folder.is_dir():
            messagebox.showerror("TypeTally", "The selected path is not a valid folder.")
            return

        try:
            files = collect_files(folder, self.include_subfolders_var.get())
        except PermissionError:
            messagebox.showerror("TypeTally", "Some items in this folder could not be accessed.")
            return
        except OSError as exc:
            messagebox.showerror("TypeTally", f"Analysis failed: {exc}")
            return

        total = len(files)
        type_summary = summarize_types(files)
        scope = "Including subfolders" if self.include_subfolders_var.get() else "Current folder only"
        self.result_var.set(f"{scope}: {total} files found")
        self.detail_var.set(f"{len(type_summary)} file types detected")

        for item in self.tree.get_children():
            self.tree.delete(item)

        for file_type, count in type_summary:
            self.tree.insert("", "end", values=(file_type, count))


def main() -> None:
    root = tk.Tk()
    app = FolderCounterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
