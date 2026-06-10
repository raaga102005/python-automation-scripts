import os
import shutil
from datetime import datetime

def rename_files(folder_path, prefix='', add_number=True, add_date=False, dry_run=True):
    """
    Renames all files in a folder with a consistent pattern.

    Options:
    - prefix: add a text prefix to every file (e.g. 'invoice_')
    - add_number: add sequential numbers (001, 002, 003...)
    - add_date: add today's date to filename
    - dry_run: if True, only shows what WOULD happen without renaming
               set to False to actually rename files

    Example: 'IMG_4829.jpg' becomes 'photo_001_2026-06-08.jpg'
    """

    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    # Get all files (not folders) in the directory
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found in folder.")
        return

    files.sort()
    today = datetime.now().strftime('%Y-%m-%d')

    print(f"Found {len(files)} files in {folder_path}")
    if dry_run:
        print("DRY RUN — no files will actually be renamed")
        print("Set dry_run=False to actually rename\n")

    renamed_count = 0

    for i, filename in enumerate(files, start=1):
        name, ext = os.path.splitext(filename)
        new_name = prefix

        if add_number:
            new_name += f"{str(i).zfill(3)}_"

        if add_date:
            new_name += f"{today}_"

        new_name += name + ext

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        print(f"  {filename}  →  {new_name}")

        if not dry_run:
            os.rename(old_path, new_path)
            renamed_count += 1

    if dry_run:
        print(f"\nDry run complete. {len(files)} files would be renamed.")
        print("Change dry_run=False to apply changes.")
    else:
        print(f"\nDone. {renamed_count} files renamed successfully.")


def bulk_rename_by_extension(folder_path, extension, new_prefix):
    """
    Renames only files with a specific extension.
    Example: rename all .jpg files to 'photo_001.jpg', 'photo_002.jpg' etc.
    """
    files = [f for f in os.listdir(folder_path)
             if f.endswith(extension) and os.path.isfile(os.path.join(folder_path, f))]

    files.sort()
    print(f"Found {len(files)} {extension} files")

    for i, filename in enumerate(files, start=1):
        new_name = f"{new_prefix}_{str(i).zfill(3)}{extension}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"  {filename} → {new_name}")

    print(f"Done. {len(files)} files renamed.")


if __name__ == "__main__":
    # Example 1: Preview renaming all files in a folder
    rename_files(
        folder_path="./test_folder",
        prefix="file_",
        add_number=True,
        add_date=True,
        dry_run=True  # Change to False to actually rename
    )

    # Example 2: Rename only .jpg files
    # bulk_rename_by_extension("./photos", ".jpg", "photo")
