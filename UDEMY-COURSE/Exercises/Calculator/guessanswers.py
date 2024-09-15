questions_txt=open('questions.txt','r')
questions_txt_split= [line.strip() for line in questions_txt.readlines()]
questions_txt.close()
print(questions_txt_split)

result_count=0
total=len(questions_txt_split)
for splits in questions_txt_split:
    question=(splits.split("="))[0]
    print(f'Guess the answer for {question}=')
    user_input=int(input("Please enter the answer:"))
    print(user_input)
    answer = int((splits.split("="))[1])
    print(answer)
    if user_input == answer:
        result_count=result_count+1
        print('You guessed it correctly')
    else:
        print('Wrong, Please try again')
print(f'result_count is {result_count}')

result_file = open('result.txt','w')
result_file_write = result_file.write(f'Your final score is {result_count}/{total}')