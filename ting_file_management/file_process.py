import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # Iterates over the indices of instance using the range function
    for index in range(len(instance)):
        # Checks if the file name value at the current index matches path_file
        if instance.search(index)["nome_do_arquivo"] == path_file:
            # If a matching file is found, return None and exit the function
            return None

    # Calls the txt_importer function to import
    # the contents of the file specified by path_file
    lines = txt_importer(path_file)

    # Creating a dictionary named file
    # to store information about the file
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    # Enqueueing the file dictionary into the instance queue
    instance.enqueue(file)
    print(file)


def remove(instance):
    # Check if the 'instance' parameter is empty
    if len(instance) == 0:
        # If it is empty, print a message indicating that there are no elements
        return print("Não há elementos", file=sys.stdout)
    # Removes the first element using the 'dequeue()' method
    #  and assign it to 'file_to_delete'
    file_to_delete = instance.dequeue()
    # Prints a success message with the name of the file that was removed
    print(
        f'Arquivo {file_to_delete["nome_do_arquivo"]} removido com sucesso',
        file=sys.stdout,
    )


def file_metadata(instance, position):
    try:
        # Try to search for the element
        #  at the given 'position' in the 'instance'
        # and print the result
        print(instance.search(position))
    except IndexError:
        # If an IndexError occurs,
        # catch the exception and print
        # an error message indicating an invalid position
        print("Posição inválida", file=sys.stderr)
