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




    
     
        
        

            
       

            

          
        
    
