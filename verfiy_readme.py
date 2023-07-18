import os
import re
import argparse
import subprocess


def get_files_and_dirs(root_path):
    """Return the file and directory structure starting from the root_path."""
    structure = {}

    for root, _, files in os.walk(root_path):
        relative_root = os.path.relpath(root, root_path)
        structure[relative_root] = []

        for file in files:
            structure[relative_root].append(file)

    return structure


def get_entries_from_readme(readme_path):
    """Return a list of entries parsed from the README.md file."""
    readme_structure = {r".": []}

    if not os.path.exists(readme_path):
        return readme_structure

    with open(readme_path, "r") as f:
        content = f.read()

    links = re.findall(r"\`(.*?)\`", content)

    cheatsheet_dir = r"."
    for link in links:
        if ".md" in link:
            readme_structure[cheatsheet_dir].append(link)
        else:
            cheatsheet_dir = link
            readme_structure[link] = []

    return readme_structure


def find_missing_entries(structure, readme_structure):
    """Return a list of entries present in the structure but missing in the readme_structure."""
    missing_entries = {}

    for dir, files in structure.items():
        if dir not in readme_structure:
            missing_entries[dir] = files
        else:
            for file in files:
                if file not in readme_structure[dir]:
                    if dir not in missing_entries:
                        missing_entries[dir] = []
                    missing_entries[dir].append(file)

    return missing_entries


def print_missing_entries(missing_entries):
    """Print the missing entries in a readable format."""
    for dir, files in missing_entries.items():
        print(f"Directory: {dir}")
        for file in files:
            print(f" - Missing file: {file}")
        print()


def find_emtpy_files(structure):
    """Find files that have 0 lines"""
    small_files = []
    for dir in structure:
        if dir == ".":
            path = "./cheatsheets/"
        else:
            path = f"./cheatsheets/{dir}"

        for file in structure[dir]:
            file_len = subprocess.check_output(f"wc -l {path}/{file}", shell=True)
            file_len = int(file_len.decode("utf-8").split(" ")[0])
            if file_len <= 1:
                small_files.append((file, file_len))
    return small_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verfify validity of README.md, and get insights about cheatsheets')
    parser.add_argument('-r', '--readme', type=str, default='README.md',
                        help='Path to the readme file.')
    parser.add_argument('-s', '--small-files', action='store_true',
                        help='Size of each batch.')

    args = parser.parse_args()

    root_dir = "./cheatsheets"
    structure = get_files_and_dirs(root_dir)

    if args.small_files:
        small_files = find_emtpy_files(structure)
        for file in small_files:
            print(f"{file[0]} has length {file[1]}")
    else:
        readme_structure = get_entries_from_readme(os.path.join("./", "README.md"))
        missing_entries = find_missing_entries(structure, readme_structure)
        print_missing_entries(missing_entries)
