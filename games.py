def roulette_simple():
    import random
    money = input ('How much money do you have? ')
    while money.isdigit() == False:
        print('Give me numbers.')
        money = input ('How much money do you have? ')
    else:
        money = float(money)
    while money > 0 :
        bet = input ('How much do you want to bet? ')
        while bet.isdigit() == False:
            print('Give me numbers.')
            bet = input ('How much do you want to bet? ')
        else:
            bet = float(bet)
        bet = min (bet, money)
        if bet <= 0:
            print('There is no bet, I\'m sorry.')
            break
        print (f'Betting {bet}')
        guess = input('Guess a number between 0 and 36: ')
        while guess.isdigit() == False:
            print('Give me numbers.')
            guess = input('Guess a number between 0 and 36: ')
        else:
            guess = float(guess)
        while guess < 0 or guess > 36:
            print ('Give a number between 0 and 36')
            guess = input('Guess a number between 0 and 36: ')
            while guess.isdigit() == False:
                print('Give me (integer) numbers.')
                guess = input('Guess a number between 0 and 36: ')
            else:
                guess = float(guess)
        winning_bet = random.randint(0, 36)
        print(winning_bet)
        if guess == winning_bet:
            print('***YOU WON!!***')
            money += bet
        else:
            print ('You lost.')
            money -= bet
        ask = input ('Do you want to play roulette again? (Yes or No): ')
        if (ask.strip(' ')).lower()== 'no':
            maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower()
            while maybe.isalpha() == False:
                print('Yes or No, please.')
                maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower() 
            else:
                if maybe == 'no':
                    print('Bye')
                    break
                elif maybe== 'yes':
                    main()
        else:
            roulette_simple()
    else:
        print('You are out of money, you can\'t gamble.')




def slot():
    import random
    money = input ('How much money do you have? ')
    while money.isdigit() == False:
        print('Give me numbers.')
        money = input ('How much money do you have? ')
    else:
        money = float(money)
    while money > 0 :
        bet = input ('How much do you want to bet? ')
        while bet.isdigit() == False:
            print('Give me numbers.')
            bet = input ('How much do you want to bet? ')
        else:
            bet = float(bet)
        bet = min (bet, money)
        if bet <= 0:
            print('There is no bet, I\'m sorry.')
            break
        print (f'Betting {bet}')
        print ('*STARTED SPINNING!!*')
        tuple1 = ( '♥' , '☻' , '♣' , '♠')
        a = random.choice(tuple1)
        b = random.choice(tuple1)
        c = random.choice(tuple1)
        d = random.choice(tuple1)
        print (a, b, c, d, sep='\t')
        if a==b==c==d:
            print('***YOU WON!!***')
            money += bet
        else:
            print('You lost')
            money -= bet
        ask = input ('Do you want to play slot again? (Yes or No): ')
        if (ask.strip(' ')).lower()== 'no':
            maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower()
            while maybe.isalpha() == False:
                print('Yes or No, please.')
                maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower() 
            else:
                if maybe == 'no':
                   print('Bye')
                   break
                elif maybe== 'yes':
                    main()
        else:
            slot()
    else:
        print('You are out of money, you can\'t gamble.')



def hangman():
    import random
    ins = []
    not_ins = []
    tuple1 = ('εγχειριδιο', 'δικλειδα', 'πυγμαιος', 'ενδελεχης', 'ειρμος', 'απινιδωτης')
    hidden_word = random.choice(tuple1)
    z = len(hidden_word)
    print (f'You have {z+4} tries to guess the word. Are you ready?')
    print ('_ '*z) 
    for i in range(z+4):
        k = ''
        u = input ('Give me a letter: ')
        while u.isalpha() == False:
            print('Only letters, please.')
            u = input ('Give me a letter: ')
        else:
            u = u.lower()
        if u in hidden_word:
            ins.append(u)
            print('You found one of the letters')
        else:
            print ('This letter is not in the hidden word')
            not_ins.append(u)            
            print ('Here is a list of the letters that you have guessed wrong', not_ins)  
        for letter in hidden_word:
            if letter in ins:
                k+=letter
            else:
                k+='_ '
        print(k)
        if hidden_word == k:
                print('You found the word!')
                break
    if not hidden_word == k:
         print(f'You lost. The hidden word was {hidden_word}.')
    ask = input ('Do you want to play hangman again? (Yes or No): ')
    if (ask.strip(' ')).lower()== 'no':
        maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower()
        while maybe.isalpha() == False:
            print('Yes or No, please.')
            maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower() 
        else:
            if maybe == 'no':
               print('Bye')
            elif maybe== 'yes':
                main()
    else:
        hangman()
        
          

