# project.py

class Project:
    """
    A class to represent a project.

    Attributes:
    -----------
    id : str
        The unique identifier of the project.
    name : str
        The name of the project.
    version : str
        The version of the project.
    description : str
        The description of the project.
    author : str
        The author of the project.
    weight : int
        The weight of the project.
    supported_versions : list
        List of supported versions.
    mc_version : str
        The Minecraft version (e.g., forge-1.20.1).
    mod_id : str
        The mod ID.
    mod_name : str
        The mod name.
    file_id : str
        The file ID.
    """

    def __init__(self, id, name, version, description, author, weight, supported_versions, mc_version, mod_id, mod_name,
                 file_id):
        self.id = id
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.weight = weight
        self.supported_versions = supported_versions
        self.mc_version = mc_version
        self.mod_id = mod_id
        self.mod_name = mod_name
        self.file_id = file_id

    def generate_plugin_json(self):
        """
        Generates the content for the plugin.json file.

        Returns:
        --------
        dict
            A dictionary containing the content for plugin.json.
        """
        return {
            "id": self.id,
            "weight": self.weight,
            "supportedversions": self.supported_versions,
            "info": {
                "name": self.name,
                "version": self.version,
                "description": self.description,
                "author": self.author
            }
        }

    def generate_yaml_content(self):
        """
        Generates the content for the .yaml file.

        Returns:
        --------
        str
            A string containing the content for the .yaml file.
        """
        return f"""---
{self.mc_version}:
  gradle: |
    repositories {{
      maven {{
          url = 'https://cursemaven.com/'
      }}
    }}

    dependencies {{
      implementation fg.deobf('curse.maven:{self.mod_name}-{self.mod_id}:{self.file_id}')
    }}
  update_files:
    - ~
name: "{self.name}"
"""
