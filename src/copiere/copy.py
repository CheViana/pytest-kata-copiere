import pathlib
import shutil


def copy_file_or_dir(source_path: pathlib.Path, dest_folder: str):
    print(f"Copying {source_path} to {dest_folder}")
    if source_path.is_dir():
        shutil.copytree(source_path, f"{dest_folder}/{source_path.parts[-1]}")
    else:
        shutil.copy2(source_path, f"{dest_folder}/{source_path.name}")
