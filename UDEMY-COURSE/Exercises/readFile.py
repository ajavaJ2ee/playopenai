open_file= open('Exercises/data.txt', 'r')


contents=open_file.read()

open_file.close()

print(contents)

input_content= input('Enter your name:')

file_write=open('Exercises/data.txt', 'w')
file_write.write(input_content)

file_write.close()