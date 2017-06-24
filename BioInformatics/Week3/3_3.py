def string_spelled_by_genome(list_of_strings):
    string = list_of_strings[0]
    for i in list_of_strings[1:]:
        string += i[-1]
    return string


print(string_spelled_by_genome(['ACCGA'
,'CCGAA'
,'CGAAG'
,'GAAGC'
,'AAGCT']))
