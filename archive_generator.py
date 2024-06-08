# archive_generator.py

import json
import os
import shutil
import zipfile


class ArchiveGenerator:
    """
    A class to generate an archive with the project content.

    Attributes:
    -----------
    project : Project
        An instance of the Project class containing project details.
    archive_name : str
        The name of the archive to be created.
    temp_dir : str
        The temporary directory used for creating the archive.
    """

    def __init__(self, project):
        self.project = project
        self.archive_name = f"{self.project.mod_name.lower().replace(' ', '')}.zip"
        self.temp_dir = "temp_project"

    def create_archive(self):
        """
        Creates the archive with the required project structure.
        """
        self.create_directory_structure()
        self.create_plugin_json()
        self.create_yaml_file()
        self.zip_directory()

    def create_directory_structure(self):
        """
        Creates the required directory structure for the project.
        """
        os.makedirs(os.path.join(self.temp_dir, "apis"), exist_ok=True)

    def create_plugin_json(self):
        """
        Creates the plugin.json file with the project details.
        """
        plugin_json_path = os.path.join(self.temp_dir, "plugin.json")
        with open(plugin_json_path, 'w') as file:
            json.dump(self.project.generate_plugin_json(), file, indent=2)

    def create_yaml_file(self):
        """
        Creates the .yaml file with the project details.
        """
        yaml_file_path = os.path.join(self.temp_dir, "apis", f"{self.project.mod_name.lower().replace(' ', '')}.yaml")
        with open(yaml_file_path, 'w') as file:
            file.write(self.project.generate_yaml_content())

    def zip_directory(self):
        """
        Zips the directory structure into a single archive file.
        """
        with zipfile.ZipFile(self.archive_name, 'w') as zipf:
            for root, dirs, files in os.walk(self.temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, self.temp_dir))
        shutil.rmtree(self.temp_dir)
