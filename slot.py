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
