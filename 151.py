with open("names.txt", 'r') as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)