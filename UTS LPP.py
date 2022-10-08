import random
daftar_puak = ["Roma", "Galia", "Viking"]
daftar_puak2 = ["Roma : gandum = 200, air = 300", "Galia : gandum = 100, air = 195", "Viking : gandum = 265, air = 265"]
def mulai_game():
    #ROMA
    status_puak_roma1 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_roma1 = ["80", "70", "30", "50", "100"]
    status_puak_roma2 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_roma2 = ["125", "85", "40", "150", "200"]
    #GALIA
    status_puak_galia1 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_galia1 = ["65", "75", "40", "50", "45"]
    status_puak_galia2 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_galia2 = ["95", "85", "60", "50", "100"]
    #VIKING
    status_puak_viking1 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_viking1 = ["55", "75", "35", "65", "65"]
    status_puak_viking2 = ["Attack : ", "Defend : ", "Agility : ", "Kebutuhan gandum : ", "Kebutuhan air : "]
    nilai_puak_viking2 = ["100", "100", "55", "200", "200"]
    #SUMBERDAYA
    gandum = random.randrange(200, 350)
    air = random.randrange(195, 380)
    sumberdayaroma1 = (gandum) - (50+150)
    sumberdayaroma2 = (air) - (100+200)
    sumberdayagalia1 = (gandum) - (50+50)
    sumberdayagalia2 = (air) - (45+150)
    sumberdayaviking1 = (gandum) - (65+200)
    sumberdayaviking2 = (air) - (65+200)
    nickname = input("Silahkan masukan nickname anda: ")
    print ("Hallo, ", nickname)
    print("I------------------ Selamat Datang di game Travian ------------------I")
    print("Sumber daya gandum anda : ", gandum)
    print("Sumber daya air anda : ", air)
    print("Silahkan pilih puak yang tersedia:")
    for x in daftar_puak2:
        print (x)
    puak_pilihan = input("Ketik puak yang ingin digunakan: ")
