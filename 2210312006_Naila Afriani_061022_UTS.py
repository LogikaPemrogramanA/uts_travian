import random

def formula(data):
   types = available()[list(data[1].keys())[0]]
   total_attack = 0
   total_defend = 0
   
   for x in data[1][list(data[1].keys())[0]].keys():
      total_attack += data[1][list(data[1].keys())[0]][x] * (types[x][0] + (0.75 * types[x][2]))
      total_defend += data[1][list(data[1].keys())[0]][x] * (types[x][1] + (0.75 * types[x][2]))

   return (data, total_attack, total_defend)

def who_win(data):
   tentara = list(data[0][0][1][list(data[0][0][1].keys())[0]].keys())
   print(tentara)
   f = data[0][0][1][list(data[0][0][1].keys())[0]]
   print(f)
   print("""
                        -- PEMENANG --
          User             : """ + data[0][0][0] + """
          Puak             : """ + list(data[0][0][1].keys())[0] + """
          Jumlah Tentara   : """ + "-" + tentara[0] + ":" + str(f[tentara[0]]) + """
                             """ + "-" + tentara[1] + ":" + str(f[tentara[1]]) + """
          Total Attack     : """ + str(data[0][1]) + """
          Total Defend     : """ + str(data[0][2]) + """
          Total Kemenangan : """ + str(data[1]) + """
          """)

def war_field(user, computer):
   comp_data = formula(computer)
   computer_attack = comp_data[1]
   computer_defend = comp_data[2]

   user_data = formula(user)
   user_attack = user_data[1]
   user_defend = user_data[2]

   rounds = 0

   game_data = []
   
   while True:
      user_stats = computer_attack - user_defend
      computer_stats = user_attack - computer_defend

      rounds += 1
         
      if user_stats <= 0:
         data = comp_data
         break
      elif computer_stats <= 0:
         data = user_data
         break

   game_data.append(data)
   game_data.append(rounds)

   return game_data

def ai():
   data = {}
   available_types = available()

   chc = random.choice(list(available_types.keys()))
   data[chc] = {}
   
   i = random.randint(1, 5)
   v = 0

   while v <= i:
      chc2 = random.choice(list(available_types[chc].keys()))
      i2 = random.randint(1, 100)
      data[chc][chc2] = i2

      v += 1

   return ("Computer", data)

def register(database):
   new_id = input("Buat ID : ")
   new_pass = input("Buat Password : ")

   database[new_id] = new_pass
   
def login(database):
   user_id = input("Masukkan ID : ")
   password = input("Masukkan Password : ")

   while (user_id not in database.keys()) or (password != database[user_id]):
      print("ID atau Password tidak cocok!")
      
      user_id = input("Masukkan ID : ")
      password = input("Masukkan Password : ")

   print("Login Berhasil!")

   return user_id

def available():
   data = {"Roma"   : {"Imperian"    : [80, 70, 30], "Equites cesaeris" : [125, 85, 40]},
           "Galia"  : {"Swordman"    : [65, 75, 40], "Theutaes thunder" : [95, 85, 60]},
           "Viking" : {"Clubswinger" : [75, 75, 35], "Teutonic knight"  : [100, 100, 55]}}

   return data

def choose_army(user):
   data = {}
   available_types = available()
   
   print("Pilih Kelompok : ")
   print("""
             1. Roma
             2. Galia
             3. Viking
         """)

   while True:
      typ = input("> ").capitalize()

      if typ in available_types.keys():
         data[typ] = {}
         
         choosen = available_types[typ]
         type_keys = tuple(choosen.keys())
        
         print("Pilih Jenis : ")
         print(f"""
                   1. {type_keys[0]}
                      - Attack  : {choosen[type_keys[0]][0]}
                      - Defend  : {choosen[type_keys[0]][1]}
                      - Agility : {choosen[type_keys[0]][2]}
                   2. {type_keys[1]}
                      - Attack  : {choosen[type_keys[1]][0]}
                      - Defend  : {choosen[type_keys[1]][1]}
                      - Agility : {choosen[type_keys[1]][2]}
                """)

         while True:
            army = input("> ").capitalize()
            
            if army in type_keys:
               amount = int(input("Jumlah : "))
               data[typ][army] = amount
               
               done = input("Sudah? (y/n) : ").lower()

               if done == "y":
                  break
            else:
               print("Tidak Tersedia!")
               
         break
      else:
         print("Tidak Tersedia!")

   return (user, data)

def main():
   database = {}

   register(database)
   user_id = login(database)

   user = choose_army(user_id)
   computer = ai()
   
   winner = war_field(user, computer)

   who_win(winner)
   

if __name__ == "__main__":
   main()
