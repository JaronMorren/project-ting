def exists_word(word, instance):
    # Creates an empty list to store the results
    results = []

    # Iterates over each index in the instance
    for index in range(len(instance)):
        # Retrieves the file at the current index from the instance
        file = instance.search(index)
        # Creates a dictionary 'data' to store information
        #  about the word occurrences in the file
        data = {
            "palavra": word,  # Stores the word being searched
            "arquivo": file["nome_do_arquivo"],  # Stores the file name
            "ocorrencias": [],
            # Creates an empty list to store the occurrences
        }
        # Iterates over each line in the file
        for line in file["linhas_do_arquivo"]:
            # Checks if the word (case-insensitive) exists in the current line
            if word.lower() in line.lower():
                # If the word is found,
                # appends the line number to the 'ocorrencias' list
                data["ocorrencias"].append(
                    {"linha": file["linhas_do_arquivo"].index(line) + 1}
                )
        # Checks if there are any occurrences for the current file
        if data["ocorrencias"]:
            # If there are occurrences, appends the 'data' dictionary
            #  to the 'results' list
            results.append(data)
            # Returns the 'results' list containing
            #  the occurrences of the word in the files
        return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
