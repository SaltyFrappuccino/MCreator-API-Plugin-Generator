# main.py

from archive_generator import ArchiveGenerator
from project import Project
from utils import parse_curseforge_url


def main():
    url = "https://www.curseforge.com/minecraft/mc-mods/sorceryfight/files/5358535"
    mod_name, file_id = parse_curseforge_url(url)

    project = Project(
        id="Jujutsu Craft (Sorcery Fight)",
        name="Jujutsu Craft (Sorcery Fight)",
        version="2.0.0",
        description="JujutsuCraft Support",
        author="Satushi",
        weight=22,
        supported_versions=[2024001],
        mc_version="forge-1.20.1",
        mod_id="471288",
        mod_name=mod_name,
        file_id=file_id
    )

    archive_generator = ArchiveGenerator(project)
    archive_generator.create_archive()


if __name__ == "__main__":
    main()