def tic_tac_toe():
    L = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print ('Hello. This game needs two players.')
    print ('The game starts now!')
    player = 'O' 
    for i in range(9):   
        print("   |--------|")
        print("2  | " + L[2][0] + "| " + L[2][1] + "| " + L[2][2] + "|")
        print("   |--------|")
        print("1  | " + L [1][0] + "| " + L[1][1] + "| " + L[1][2] + "|")
        print("   |--------|")
        print("0  | " + L[0][0] + "| " + L[0][1] + "| " + L[0][2] + "|")
        print("   |--------|")
        print("     0  1  2")
        if player == 'O':
            player = 'X'
        else:
            player = 'O'
        while True:
            print("Player " + player + "\'s turn! ")
            r = input ('Give number of the row you want to place your symbol(0,1 or 2): ')
            while r.isdigit() == False:
                print("Give 0, 1 or 2, please.")
                r = input ('Give number of the row you want to place your symbol(0,1 or 2): ')
            else:
                 r = int(r)
            c = input('Give number of the column you want to place your symbol(0,1 or 2): ')
            while c.isdigit() == False:
                print("Give 0, 1 or 2, please.")
                c = input('Give number of the column you want to place your symbol(0,1 or 2): ')
            else:
                 c = int(c)
            if r < 0 or r > 2:
                print("Give 0, 1 or 2, please.")
                continue
            elif c < 0 or c > 2:
                print("Give 0, 1, 2, please.")
                continue
            elif L[r][c]!=" ":
                print("Pick an empty box, please.")
                continue
            else:
                L[r][c]=player
                break
        winner = False
        for i in range(3):
            if (L[i][0]== L[i][1]== L[i][2]) and (L[i][0] != " "):
                winner = player
        for j in range(3):
            if (L[0][j]== L[1][j]== L[2][j]) and (L[0][j] != " "):
                winner = player
        if ((L[0][0] == L[1][1] == L[2][2]) and L[0][0] != " ") or ((L[2][0] == L[1][1] == L[0][2]) and L[2][0] != " "):
            winner = player
        if winner:
            print("   |--------|")
            print("2  | " + L[2][0] + "| " + L[2][1] + "| " + L[2][2] + "|")
            print("   |--------|")
            print("1  | " + L [1][0] + "| " + L[1][1] + "| " + L[1][2] + "|")
            print("   |--------|")
            print("0  | " + L[0][0] + "| " + L[0][1] + "| " + L[0][2] + "|")
            print("   |--------|")
            print("     0  1  2")
            print("Player " + player + " won! ")
            break
    if not winner:
        print("   |--------|")
        print("2  | " + L[2][0] + "| " + L[2][1] + "| " + L[2][2] + "|")
        print("   |--------|")
        print("1  | " + L [1][0] + "| " + L[1][1] + "| " + L[1][2] + "|")
        print("   |--------|")
        print("0  | " + L[0][0] + "| " + L[0][1] + "| " + L[0][2] + "|")
        print("   |--------|")
        print("     0  1  2")
        print("It\'s a tie!")
    ask = input ('Do you want to play tictactoe again? (Yes or No): ')
    if (ask.strip(' ')).lower()== 'no':
        maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower()
        while maybe.isalpha() == False:
            print('Yes or No, please.')
            maybe = ((input ('Maybe you want to play another game? ')).strip(' ')).lower() 
        else:
            if maybe == 'no':
               print('Bye')
            elif maybe== 'yes':
                main()
    else:
        tic_tac_toe()
 
 

def main():
    x = input ('Hello! Do you want to play games for kids or adults? ')
    a = (x.strip(' ')).lower() 
    if a.isalpha():
        if a == 'kids':
            y = input ('Do you want to play tictactoe or hangman? ')
            b = (y.strip(' ')).lower()
            if b.isalpha():
                if b == 'tictactoe':
                    tic_tac_toe()
                elif b == 'hangman':
                     hangman()
                else:
                    print ('Choose one of the options, please.')
            else:
                print ('Choose one of the options, please.')
        elif a == 'adults':
            y = input ('Do you want to play (simplified) roulette or slot? ')
            b = (y.strip(' ')).lower()
            if b.isalpha():
                if b == 'roulette':
                    roulette_simple()
                elif b == 'slot':
                    slot()
                else:
                    print ('Choose one of the options, please.')
            else:
                print ('Choose one of the options, please.')
        else:
            print ('Choose one of the options, please.')
    else:
         print ('Choose one of the options, please.')
    
    
