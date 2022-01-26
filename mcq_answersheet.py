print("Welcome to MCQ answersheet generator!")
print("Please input a, b, c or d as the answer of a given mcq question")
mcq_limit = int(input("How many mcq question you are going to answer? : "))
a = True
mcq_number = 1
mcq_quantity = 0
mcq_answers = []

while a == True:
    mcq_answer = input(f"{mcq_number}. ")
    if mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd':
        print("Please enter a valid answer!")
        continue
    mcq_answers.append(f"{mcq_number}.{mcq_answer}")
    mcq_quantity = mcq_quantity+1
    mcq_number = mcq_number+1
    if mcq_limit == mcq_quantity:
        a = False
print("=== Your answers are below! ===")
for b in mcq_answers:
    print(b)