#PUAK = ROMA
    if puak_pilihan.lower() == "roma" :
        print ("Imperians :")
        print(status_puak_roma1[0] + nilai_puak_roma1[0])
        print(status_puak_roma1[1] + nilai_puak_roma1[1])
        print(status_puak_roma1[2] + nilai_puak_roma1[2])
        print(status_puak_roma1[3] + nilai_puak_roma1[3])
        print(status_puak_roma1[4] + nilai_puak_roma1[4])
        print ("Equites Cesaeris :")
        print(status_puak_roma2[0] + nilai_puak_roma2[0])
        print(status_puak_roma2[1] + nilai_puak_roma2[1])
        print(status_puak_roma2[2] + nilai_puak_roma2[2])
        print(status_puak_roma2[3] + nilai_puak_roma2[3])
        print(status_puak_roma2[4] + nilai_puak_roma2[4])
        if sumberdayaroma1 < 0 or sumberdayaroma2 < 0 :
            print ("Sumberdaya tidak cukup untuk mengerahkan pasukan ini, silahkan pilih yang lain")
            print ("Tips1 : Jika sumber daya gandum > 265 dan sumber daya air 265 disarankan untuk mengerahkan Viking")
            print ("Tips2 : Jika sumber daya gandum > 200 dan sumber daya air 300 disarankan untuk mengerahkan Roma")
            print ("Tips3 : Jika sumber daya gandum > 100 dan sumber daya air 195 disarankan untuk mengerahkan Viking")
            return mulai_game()
        else :
            totalpasukan1 = input("Masukan pasukan Imperians yang akan dikerahkan: ")
            totalpasukan2 = input("Masukan pasukan Equites Cesaeris yang akan dikerahkan: ")
            if int(totalpasukan1) > 100 or int(totalpasukan2) > 100 :
                print("Pasukan yang dikerahkan melebihi batas!!")
                return mulai_game()
            else :
                total_attack = int(totalpasukan1) * (int(nilai_puak_roma1[0]) + (0.75 * int(nilai_puak_roma1[2]))) +  int(totalpasukan2) * (int(nilai_puak_roma2[0]) + (0.75 * int(nilai_puak_roma2[2])))
                print("Total attack pasukan anda : " + str(total_attack))
                print ("\n")
                print("Giliran lawan memilih puak...")
                puak_lawan = random.choice(daftar_puak)
                print("Lawan telah memilih", puak_lawan)
                if puak_lawan.lower() == "roma":
                    print ("Imperians :")
                    print(status_puak_roma1[0] + nilai_puak_roma1[0])
                    print(status_puak_roma1[1] + nilai_puak_roma1[1])
                    print(status_puak_roma1[2] + nilai_puak_roma1[2])
                    print ("Equites Cesaeris :")
                    print(status_puak_roma2[0] + nilai_puak_roma2[0])
                    print(status_puak_roma2[1] + nilai_puak_roma2[1])
                    print(status_puak_roma2[2] + nilai_puak_roma2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Imperians yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Equites Cesaeris yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_roma1[1]) + (0.75 * int(nilai_puak_roma1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_roma2[1]) + (0.75 * int(nilai_puak_roma2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Imperians :", totalpasukan1)
                        print ("Equites Cesaeris :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "galia":
                    print ("Swordman :")
                    print(status_puak_galia1[0] + nilai_puak_galia1[0])
                    print(status_puak_galia1[1] + nilai_puak_galia1[1])
                    print(status_puak_galia1[2] + nilai_puak_galia1[2])
                    print ("Theutaes Thunder :")
                    print(status_puak_galia2[0] + nilai_puak_galia2[0])
                    print(status_puak_galia2[1] + nilai_puak_galia2[1])
                    print(status_puak_galia2[2] + nilai_puak_galia2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Swordman yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Theutaes Thunder yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_galia1[1]) + (0.75 * int(nilai_puak_galia1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_galia2[1]) + (0.75 * int(nilai_puak_galia2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Imperians :", totalpasukan1)
                        print ("Equites Cesaeris :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "viking":
                    print ("Clubswinger :")
                    print(status_puak_viking1[0] + nilai_puak_viking1[0])
                    print(status_puak_viking1[1] + nilai_puak_viking1[1])
                    print(status_puak_viking1[2] + nilai_puak_viking1[2])
                    print ("Teutonic Knight :")
                    print(status_puak_viking2[0] + nilai_puak_viking2[0])
                    print(status_puak_viking2[1] + nilai_puak_viking2[1])
                    print(status_puak_viking2[2] + nilai_puak_viking2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Clubswinger yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Teutonic Knight yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_viking1[1]) + (0.75 * int(nilai_puak_viking1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_viking2[1]) + (0.75 * int(nilai_puak_viking2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Impearins :", totalpasukan1)
                        print ("Equites Cesaeris :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()
#PUAK=GALIA        
    if puak_pilihan.lower() == "galia" :
        print ("Swordman :")
        print(status_puak_galia1[0] + nilai_puak_galia1[0])
        print(status_puak_galia1[1] + nilai_puak_galia1[1])
        print(status_puak_galia1[2] + nilai_puak_galia1[2])
        print(status_puak_galia1[3] + nilai_puak_galia1[3])
        print(status_puak_galia1[4] + nilai_puak_galia1[4])
        print ("Theutaes Thunder :")
        print(status_puak_galia2[0] + nilai_puak_galia2[0])
        print(status_puak_galia2[1] + nilai_puak_galia2[1])
        print(status_puak_galia2[2] + nilai_puak_galia2[2])
        print(status_puak_galia2[3] + nilai_puak_galia2[3])
        print(status_puak_galia2[4] + nilai_puak_galia2[4])
        if sumberdayagalia1 < 0 or sumberdayagalia2 < 0 :
            print ("Sumberdaya tidak cukup untuk mengerahkan pasukan ini, silahkan pilih yang lain")
            print ("Tips1 : Jika sumber daya gandum > 265 dan sumber daya air 265 disarankan untuk mengerahkan Viking")
            print ("Tips2 : Jika sumber daya gandum > 200 dan sumber daya air 300 disarankan untuk mengerahkan Roma")
            print ("Tips3 : Jika sumber daya gandum > 100 dan sumber daya air 195 disarankan untuk mengerahkan Viking")
            return mulai_game()
        else :
            totalpasukan1 = input("Masukan pasukan Swordman yang akan dikerahkan: ")
            totalpasukan2 = input("Masukan pasukan Theutaes Thunder yang akan dikerahkan: ")
            if int(totalpasukan1) > 100 or int(totalpasukan2) > 100 :
                print("Pasukan yang dikerahkan melebihi batas!!")
                return mulai_game()
            else :
                total_attack = int(totalpasukan1) * (int(nilai_puak_galia1[0]) + (0.75 * int(nilai_puak_galia1[2]))) +  int(totalpasukan2) * (int(nilai_puak_galia2[0]) + (0.75 * int(nilai_puak_galia2[2])))
                print("Total attack pasukan anda : " + str(total_attack))
                print ("\n")
                print("Giliran lawan memilih puak...")
                puak_lawan = random.choice(daftar_puak)
                print("Lawan telah memilih", puak_lawan)
                if puak_lawan.lower() == "roma":
                    print ("Imperians :")
                    print(status_puak_roma1[0] + nilai_puak_roma1[0])
                    print(status_puak_roma1[1] + nilai_puak_roma1[1])
                    print(status_puak_roma1[2] + nilai_puak_roma1[2])
                    print ("Equites Cesaeris :")
                    print(status_puak_roma2[0] + nilai_puak_roma2[0])
                    print(status_puak_roma2[1] + nilai_puak_roma2[1])
                    print(status_puak_roma2[2] + nilai_puak_roma2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Imperians yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Equites Cesaeris yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_roma1[1]) + (0.75 * int(nilai_puak_roma1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_roma2[1]) + (0.75 * int(nilai_puak_roma2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Swordman :", totalpasukan1)
                        print ("Theutaes Thunder :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "galia":
                    print ("Swordman :")
                    print(status_puak_galia1[0] + nilai_puak_galia1[0])
                    print(status_puak_galia1[1] + nilai_puak_galia1[1])
                    print(status_puak_galia1[2] + nilai_puak_galia1[2])
                    print ("Theutaes Thunder :")
                    print(status_puak_galia2[0] + nilai_puak_galia2[0])
                    print(status_puak_galia2[1] + nilai_puak_galia2[1])
                    print(status_puak_galia2[2] + nilai_puak_galia2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Swordman yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Theutaes Thunder yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_galia1[1]) + (0.75 * int(nilai_puak_galia1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_galia2[1]) + (0.75 * int(nilai_puak_galia2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Swordman :", totalpasukan1)
                        print ("Theutaes Thunder :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "viking":
                    print ("Clubswinger :")
                    print(status_puak_viking1[0] + nilai_puak_viking1[0])
                    print(status_puak_viking1[1] + nilai_puak_viking1[1])
                    print(status_puak_viking1[2] + nilai_puak_viking1[2])
                    print ("Teutonic Knight :")
                    print(status_puak_viking2[0] + nilai_puak_viking2[0])
                    print(status_puak_viking2[1] + nilai_puak_viking2[1])
                    print(status_puak_viking2[2] + nilai_puak_viking2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Clubswinger yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Teutonic Knight yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_viking1[1]) + (0.75 * int(nilai_puak_viking1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_viking2[1]) + (0.75 * int(nilai_puak_viking2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Swordman :", totalpasukan1)
                        print ("Theutaes Thunder :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()
#PUAK=VIKING         
    if puak_pilihan.lower() == "viking" :
        print ("Clubswinger :")
        print(status_puak_viking1[0] + nilai_puak_viking1[0])
        print(status_puak_viking1[1] + nilai_puak_viking1[1])
        print(status_puak_viking1[2] + nilai_puak_viking1[2])
        print(status_puak_viking1[3] + nilai_puak_viking1[3])
        print(status_puak_viking1[4] + nilai_puak_viking1[4])
        print ("Teutonic Knight :")
        print(status_puak_viking2[0] + nilai_puak_viking2[0])
        print(status_puak_viking2[1] + nilai_puak_viking2[1])
        print(status_puak_viking2[2] + nilai_puak_viking2[2])
        print(status_puak_viking2[3] + nilai_puak_viking2[3])
        print(status_puak_viking2[4] + nilai_puak_viking2[4])
        if sumberdayaviking1 < 0 or sumberdayaviking2 < 0 :
            print ("Sumberdaya tidak cukup untuk mengerahkan pasukan ini, silahkan pilih yang lain")
            print ("Tips1 : Jika sumber daya gandum > 265 dan sumber daya air 265 disarankan untuk mengerahkan Viking")
            print ("Tips2 : Jika sumber daya gandum > 200 dan sumber daya air 300 disarankan untuk mengerahkan Roma")
            print ("Tips3 : Jika sumber daya gandum > 100 dan sumber daya air 195 disarankan untuk mengerahkan Viking")
            return mulai_game()
        totalpasukan1 = input("Masukan pasukan Clubswinger yang akan dikerahkan: ")
        totalpasukan2 = input("Masukan pasukan Teutonic Knight yang akan dikerahkan: ")
        if int(totalpasukan1) > 100 or int(totalpasukan2) > 100 :
            print("Pasukan yang dikerahkan melebihi batas!!")
            return mulai_game()
        else :
                total_attack = int(totalpasukan1) * (int(nilai_puak_viking1[0]) + (0.75 * int(nilai_puak_viking1[2]))) +  int(totalpasukan2) * (int(nilai_puak_viking2[0]) + (0.75 * int(nilai_puak_viking2[2])))
                print("Total attack pasukan anda : " + str(total_attack))
                print ("\n")
                print("Giliran lawan memilih puak...")
                puak_lawan = random.choice(daftar_puak)
                print("Lawan telah memilih", puak_lawan)
                if puak_lawan.lower() == "roma":
                    print ("Imperians :")
                    print(status_puak_roma1[0] + nilai_puak_roma1[0])
                    print(status_puak_roma1[1] + nilai_puak_roma1[1])
                    print(status_puak_roma1[2] + nilai_puak_roma1[2])
                    print ("Equites Cesaeris :")
                    print(status_puak_roma2[0] + nilai_puak_roma2[0])
                    print(status_puak_roma2[1] + nilai_puak_roma2[1])
                    print(status_puak_roma2[2] + nilai_puak_roma2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Imperians yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Equites Cesaeris yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_roma1[1]) + (0.75 * int(nilai_puak_roma1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_roma2[1]) + (0.75 * int(nilai_puak_roma2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Clubswinger :", totalpasukan1)
                        print ("Teutonic Knight :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "galia":
                    print ("Swordman :")
                    print(status_puak_galia1[0] + nilai_puak_galia1[0])
                    print(status_puak_galia1[1] + nilai_puak_galia1[1])
                    print(status_puak_galia1[2] + nilai_puak_galia1[2])
                    print ("Theutaes Thunder :")
                    print(status_puak_galia2[0] + nilai_puak_galia2[0])
                    print(status_puak_galia2[1] + nilai_puak_galia2[1])
                    print(status_puak_galia2[2] + nilai_puak_galia2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Swordman yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Theutaes Thunder yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_galia1[1]) + (0.75 * int(nilai_puak_galia1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_galia2[1]) + (0.75 * int(nilai_puak_galia2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Clubswinger :", totalpasukan1)
                        print ("Teutonic Knight :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()

                elif puak_lawan.lower() == "viking":
                    print ("Clubswinger :")
                    print(status_puak_viking1[0] + nilai_puak_viking1[0])
                    print(status_puak_viking1[1] + nilai_puak_viking1[1])
                    print(status_puak_viking1[2] + nilai_puak_viking1[2])
                    print ("Teutonic Knight :")
                    print(status_puak_viking2[0] + nilai_puak_viking2[0])
                    print(status_puak_viking2[1] + nilai_puak_viking2[1])
                    print(status_puak_viking2[2] + nilai_puak_viking2[2])
                    totalpasukan1musuh = random.randrange(1, 100)
                    totalpasukan2musuh = random.randrange(1, 100)
                    print ("Clubswinger yang dikerahkan musuh: ", totalpasukan1musuh)
                    print ("Teutonic Knight yang dikerahkan musuh: ", totalpasukan2musuh)
                    total_defend = int(totalpasukan1musuh) * (int(nilai_puak_viking1[1]) + (0.75 * int(nilai_puak_viking1[2]))) +  int(totalpasukan2musuh) * (int(nilai_puak_viking2[1]) + (0.75 * int(nilai_puak_viking2[2])))
                    print("Total defend musuh : ", total_defend)
                    print("Ketik SERANG jika sudah siap untuk menyerang")
                    komando = input()
                    if komando == "SERANG" :
                        pertandingan = total_attack - total_defend
                    if pertandingan > 0 :
                        print ("ANDA MENANG!!")
                        print ("username : ", nickname)
                        print ("Jumlah pasukan :")
                        print ("Clubswinger :", totalpasukan1)
                        print ("Teutonic Knight :", totalpasukan2)
                        print ("Total attack anda : ", total_attack)
                        print ("Total defend musuh : ", total_defend)
                        print ("Total Kemenangan : ", round(total_attack/total_defend))
                    else :
                        print ("Anda kalah, semoga beruntung lain kali")
                        return mulai_game()
        
#fungsi login
import hashlib
def Register():
    username = input("Masukan Username anda: ")
    pwd = input("Masukan password anda: ")
    conf_pwd = input("Konfirmasi password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(username + "\n")
             f.write(hash1)
        f.close()
        print("Anda telah Terdaftar, silahkan login")
    else:
        print("Password berbeda dengan yang diatas \n")
def login():
    username = input("Masukan username: ")
    pwd = input("Masukan password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if username == stored_email and auth_hash == stored_pwd:
        status_login = "active"
        print("Status login = active")
        print ("\n")
        mulai_game()
        
    else:
         print("Login gagal! \n")

while 1:
    print("I------------------ Selamat Datang ------------------I")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Masukan pilihan Anda: "))
    if ch == 1:
        Register()
    elif ch == 2:
        login()
        break
    elif ch == 3:
        break
    else:
        print("Tidak terdapat pada pilihan!")