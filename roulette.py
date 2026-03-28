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
                print('Give me numbers.')
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
