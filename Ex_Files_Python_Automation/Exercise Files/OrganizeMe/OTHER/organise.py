import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "OTHER"

def organiseDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath = Path(item)
        filetype = filepath.suffix.lower()
        directory = pickDirectory(filetype)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            directory_path.mkdir()
        filepath.rename(directory_path.joinpath(filepath))

organiseDirectory()