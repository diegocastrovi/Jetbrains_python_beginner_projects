import random

#global vars
name_1 = 'John'
name_2 = 'Jack'
user = ''
bot = ''
current_turn = ''
next_turn = ''


#initialize
current_turn = ''
next_turn = ''
#function to switch names
def switch_names():
    global current_turn, next_turn
    temp = current_turn
    current_turn = next_turn
    next_turn = temp

print("How many pencils would you like to use:")

#loop to enter right initial value of pencils
while True:
    temp = input()
    if temp.isnumeric():
        pencils = int(temp)
        if pencils != 0:
            break
        else:
            print("The number of pencils should be positive")
            continue
    else:
        print("The number of pencils should be numeric")
        continue
print("Who will be the first (John, Jack):")

#loop to choose correct names
while True:
    current_turn = input()
    if current_turn in (name_1, name_2):
        if current_turn == name_1:
            next_turn = name_2
        else:
            next_turn = name_1
            
        print("|" * pencils)
        break
        
    else:
        print(f"Choose between {name_1} and {name_2}")
        continue
        
user = 'John'
bot = 'Jack'

print(f"{current_turn}'s' turn:")
#principal loop
while True:
    #if current_user == user:
        #play_user()
    #else:
        #play_bot()
    if current_turn == user:
        ###
        temp = input()
        if temp in ('1','2','3'):
            remove_pencil = int(temp)
            if remove_pencil <= pencils:   #Verify that number of pencils is less than the current number of pencils
                pencils -= remove_pencil
                if (pencils > 0):
                    print("|" * pencils)
                else:
                    switch_names()
                    print(f"{current_turn}'s' won!")
                    break
                switch_names()    
                print(f"{current_turn}'s' turn:")
            else:
                print("Too many pencils were taken")
                continue
        else:
            print("Possible values: '1', '2' or '3'")
            continue
        ###
    else:
        if pencils <= 1:
            remove_pencil = pencils
            pencils -= remove_pencil
            print(remove_pencil)
            switch_names()
            print(f"{current_turn}'s' won!")
            break
        elif pencils % 4 == 1:  #losing position
            remove_pencil = random.choice([1,2,3])
        else: #winning position
            remove_pencil = (pencils - 1) % 4
        pencils -= remove_pencil
        print(remove_pencil)
        print("|" * pencils)
        switch_names()
        print(f"{current_turn}'s' turn:")
    
    