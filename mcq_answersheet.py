print("Welcome to MCQ answersheet generator!")
print("Please input a, b, c or d as the answer of a given mcq question")
mcq_limit = int(input("How many mcq question you are going to answer? : "))
a = True
mcq_number = 1
mcq_quantity = 0
mcq_answers = []
mcq_answersheet = []
mcq_answersheet_number = 1

while a == True:
    mcq_answer = input(f"{mcq_number}. ")
    if mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd':
        print("Please enter a valid answer!")
        continue
    mcq_answers.append(f"{mcq_number}.{mcq_answer}")
    mcq_answersheet.append(mcq_answer)
    mcq_quantity = mcq_quantity+1
    mcq_number = mcq_number+1
    if mcq_limit == mcq_quantity:
        a = False
print("=== Your answers are below! ===")
print(">>> Press 1 to get your answers in a list")
print(">>> Press 2 to get your answers in a string")
print(">>> Press 3 to get your answers in mcq answersheet style")
print(">>> Type 'exit' to exit")
print(">>> Type 'help' to get other functions")
while a == False:
    b = input("> ")
    if b == 'help':
        print("")
    elif b == 'exit':
        break
    elif b == '1':
        for c in mcq_answers:
            print(c)
    elif b == '2':
        print(mcq_answers)
    elif b == '3':
        for c in mcq_answersheet:
            if c == 'a':
                print(f"{mcq_answersheet_number}. ⬤ Ⓑ Ⓒ Ⓓ")
            elif c == 'b':
                print(f"{mcq_answersheet_number}. Ⓐ ⬤ Ⓒ Ⓓ")
            elif c == 'c':
                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ ⬤ Ⓓ")
            else:
                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ ⬤")
            mcq_answersheet_number = mcq_answersheet_number + 1
    else : 
        print("Please enter a valid input")
