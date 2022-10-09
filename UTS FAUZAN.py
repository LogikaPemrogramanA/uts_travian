import random
clan_trav= ['Roma', 'Galia', 'Viking']
roma = ['Imperian', 'Equites Cesaeris']
roma_attack = [80, 125]
roma_defend = [70, 85]
roma_agility = [30, 40]

galia = ['Swordsman', 'Theutaes Thunder']
galia_attack = [65, 95]
galia_defend = [75, 85]
galia_agility = [40, 60]

Viking = ['Clubswinger', 'Teutonic Knight']
viking_attack = [75, 100]
viking_defend = [75, 100]
viking_agility = [35, 55]

print('Ketik log_in() untuk mulai permainan')
#Login
def log_in() :
    id1 = input('Create New Username:')
    password1 = input('Create New Password:')
    print('\n YOUR ACCOUNT HAS BEEN CREATED')
    id2 = input('\nLogin to Your Acoount:')
    password2 = input('Your Password?:')
#pilih puak untuk dimainkan
#puak adalah Clan
#Pada perogram ini, saya memutuskan untuk mengganti kata puak dengan clan agar lebih familiar dan mudah untuk dimengerti oleh para pemain
    if id2 == id1 and password2 == password1 :
        print('status_login = active')
        print('\nWelcome back, ' + id1,'!')
        print('Choose your Clan! : ')
        print('\nRoma', 'Galia', 'Viking')
        
        choose_clan = input()
        if choose_clan == clan_trav[0] :
            print('Imperian')
            print('Attack : 80, Defend : 70, Agility : 30')
            print('Equites Cesaeris')
            print('Attack : 125, Defend : 85, Agility : 40')
            banyak_tentara1 = input('How many Imperian? :')
            banyak_tentara2 = input('How many Equites Cesaeris? :')
            if int(banyak_tentara1) > 100 or int(banyak_tentara2) > 100 :
                print('The Number of Your Soldiers Exceeds The Limit!!')
                return log_in()
            else :
                total_attack = banyak_tentara1 * (roma_attack[0] + (0.75 * roma_agility[0])) +  banyak_tentara2 * (roma_attack[1] + (0.75 * roma_agility[1]))
                print('Your Total Attack : ', total_attack)
                print('Enemy is Choosing Clan...')
                choose_enemy = random.choice(clan_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == clan_trav[0] :
                    print('Imperian')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Imperian : ', banyak_enemy1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War!')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('Clan : Roma')
                            print('TROOPS')
                            print('Imperian : ', banyak_tentara1)
                            print('Equites Cecaris : ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                elif choose_enemy == clan_trav[1] :
                    print('Swordsman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Swordsman : ', banyak_enemy1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War!')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('Clan : Galia')
                            print('TROOPS')
                            print('Swordsman : ', banyak_tentara1)
                            print('Theutaes Thunder: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defense : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                else :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy1)
                    print('Enemy Teutonic Knight : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War!')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('Clan : Viking')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_tentara1)
                            print('Teutonic Knight: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()

        elif choose_clan == clan_trav[1] :
            print('Swordsman')
            print('Attack : 65, Defend : 75, Agility : 40')
            print('Theutaes Thunder')
            print('Attack : 95, Defend : 85, Agility : 60')
            banyak_tentara1 = input('How many Swordsman? :')
            banyak_tentara2 = input('How many Theutaes Thunder? :')
            if int(banyak_tentara1) > 100 or int(banyak_tentara2) > 100 :
                print('The Number of Your Soldiers Exceeds The Limit!')
                return log_in()
            else :
                total_attack = banyak_tentara1 * (galia_attack[0] + (0.75 * galia_agility[0])) +  banyak_tentara2 * (galia_attack[1] + (0.75 * galia_agility[1]))
                print('Your Total Attack : ', total_attack)
                print('Enemy is Choosing Clan...')
                choose_enemy = random.choice(clan_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == clan_trav[0] :
                    print('Imperian')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Imperian : ', banyak_enemy_1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy2)
                    total_defense = banyak_enemy_1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Galia')
                            print('TROOPS')
                            print('Swordsman : ', banyak_tentara1)
                            print('Theutaes Thunder : ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                elif choose_enemy == clan_trav[1] :
                    print('Swordsman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordsman : ', banyak_enemy1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy2)
                    total_defense = banyak_enemy_1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy_2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Galia')
                            print('TROOPS')
                            print('Swordsman : ', banyak_tentara1)
                            print('Theutaes Thunder: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy1)
                    print('Enemy Teutonic Knight : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Galia')
                            print('TROOPS')
                            print('Swordsman : ', banyak_tentara1)
                            print('Theutaes Thunder: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()

        else : 
            print('Clubswinger')
            print('Attack : 75, Defend : 75, Agility : 35')
            print('Teutonic Knight')
            print('Attack : 100, Defend : 100, Agility : 55')
            banyak_tentara1 = input('How many Clubswinger? :')
            banyak_tentara2 = input('How many Teutonic Knight? :')
            if int(banyak_tentara1) > 100 or int(banyak_tentara2) > 100 :
                print('The Number of Your Soldiers Exceeds The Limit!')
                return log_in()
            else :
                total_attack = banyak_tentara1 * (viking_attack[0] + (0.75 * viking_agility[0])) +  banyak_tentara2 * (viking_attack[1] + (0.75 * viking_agility[1]))
                print('Your Total Attack : ', total_attack)
                print('Enemy is Choosing Clan...')
                choose_enemy = random.choice(clan_trav)
                print('Enemy has chosen' , choose_enemy)
                if choose_enemy == clan_trav[0] :
                    print('Imperian')
                    print('Attack : 80, Defend : 70, Agility : 30')
                    print('Equites Cesaeris')
                    print('Attack : 125, Defend : 85, Agility : 40')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Imperian : ', banyak_enemy1)
                    print('Enemy Equites Cesaeris : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (roma_defend[0] + (0.75 * roma_agility[0])) +  banyak_enemy2 * (roma_defend[1] + (0.75 * roma_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Viking')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_tentara1)
                            print('Teutonic Knight : ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                elif choose_enemy == clan_trav[1] :
                    print('Swordsman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Swordsman : ', banyak_enemy1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy2)
                    total_defense = banyak_enemy_1 * (galia_defend[0] + (0.75 * galia_agility[0])) +  banyak_enemy2 * (galia_defend[1] + (0.75 * galia_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Viking')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_tentara1)
                            print('Teutonic Knight: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy1 = random.randrange(1, 100)
                    banyak_enemy2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy1)
                    print('Enemy Teutonic Knight : ', banyak_enemy2)
                    total_defense = banyak_enemy1 * (viking_defend[0] + (0.75 * viking_agility[0])) +  banyak_enemy2 * (viking_defend[1] + (0.75 * viking_agility[1]))
                    print('Enemy Total Defense : ', total_defense)
                    print('Type ATTACK To Start The War')
                    Attack = input()
                    if Attack == 'ATTACK' :
                        pemenang = total_attack - total_defense
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Username :', id1)
                            print('clan : Viking')
                            print('TROOPS')
                            print('Clubswinger : ', banyak_tentara1)
                            print('Teutonic Knight: ', banyak_tentara2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defense)
                            print('Total kemenangan : ', round(total_attack/total_defense), 'Ronde')
                        else :
                            print('YOU LOSE!')
                            return log_in()        
    else : 
        print('Failed To Hack Your Friends Account?')
        print('Please Insert The Right Username and Password!')

#CONTOH HASIL OUTPUT DARI RUN CODE :

#Create New Username: pawjann
#Create New Password: kungkingkangkungking
# YOUR ACCOUNT HAS BEEN CREATED
#Login to Your Acoount: pawjann
#Your Password?: kungkingkangkungking
#status_login = active

#Welcome back, pawjann !
#Choose your clan! : 

#Roma Galia Viking
#Galia
#Swordsman
#Attack : 65, Defend : 75, Agility : 40
#Theutaes Thunder
#Attack : 95, Defend : 85, Agility : 60
#How many Swordsman? : 100
#How many Teutonic Knight? : 100
#Your Total Attack : 23500.0
#Enemy is Choosing Clan...
#Enemy has chosen Roma
#Imperian
#Attack : 80, Defend : 70, Agility : 30
#Equites Cesaeris
#Attack : 125, Defend : 85, Agility : 40
#Enemy Imperian :  20
#Enemy Equites Cesaeris :  35
#Enemy Total Defense : 5875.0
#Type ATTACK To Start The War
#Attack
#YOU WIN!
#Username : pawjann
#clan : Galia
#TROOPS
#Swordsman : 100
#Theutaes Thunder : 100
#Total attack : 23500.0
#Total defend : 5875.0
#Total kemenangan : 4 Ronde