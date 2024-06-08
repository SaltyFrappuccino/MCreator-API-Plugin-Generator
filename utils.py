# utils.py

import re


def parse_curseforge_url(url):
    """
    Parses the CurseForge URL to extract the mod name and file ID.

    Parameters:
    -----------
    url : str
        The URL of the CurseForge page.

    Returns:
    --------
    tuple
        A tuple containing the mod name and file ID.
    """
    pattern = r'/mc-mods/([^/]+)/files/(\d+)'
    match = re.search(pattern, url)
    if match:
        mod_name, file_id = match.groups()
        return mod_name, file_id
    else:
        raise ValueError("Invalid URL format")
