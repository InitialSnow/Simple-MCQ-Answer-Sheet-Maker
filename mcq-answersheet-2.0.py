print("==================================================")
print("||         MCQ ANSWER SHEET GENERATOR           ||")
print("==================================================")
print("")
print("Type a command. Input 'help' to get a list of available commands")

a1 = True
a2 = True
a3 = True
a4 = True
mcq_mode = 0
mcq_number = 1
mcq_answersheet_number = 1
mcq_answers = []
mcq_answersheet = []

while a1 == True:
    inp = input("> ")
    if inp == "help":
        print('"start"    : initiates the process of generating mcq answer sheet')
        print('"exit"     : exits the program')
    elif inp == "start":
        print("Please configure your mcq answer sheet")
        print("=====================================================")
        print("||    How many questions you are going to answer?  ||")
        print("=====================================================")
        while a4 == True:
            inp2_not_checked = input("> ")
            try:
                inp2 = int(inp2_not_checked)
                break
            except ValueError:
                print("Please give a valid input!")
                continue
        print("=====================================")
        print("||  How many options do you want?  ||")
        print("||   [a] 4          [b] 5          ||")
        print("=====================================")
        while a2 == True :
            inp3 = input("> ")
            if inp3 == "a" or inp3 == "[a]" or inp3 == "4":
                mcq_mode = 4
                break
            elif inp3 == "b" or inp3 == "[b]" or inp3 == "5":
                mcq_mode = 5
                break
            else : 
                print("Please give a valid input")
                continue
        if mcq_mode == 4:
            while mcq_number <= inp2:
                print("-----------------")
                mcq_answer = input(f"{mcq_number} ==> ")
                if mcq_answer == 'skip':
                    print("This question has been skipped!")
                    mcq_answersheet.append(mcq_answer)
                    mcq_answers.append(f"{mcq_number}. [skipped]")
                    mcq_number = mcq_number+1
                    continue
                elif mcq_answer == 'correct':
                    mcq_answersheet.pop()
                    mcq_answers.pop()
                    mcq_number = mcq_number-1
                    continue
                elif mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd' and mcq_answer != '!a' and mcq_answer != '!b' and mcq_answer != '!c' and mcq_answer != '!d' and mcq_answer != '!e':
                    print("Please enter a valid answer!")
                    continue
                mcq_answersheet.append(mcq_answer)
                mcq_answers.append(f"{mcq_number}. {mcq_answer}")
                mcq_number = mcq_number+1
            print("==================================================")
            print("||         Your answers have been recorded!     ||")
            print("==================================================")
            print(">>> Press 1 to get your answers in a mcq answer sheet")
            print(">>> Press 2 to get your answers in a list")
            print(">>> Press 3 to answer skipped questions")
            print(">>> Press 4 to exit answer mode")
            while a3 == True:
                inp4 = input(">> ")
                if inp4 == "1":
                    mcq_answersheet_number = 1
                    for c in mcq_answersheet:
                        if c == 'a':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   ⬤ Ⓑ Ⓒ Ⓓ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  ⬤ Ⓑ Ⓒ Ⓓ")
                            else:
                                print(f"{mcq_answersheet_number}. ⬤ Ⓑ Ⓒ Ⓓ")
                        elif c == 'b':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ ⬤ Ⓒ Ⓓ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ ⬤ Ⓒ Ⓓ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ ⬤ Ⓒ Ⓓ")
                        elif c == 'c':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ ⬤ Ⓓ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ ⬤ Ⓓ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ ⬤ Ⓓ")
                        elif c == 'd':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ Ⓒ ⬤")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ Ⓒ ⬤")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ ⬤")
                        elif c == '!a':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                        elif c == '!b':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                        elif c == '!c':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                        elif c == '!d':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                        elif c=='!e':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                        else:
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   [skipped]")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  [skipped]")
                            else:
                                print(f"{mcq_answersheet_number}. [skipped]")
                        mcq_answersheet_number = mcq_answersheet_number + 1
                elif inp4 == '2':
                    for d in mcq_answers:
                        print(d)
                elif inp4 == '3':
                    mcq_number000 = 0
                    for z in mcq_answersheet:
                        mcq_number000 = mcq_number000+1
                        if z == "skip":
                            mcq_answer = input(f"{mcq_number000}. ")
                            if mcq_answer == 'skip':
                                print("This question has been skipped!")
                                mcq_answers[mcq_number000-1] = f"{mcq_number000}. skipped"
                                mcq_answersheet[mcq_number000-1] = mcq_answer
                                continue
                            elif mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd':
                                print("Please enter a valid answer!")
                                continue
                            mcq_answers[mcq_number000-1] = f"{mcq_number000}. {mcq_answer}"
                            mcq_answersheet[mcq_number000-1] = mcq_answer
                elif inp4 == '4':
                    break

        elif mcq_mode == 5:
            while mcq_number <= inp2:
                print("-----------------")
                mcq_answer = input(f"{mcq_number} ==> ")
                if mcq_answer == 'skip':
                    print("This question has been skipped!")
                    mcq_answersheet.append(mcq_answer)
                    mcq_answers.append(f"{mcq_number}. [skipped]")
                    mcq_number = mcq_number+1
                    continue
                elif mcq_answer == 'correct':
                    mcq_answersheet.pop()
                    mcq_answers.pop()
                    mcq_number = mcq_number-1
                    continue
                elif mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd' and mcq_answer != 'e':
                    print("Please enter a valid answer!")
                    continue
                mcq_answersheet.append(mcq_answer)
                mcq_answers.append(f"{mcq_number}. {mcq_answer}")
                mcq_number = mcq_number+1
            print("==================================================")
            print("||         Your answers have been recorded!     ||")
            print("==================================================")
            print(">>> Press 1 to get your answers in a mcq answer sheet")
            print(">>> Press 2 to get your answers in a list")
            print(">>> Press 3 to answer skipped questions")
            print(">>> Press 4 to exit answer mode")
            while a3 == True:
                inp4 = input(">> ")
                if inp4 == "1":
                    mcq_answersheet_number = 1
                    for c in mcq_answersheet:
                        if c == 'a':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. ⬤ Ⓑ Ⓒ Ⓓ Ⓔ")
                        elif c == 'b':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ ⬤ Ⓒ Ⓓ Ⓔ")
                        elif c == 'c':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ ⬤ Ⓓ Ⓔ")
                        elif c == 'd':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ ⬤ Ⓔ")
                        elif c == 'e':
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                            else:
                                print(f"{mcq_answersheet_number}. Ⓐ Ⓑ Ⓒ Ⓓ ⬤")
                        else:
                            if mcq_answersheet_number < 10:
                                print(f"{mcq_answersheet_number}.   [skipped]")
                            elif mcq_answersheet_number < 100:
                                print(f"{mcq_answersheet_number}.  [skipped]")
                            else:
                                print(f"{mcq_answersheet_number}. [skipped]")
                        mcq_answersheet_number = mcq_answersheet_number + 1
                elif inp4 == '2':
                    for d in mcq_answers:
                        print(d)
                elif inp4 == '3':
                    mcq_number000 = 0
                    for z in mcq_answersheet:
                        mcq_number000 = mcq_number000+1
                        if z == "skip":
                            mcq_answer = input(f"{mcq_number000}. ")
                            if mcq_answer == 'skip':
                                print("This question has been skipped!")
                                mcq_answers[mcq_number000-1] = f"{mcq_number000}. skipped"
                                mcq_answersheet[mcq_number000-1] = mcq_answer
                                continue
                            elif mcq_answer != 'a' and mcq_answer != 'b' and mcq_answer != 'c' and mcq_answer != 'd' and mcq_answer != 'e':
                                print("Please enter a valid answer!")
                                continue
                            mcq_answers[mcq_number000-1] = f"{mcq_number000}. {mcq_answer}"
                            mcq_answersheet[mcq_number000-1] = mcq_answer
                elif inp4 == '4':
                    break
        mcq_mode = 0
        mcq_number = 1
        mcq_answersheet_number = 1
        mcq_answers = []
        mcq_answersheet = []

    elif inp == "exit" :
        break
    else :
        print("Please give a valid input")
