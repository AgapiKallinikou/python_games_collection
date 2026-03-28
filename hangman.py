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
