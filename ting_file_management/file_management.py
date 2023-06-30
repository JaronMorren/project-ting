import sys


def txt_importer(path_file):
    # Checks if the file does not have a ".txt" extension
    if not path_file.endswith(".txt"):
        # Prints an error message to the standard error output using sys.stderr
        return print("Formato inválido", file=sys.stderr)
    try:
        # Opens the file in read mode using a context manager
        with open(path_file, "r") as file:
            # Reads the contents of the file and splitting it into lines
            lines = file.read().split("\n")
        return lines
    except FileNotFoundError:
        # Prints an error message with the file name to sys.stderr
        # if the file is not found
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
