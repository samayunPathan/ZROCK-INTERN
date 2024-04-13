def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("Contents of the file:", contents)
    except FileNotFoundError:
        print("File not found.")


read_file("sample.txt")
