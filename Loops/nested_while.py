print('welcome')
restart = ('Y')
chances = 3
balance =67.14
while chances>=0:
    pin = int(input('Please enter 4 digit pin'))
    if(pin == 1234):
        print('pin validated')
        while restart not in ('n','N',"No",'no','NO'):
            print('press ')
            print('1 : check balance')
            print('2 : check withdrawl')
            print('3 : return')
            option = int(input('your choice'))
            if option == 1:
                print('balance:',balance,'\n')
                restart = input('press y if you want to go back. ELse N')
                if restart in ('n','N',"No",'no','NO'):
                    print('Tq')
            elif option == 2:
                print('enter the amount u want to withdraw')
                am = int(input())
                if balance>= am:
                    remBal = balance - am
                    print('balance:', remBal, '\n')
                    restart = input('press y if you want to go back. ELse N')
                    if restart in ('n', 'N', "No", 'no', 'NO'):
                        print('Tq')
                else:
                    print('no sufficient bal')
                    restart = input('press y if you want to go back. ELse N')
                    if restart in ('n', 'N', "No", 'no', 'NO'):
                        print('Tq')
            elif option == 3:
                print('please collect ur card')
                print('thanku for using our services')
                break
            else:
                print('please enter correct choice')
                restart = 'y'
    elif pin != ('1234'):
        print('Incorrect pin')
        chances = chances -1
        if chances == 0:
            print('no more tries')
            break

