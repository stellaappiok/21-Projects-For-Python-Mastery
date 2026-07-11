import json
import os
import shutil
from subprocess import PIPE, run

SEARCH_KEYWORD = "game"
GO_EXTENSION = ".go"
BUILD_COMMAND = ["go", "build"]


def find_game_directories(source_folder):
    """Find folders whose names contain 'game'."""
    game_dirs = []

    for item in os.scandir(source_folder):
        if item.is_dir() and SEARCH_KEYWORD in item.name.lower():
            game_dirs.append(item.path)

    return game_dirs


def get_output_names(paths):
    """Remove '_game' from folder names."""
    return [
        os.path.basename(path).replace("_game", "")
        for path in paths
    ]


def copy_folder(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def write_metadata(output_folder, names):
    metadata = {
        "gameNames": names,
        "numberOfGames": len(names)
    }

    metadata_file = os.path.join(output_folder, "metadata.json")

    with open(metadata_file, "w") as file:
        json.dump(metadata, file, indent=4)


def find_go_file(folder):
    for file in os.listdir(folder):
        if file.endswith(GO_EXTENSION):
            return file
    return None


def compile_game(folder):
    go_file = find_go_file(folder)

    if go_file is None:
        print(
            f"No Go file found in '{os.path.basename(folder)}'. Skipping compilation.")
        return

    current = os.getcwd()

    try:
        os.chdir(folder)

        result = run(
            BUILD_COMMAND + [go_file],
            stdout=PIPE,
            stderr=PIPE,
            text=True
        )

        if result.returncode == 0:
            print(f"Compiled {go_file} successfully.")
        else:
            print(f"Failed to compile {go_file}.")
            print(result.stderr)

    finally:
        os.chdir(current)


def process_games(source_folder, output_folder):
    game_folders = find_game_directories(source_folder)

    if not game_folders:
        print("No game folders were found.")
        write_metadata(output_folder, [])
        return

    output_names = get_output_names(game_folders)

    for source, name in zip(game_folders, output_names):
        destination = os.path.join(output_folder, name)

        print(f"Copying '{name}'...")
        copy_folder(source, destination)

        print(f"Compiling '{name}'...")
        compile_game(destination)

    write_metadata(output_folder, output_names)

    print("\nFinished!")
    print(f"{len(output_names)} game(s) processed.")


def main():
    current_directory = os.getcwd()

    source_folder = os.path.join(current_directory, "games")
    output_folder = os.path.join(current_directory, "output")

    # Automatically create folders
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    print("Source folder :", source_folder)
    print("Output folder :", output_folder)
    print()

    process_games(source_folder, output_folder)


if __name__ == "__main__":
    main()
