import random
puak_trav= ['Romans', 'Galia', 'Vikings']
roma = ['Imperian', 'Equites Cesaeris']
roma_attack = [80, 125]
roma_defend = [70, 85]
roma_agility = [30, 40]

galia = ['Swordman', 'Theutaes Thunder']
galia_attack = [65, 95]
galia_defend = [75, 85]
galia_agility = [40, 60]

vikings = ['Clubswinger', 'Teutonic Knight']
viking_attack = [75, 100]
viking_defend = [75, 100]
viking_agility = [35, 55]

print('Ketik Mulai_game() untuk mulai permainan')
#Login
def Mulai_game() :
    id_1 = input('Create New Username:')
    password_1 = input('Create New Password:')
    print('\n NEW ACCOUNT CREATED')
    id_2 = input('\nLogin to Your Acoount:')
    password_2 = input('Your Password?:')
#pilih puak
    if id_2 == id_1 and password_2 == password_1 :
        print('status_login = active')
        print('\nWelcome back, ' + id_1,'!')
        print('Choose your Puak! : ')
        print('\nRomans', 'Galia', 'Vikings')
        choose_puak = input()
        if choose_puak == puak_trav[0] :
            print('Imperians')
            print('Attack : 80, Defend : 70, Agility : 30')
            print('Equites Cesaeris')
            print('Attack : 125, Defend : 85, Agility : 40')
            banyak_army_1 = input('How many Imperians? :')
            banyak_army_2 = input('How many Equites Cesaeris? :')
            if int(banyak_army_1) > 100 or int(banyak_army_2) > 100 :
                print('Too much soldier you can deploy!')
                return Mulai_game()
            else :
                total_attack = banyak_army_1 * (roma_attack[0] + (0.75 * roma_agility[0])) +  banyak_army_2 * (roma_attack[1] + (0.75 * roma_agility[1]))
                print(total_attack)
                print('Enemy choosing puak...')
                choose_enemy = random.choice(puak_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == puak_trav[0] :
                    print('Imperians')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Imperians : ', banyak_enemy_1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy_2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Romans')
                            print('TROOPS')
                            print('Imperian : ', banyak_army_1)
                            print('Equites Cecaris : ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy_2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', banyak_army_1)
                            print('Theutaes Thunder: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                else :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy_2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_army_1)
                            print('Teutonic Knight: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()

        elif choose_puak == puak_trav[1] :
            print('Swordman')
            print('Attack : 65, Defend : 75, Agility : 40')
            print('Theutaes Thunder')
            print('Attack : 95, Defend : 85, Agility : 60')
            banyak_army_1 = input('How many Swordman? :')
            banyak_army_2 = input('How many Theutaes Thunder? :')
            if int(banyak_army_1) > 100 or int(banyak_army_2) > 100 :
                print('Too much soldier you can deploy!')
                return Mulai_game()
            else :
                total_attack = banyak_army_1 * (galia_attack[0] + (0.75 * galia_agility[0])) +  banyak_army_2 * (galia_attack[1] + (0.75 * galia_agility[1]))
                print(total_attack)
                print('Enemy choosing puak...')
                choose_enemy = random.choice(puak_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == puak_trav[0] :
                    print('Imperians')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Imperians : ', banyak_enemy_1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy_2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', banyak_army_1)
                            print('Theutaes Thunder : ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy_2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', banyak_army_1)
                            print('Theutaes Thunder: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy_2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', banyak_army_1)
                            print('Theutaes Thunder: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
        
        else : 
            print('Clubswinger')
            print('Attack : 75, Defend : 75, Agility : 35')
            print('Teutonic Knight')
            print('Attack : 100, Defend : 100, Agility : 55')
            banyak_army_1 = input('How many Clubswinger? :')
            banyak_army_2 = input('How many Teutonic Knight? :')
            if int(banyak_army_1) > 100 or int(banyak_army_2) > 100 :
                print('Too much soldier you can deploy!')
                return Mulai_game()
            else :
                total_attack = banyak_army_1 * (viking_attack[0] + (0.75 * viking_agility[0])) +  banyak_army_2 * (viking_attack[1] + (0.75 * viking_agility[1]))
                print(total_attack)
                print('Enemy choosing puak...')
                choose_enemy = random.choice(puak_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == puak_trav[0] :
                    print('Imperians')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Imperians : ', banyak_enemy_1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy_2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_army_1)
                            print('Teutonic Knight : ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy_2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_army_1)
                            print('Teutonic Knight: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = banyak_enemy_1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy_2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('CONGRATULATIONS')
                            print('Username :', id_1)
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_army_1)
                            print('Teutonic Knight: ', banyak_army_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('DEFEAT')
                            return Mulai_game()        
    else : 
        print('Login Failed, Please Check Your Id or Password!')

#CONTOH HASIL OUTPUT DARI RUN CODE :

#Create New Username: Fris
#Create New Password: GibranFA
# NEW ACCOUNT CREATED
#Login to Your Acoount: Fris
#Your Password?: GibranFA
#status_login = active

#Welcome back, Fris !
#Choose your Puak! : 

#Romans Galia Vikings
# Vikings
#Clubswinger
#Attack : 75, Defend : 75, Agility : 35
#Teutonic Knight
#Attack : 100, Defend : 100, Agility : 55
#How many Clubswinger? : 80
#How many Teutonic Knight? : 7
#9088.75
#Enemy choosing puak...
#Enemy has chosen Romans
#Imperians
#Attack : 80, Defend : 70, Agility : 30
#Equites Cesaeris
#Attack : 125, Defend : 85, Agility : 40
#Enemy Imperians :  16
#Enemy Equites Cesaeris :  43
#Enemy total defend :  6425.0
#To attack type SERANG
# SERANG
#CONGRATULATIONS
#Username : Fris
#Puak : Vikings
#TROOPS
#Clubswinger :  80
#Teutonic Knight :  7
#Total attack :  9088.75
#Total defend :  6425.0
#Total kemenangan :  1