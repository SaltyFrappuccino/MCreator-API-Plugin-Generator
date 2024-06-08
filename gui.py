# gui.py

import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox

from archive_generator import ArchiveGenerator
from project import Project
from utils import parse_curseforge_url


class ProjectGUI:
    """
    A class to represent the GUI for project input.

    Methods:
    --------
    create_widgets():
        Creates and places all widgets in the GUI.
    generate_archive():
        Handles the generation of the project archive.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("MCreator API Plugin Generator")
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and places all widgets in the GUI.
        """
        # Labels and entry fields
        ttk.Label(self.root, text="Project ID:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.project_id = ttk.Entry(self.root)
        self.project_id.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Project Name:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.project_name = ttk.Entry(self.root)
        self.project_name.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Version:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.version = ttk.Entry(self.root)
        self.version.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Description:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.description = ttk.Entry(self.root)
        self.description.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Author:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.author = ttk.Entry(self.root)
        self.author.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Weight:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.weight = ttk.Entry(self.root)
        self.weight.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Supported Versions:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.supported_versions = ttk.Entry(self.root)
        self.supported_versions.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Minecraft Version:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.mc_version = ttk.Entry(self.root)
        self.mc_version.grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Mod ID:").grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
        self.mod_id = ttk.Entry(self.root)
        self.mod_id.grid(row=8, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="CurseForge URL:").grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
        self.url = ttk.Entry(self.root)
        self.url.grid(row=9, column=1, padx=10, pady=5)

        author_label = ttk.Label(self.root, text="Author: ")
        author_label.grid(row=10, column=0, padx=10, pady=5, sticky=tk.E)

        author_link = tk.Label(self.root, text="SaltyFrappuccino", fg="blue", cursor="hand2")
        author_link.grid(row=10, column=1, padx=10, pady=5, sticky=tk.W)
        author_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/SaltyFrappuccino"))

        self.generate_button = ttk.Button(self.root, text="Generate Plugin", command=self.generate_archive)
        self.generate_button.grid(row=11, column=0, columnspan=2, pady=10)

    def generate_archive(self):
        """
        Handles the generation of the project archive.
        """
        try:
            # Parse URL to get mod_name and file_id
            mod_name, file_id = parse_curseforge_url(self.url.get())

            # Get supported versions as a list
            supported_versions = list(map(int, self.supported_versions.get().split(',')))

            # Create Project instance
            project = Project(
                id=self.project_id.get(),
                name=self.project_name.get(),
                version=self.version.get(),
                description=self.description.get(),
                author=self.author.get(),
                weight=int(self.weight.get()),
                supported_versions=supported_versions,
                mc_version=self.mc_version.get(),
                mod_id=self.mod_id.get(),
                mod_name=mod_name,
                file_id=file_id
            )

            # Create ArchiveGenerator instance and generate the archive
            archive_generator = ArchiveGenerator(project)
            archive_generator.create_archive()

            messagebox.showinfo("Success", "Archive generated successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectGUI(root)
    root.mainloop()
