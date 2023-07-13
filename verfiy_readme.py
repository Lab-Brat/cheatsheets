import os
import re


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


if __name__ == "__main__":
    root_dir = "./cheatsheets"
    structure = get_files_and_dirs(root_dir)
    readme_structure = get_entries_from_readme(os.path.join("./", "README.md"))

    missing_entries = find_missing_entries(structure, readme_structure)

    print_missing_entries(missing_entries)
