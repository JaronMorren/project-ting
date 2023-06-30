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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
