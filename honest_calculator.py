# write your code here

# messages to show
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_last_3 = [0]*13
msg_last_3[10] = msg_10
msg_last_3[11] = msg_11
msg_last_3[12] = msg_12


operators = ['+','-','*','/']  #valid operators
memory = 0.0  #initialize memory

def is_one_digit (v):  #check if a number ha sonly one digit
    if ((v > -10) and (v < 10) and v.is_integer()):
        return True
    else:
        return False

def check(v1, v2, v3):  #check if the operations are too easy
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 ==1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg) 

while True:  #principal loop 
    print(msg_0)
    calc = input()  # firs tinput
    result = 0
    x, oper, y = calc.split()  #retrieving values for x, y and oper
    
    if x == 'M':   # verify if we are using the memory for x or y value
        x = memory
    if y == 'M':
        y = memory
    
    try:
        float(x)  #verify if x and y are valid inputs
        float(y)
    except:
        print(msg_1)  #msg if either x or y is not a number
        continue
    if oper not in operators: # verify if the operator is valid
        print(msg_2)  #msg if the input operation is not valid 
        continue  
    else:    #inputs validated
        x = float(x) #transform it into floats
        y = float(y)
        
        check(x, y, oper)  #calls a function to judge your laziness :p
        
        if oper == '+':  #perform the operation
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        else:
            try:
                result = x / y  #verify the division is not by 0
            except:
                print(msg_3)  #msg if division by 0
                continue
    
    print(result)
    
    answer = ''  #intialize answer


    #ask to store the value in the memory
    while answer not in ('y' ,'n') : #wait here until the anser is 'y' or 'n'
        print(msg_4)
        answer = input()
        
    if answer == 'y':
        if is_one_digit(result):
            msg_index = 10
            answer = ''
            while True: 
                print(msg_last_3[msg_index])
                answer = input()
                if answer != 'y' and answer != 'n':
                    continue
                elif answer == 'y':
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
                        break
                else:
                    break
        else:
            memory = result  #almacenate value in memory if desired
    
    answer = ''  #intialize answer

    #ask to continue using the calculator
    while answer not in ('y' ,'n'): #wait here until the anser is 'y' or 'n'
        print(msg_5)
        answer = input()

    if answer == 'y':
        continue  #repeat the principal loop
    else:
        break   
