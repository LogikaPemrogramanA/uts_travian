import hashlib
import random
from sysconfig import get_path_names
def signup():
    user = input("Username : " )
    pwd = input("Password :")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("mamamia.txt", "w") as f:
             f.write(user + "\n")
             f.write(hash1)
        f.close()
        
    else:
        print("Password yang anda masukkan tidak sama \n")

    login()

def login():
    user = input("Username : " )
    pwd = input("password : ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("mamamia.txt", "r") as f:
        stored_user, stored_pwd = f.read().split("\n")
    f.close()
    if user == stored_user and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         print("Status login = active")
    else:
         print("Login failed! \n")
         login ()

def roma ():
     print ("imperian")
     print ("attack : 80")
     print ("defend : 70")
     print ("agility : 30")
     print ("")
     print ("equites caesaris")
     print ("attack : 125")
     print ("defend : 85")
     print ("agility :40")

def galia ():
     print ("swordman")
     print ("attack : 65")
     print ("defend : 75")
     print ("agility : 40")
     print ("")
     print ("theutaes thunder")
     print ("attack : 95")
     print ("defend : 85")
     print ("agility : 60")

def viking ():
     print ("clubswinger")
     print ("attack : 75")
     print ("defend : 75")
     print ("agility : 35")
     print ("")
     print ("teutonic knight")
     print ("attack : 100")
     print ("defend : 100")
     print ("agility : 55")
def game():
    print ("Selamat datang di gladiator war")
    print ("Silahkan pilih Klan yang anda mau")
    print ("1. Roma")
    print ("2. Galia")
    print ("3. Viking")
    clan = int(input ("silahkan ketik angka dari klan anda ingin lihat: "))
    if clan == 1 :
          roma()
    elif clan == 2 :
             galia()
    elif clan == 3 :
              viking ()
    
    print("apakah anda ingin melanjutkan permainan sebagai klan ini?")

    chs=input("iya/tidak :")
    if chs == "tidak":
        game()
    elif (chs!="iya"):
        game()
    
    print ("memasuki game")

    if clan == 1 :
            print('Imperians') #roma
            print('Attack : 80, Defend : 70, Agility : 30')
            print('Equites Cesaeris')
            print('Attack : 125, Defend : 85, Agility : 40')
            jumlah_pasukan_1 = input('How many Imperians? :')
            jumlah_pasukan_2 = input('How many Equites Cesaeris? :')
            if int(jumlah_pasukan_1) > 100 or int(jumlah_pasukan_2) > 100 :
                print('Too much soldier you can deploy!')
                return game()
            else :
                total_attack = int(jumlah_pasukan_1) * (int(roma_attack [1]) + (0.75 * int(roma_agility [1]))) +  int(jumlah_pasukan_2) * (int(roma_attack[1]) + (0.75 * int(roma_agility[1])))
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
                    total_defend = int(banyak_enemy_1) * (int(roma_defend[1]) + (0.75 * int(roma_agility[1]))) +  int (banyak_enemy_2) * (int(roma_defend[1]) + (0.75 * int(roma_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Romans')
                            print('TROOPS')
                            print('Imperian : ', jumlah_pasukan_1)
                            print('Equites Cecaris : ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(galia_defend[0]) + (0.75 * int(galia_agility[0]))) +  int(banyak_enemy_2) * (int(galia_defend[1]) + (0.75 * int(galia_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', jumlah_pasukan_1)
                            print('Theutaes Thunder: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                else :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(viking_defend[0]) + (0.75 * int(viking_agility[0]))) + int(banyak_enemy_2) * (int(viking_defend[1]) + (0.75 * int(viking_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', jumlah_pasukan_1)
                            print('Teutonic Knight: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()

    elif clan == 2 :
            print('Swordman') #galia
            print('Attack : 65, Defend : 75, Agility : 40')
            print('Theutaes Thunder')
            print('Attack : 95, Defend : 85, Agility : 60')
            jumlah_pasukan_1 = input('How many Swordman? :')
            jumlah_pasukan_2 = input('How many Theutaes Thunder? :')
            if int(jumlah_pasukan_1) > 100 or int(jumlah_pasukan_2) > 100 :
                print('Too much soldier you can deploy!')
                return game()
            else :
                total_attack = int(jumlah_pasukan_1) * (int(galia_attack[0]) + (0.75 * int(galia_agility[0]))) +  int(jumlah_pasukan_2) * (int(galia_attack[1]) + (0.75 * int(galia_agility[1])))
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
                    total_defend = int(banyak_enemy_1) * (int(roma_defend[0]) + (0.75 * int(roma_agility[0]))) +  int(banyak_enemy_2) * (int(roma_defend[1]) + (0.75 * int(roma_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', jumlah_pasukan_1)
                            print('Theutaes Thunder : ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(galia_defend[0]) + (0.75 * int(galia_agility[0]))) +  int(banyak_enemy_2) * (int(galia_defend[1]) + (0.75 * int(galia_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', jumlah_pasukan_1)
                            print('Theutaes Thunder: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(viking_defend[0]) + (0.75 * int(viking_agility[0]))) +  int(banyak_enemy_2) * (int(viking_defend[1]) + (0.75 * int(viking_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Galia')
                            print('TROOPS')
                            print('Swordman : ', jumlah_pasukan_1)
                            print('Theutaes Thunder: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                            
    elif clan == 3:
            print('Clubswinger') #viking
            print('Attack : 75, Defend : 75, Agility : 35')
            print('Teutonic Knight')
            print('Attack : 100, Defend : 100, Agility : 55')
            jumlah_pasukan_1 = input('How many Clubswinger? :')
            jumlah_pasukan_2 = input('How many Teutonic Knight? :')
            if int(jumlah_pasukan_1) > 100 or int(jumlah_pasukan_2) > 100 :
                print('Too much soldier you can deploy!')
                return game()
            else :
                total_attack = int(jumlah_pasukan_1) * (int(viking_attack[0]) + (0.75 * int(viking_agility[0]))) +  int(jumlah_pasukan_2) * (int(viking_attack[1]) + (0.75 * int(viking_agility[1])))
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
                    total_defend = int(banyak_enemy_1) * (int(roma_defend[0]) + (0.75 * int(roma_agility[0]))) +  int(banyak_enemy_2) * (int(roma_defend[1]) + (0.75 * int(roma_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')

                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', jumlah_pasukan_1)
                            print('Teutonic Knight : ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return game()
                elif choose_enemy == puak_trav[1] :
                    print('Swordman')
                    print('Attack : 65, Defend : 75, Agility : 40')
                    print('Theutaes Thunder')
                    print('Attack : 95, Defend : 85, Agility : 60')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Swordman : ', banyak_enemy_1)
                    print('Enemy Theutaes Thunder : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(galia_defend[0]) + (0.75 * int(galia_agility[0]))) +  int(banyak_enemy_2) * (int(galia_defend[1]) + (0.75 * int(galia_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', jumlah_pasukan_1)
                            print('Teutonic Knight: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                
                else  :
                    print('Clubswinger')
                    print('Attack : 75, Defend : 75, Agility : 35')
                    print('Teutonic Knight')
                    print('Attack : 100, Defend : 100, Agility : 55')
                    banyak_enemy_1 = random.randrange(1, 100)
                    banyak_enemy_2 = random.randrange (1, 100)
                    print('Enemy Clubswinger : ', banyak_enemy_1)
                    print('Enemy Teutonic Knight : ', banyak_enemy_2)
                    total_defend = int(banyak_enemy_1) * (int(viking_defend[0]) + (0.75 * int(viking_agility[0]))) +  int(banyak_enemy_2) * (int(viking_defend[1]) + (0.75 * int(viking_agility[1])))
                    print('Enemy total defend : ', total_defend)
                    print('To attack type SERANG')
                    serang = input()
                    if serang == 'SERANG' :
                        pemenang = total_attack - total_defend
                        if pemenang > 0 :
                            print('YOU WIN!')
                            print('Puak : Vikings')
                            print('TROOPS')
                            print('Clubswinger : ', jumlah_pasukan_1)
                            print('Teutonic Knight: ', jumlah_pasukan_2)
                            print('Total attack : ', total_attack)
                            print('Total defend : ', total_defend)
                            print('Total kemenangan : ', round(total_attack/total_defend))
                        else :
                            print('YOU LOSE!')
                            return get_path_names()    
    else:
        game()    

puak_trav= ['Romans', 'Galia', 'Vikings']
roma_attack = [80, 125]
roma_defend = [70, 85]
roma_agility = [30, 40]

galia_attack = [65, 95]
galia_defend = [75, 85]
galia_agility = [40, 60]

viking_attack = [75, 100]
viking_defend = [75, 100]
viking_agility = [35, 55]

def begin():
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    lgn = int(input ("silahkan pilih 1/2 : ")  )
    if lgn == 1:
        signup()
    if lgn == 2:
        login()
    elif (lgn!=1 and  lgn!=2):
        begin()


begin ()  
game()
