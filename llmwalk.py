import os

OUTPUT_FILENAME = "compiled_project.txt"
ROOT_DIR = "."  # Change this to the desired root directory

def build_file_tree(start_path):
    tree = ""
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, "").count(os.sep)
        indent = "    " * level
        tree += f"{indent}{os.path.basename(root)}/\n"
        sub_indent = "    " * (level + 1)
        for f in files:
            tree += f"{sub_indent}{f}\n"
    return tree

def collect_file_contents(start_path):
    contents = ""
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    file_data = f.read()
                contents += "\n" + "="*80 + "\n"
                contents += f"FILE: {file_path}\n"
                contents += "="*80 + "\n"
                contents += file_data + "\n"
            except Exception as e:
                contents += "\n" + "="*80 + "\n"
                contents += f"FILE: {file_path} (ERROR READING FILE: {e})\n"
                contents += "="*80 + "\n"
    return contents

def main():
    print("Building file tree and collecting file contents...")
    file_tree = build_file_tree(ROOT_DIR)
    file_contents = collect_file_contents(ROOT_DIR)

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as out_file:
        out_file.write("PROJECT FILE TREE:\n")
        out_file.write(file_tree)
        out_file.write("\n\nPROJECT FILE CONTENTS:\n")
        out_file.write(file_contents)

    print(f"Compilation complete. Output written to {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()

