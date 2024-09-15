def save_file(content,fileName):
    with open(fileName,'w') as file:
        file.write(content)

def read_file(fileName):
    with open(fileName,'r') as file:
        return file.read()