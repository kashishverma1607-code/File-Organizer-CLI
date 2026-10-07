import os
import shutil
import argparse


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    if extension in [".pdf", ".docx", ".txt", ".xlsx"]:
        return "Documents"

    elif extension in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"

    elif extension in [".mp3", ".wav"]:
        return "Audio"

    elif extension in [".mp4", ".mkv", ".avi"]:
        return "Videos"

    else:
        return "Others"


def organize_files(folder, dry_run=False):

    if not os.path.exists(folder):
        print(f"Error: Folder does not exist: {folder}")
        return 2

    if not os.path.isdir(folder):
        print(f"Error: The given path is not a folder: {folder}")
        return 1

    if dry_run:
        print(f"\nDry run: No files will be moved.\n")
    else:
        print(f"\nOrganizing files in: {folder}\n")

    try:
        for file in os.listdir(folder):

            source = os.path.join(folder, file)

            if os.path.isfile(source):

                category = get_category(file)

                destination_folder = os.path.join(folder, category)

                destination = os.path.join(destination_folder, file)

                if os.path.exists(destination):
                    print(f"Skipped: {file} already exists in {category}")
                    continue

                if dry_run:
                    print(f"Would move: {file} -> {category}")

                else:
                    os.makedirs(destination_folder, exist_ok=True)

                    shutil.move(source, destination)

                    print(f"Moved: {file} -> {category}")

    except PermissionError:
        print("Error: Permission denied.")
        return 3

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 130

    except Exception as error:
        print("Error: Something went wrong.")
        print(f"Reason: {error}")
        return 1

    if dry_run:
        print("\nDry run completed. No files were moved.")
    else:
        print("\nFile organization completed!")

    return 0


def main():

    parser = argparse.ArgumentParser(
        description="Organize files into folders based on their file type."
    )

    parser.add_argument(
        "folder",
        help="Path of the folder whose files you want to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving files"
    )

    args = parser.parse_args()

    return organize_files(args.folder, args.dry_run)


if __name__ == "__main__":
    import sys
    sys.exit(main())