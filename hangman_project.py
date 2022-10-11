# Write your code here
import  random
won_games = 0
lost_games = 0

print("H A N G M A N")

while True:
    
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    
    start = input()
    
    if start == 'play':

        list_words = ['python', 'java', 'swift', 'javascript']
        word = random.choice(list_words)
        attempt = 8
        disp = list('-'*(len(word)))
        already_guessed = []
        win = False
        
        
        
        while attempt > 0:
            
            print()
            print("".join(disp))
            
            if (disp) == list(word):
                win = True
                break
            
            guess = input("Input a letter:")
        
            if (len(guess)!=1):  #input is not a single letter, ask again
                print("Please, input a single letter.")
                continue
                
            if (not(guess.isalpha()) or not(guess.islower())):  #input is not a lowercase letter of the alphabet, ask again
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
        
            if guess in already_guessed:  #input letter already guessed
                print("You've already guessed this letter.")
                continue

            already_guessed.append(guess)
        
            if guess in word:
                    for index, element in enumerate(word):
                        if element == guess:
                            disp[index] = element
            else:
                print("That letter doesn't appear in the word.")
                attempt -=1
          
        if win:
            print(f"""You guessed the word {word}!
            You survived!""")
            won_games += 1
        else:
            print("You lost!")
            lost_games +=1

        continue
    
    elif start == 'results':
        print(f"""
        You won: {won_games} times.
        You lost: {lost_games} times.""")
        
    elif start == 'exit':
        break
