#!/usr/bin/env python
# coding: utf-8

# In[6]:


# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:47:46 2022

@author: Jessie Theodora
"""

#GAME
import random
puak = ["Roma","Galia","Viking"]

roma = ["Imperian","Equites Cesaeris"]
attack_roma = [80,125]
defend_roma = [70,85]
agility_roma = [30,40]
roma_wheat_needs = [50,150]
roma_water_needs = [100,200]

galia = ["Swordman","Theutaes Thunder"]
attack_galia = [65,95]
defend_galia = [75,85]
agility_galia = [40,60]
galia_wheat_needs = [50,50]
galia_water_needs = [45,150]

viking = ["Clubswinger","Teutonic Knight"]
attack_viking = [75,100]
defend_viking = [75,100]
agility_viking = [35,55]
viking_wheat_needs = [65,200]
viking_water_needs = [65,200]

#SUMBER DAYA TEAMS
gandum = random.randrange(150,350)
air = random.randrange(200,400)
sd_gandum_roma = (gandum)-(roma_wheat_needs[0]+roma_wheat_needs[1])
sd_air_roma = (air)-(roma_water_needs[0]+roma_water_needs[1])
sd_gandum_galia = (gandum)-(galia_wheat_needs[0]+galia_wheat_needs[1])
sd_air_galia = (air)-(galia_water_needs[0]+galia_water_needs[1])
sd_gandum_viking = (gandum)-(viking_wheat_needs[0]+viking_wheat_needs[1])
sd_air_viking = (gandum)-(viking_water_needs[0]+viking_water_needs[1])

def start_game():
    print ("Gandum yang anda miliki: ", gandum)
    print ("Air yang anda miliki: ", air)
    for x in puak:
        print (x)
    pilihan_puak = input("Masukkan puak pilihan anda(kapital): ")
    if pilihan_puak == "ROMA":
        print (roma[0] + ": ")
        print ("Attack: ", attack_roma[0])
        print ("Defence: ", defend_roma[0])
        print ("Agility: ", agility_roma[0])
        print ("Kebutuhan gandum: ", roma_wheat_needs[0])
        print ("Kebutuhan air: ", roma_water_needs[0])
        print (roma[1] + ": ")
        print ("Attack: ", attack_roma[1])
        print ("Defence: " , defend_roma[1])
        print ("Agility: " , agility_roma[1])
        print ("Kebutuhan gandum: ", roma_wheat_needs[1])
        print ("Kebutuhan air: ", roma_water_needs[1])
        if sd_gandum_roma < 0 or sd_air_roma < 0:
            print ("Jumlah gandum dan air anda tidak cukup untuk memilih pasukan ini")
            print ("Tips: Jika gandum > 200 dan air > 300, pilih Roma; Jika gandum > 100 dan air > 195, pilih Galia; Jika gandum > 265 dan air > 265, pilih Viking")
            return start_game()
        else:
            jumlah_imperians = input("Masukkan jumlah Imperians untuk menyerang: ")
            jumlah_equites = input("Masukan jumlah Equites Cesaeris untuk menyerang: ")
            total_attack = (int(jumlah_imperians)*(attack_roma[0]+0.75*agility_roma[0])) + (int(jumlah_equites)*(attack_roma[1]+0.75*agility_roma[1]))
            print ("Total attack anda: ", str(total_attack))
            puak_musuh = random.choice(puak)
            print ("Pilihan puak musuh anda adalah ", puak_musuh, "!!!")
            if puak_musuh == "Roma":
                print (roma[0] , ": ")
                print ("Attack: ", attack_roma[0])
                print ("Defence: " , defend_roma[0])
                print ("Agility: " , agility_roma[0])
                print (roma[1], ": ")
                print ("Attack: ", attack_roma[1])
                print ("Defence: ", defend_roma[1])
                print ("Agility: ", agility_roma[1])
                total_imperians_musuh = random.randrange(1,100)
                total_equites_musuh = random.randrange(1,100)
                print ("Jumlah Imperians musuh: ", total_imperians_musuh)
                print ("Jumlah Equites Cesaeris musuh: ", total_equites_musuh)
                defend_roma_musuh = (int(total_imperians_musuh)*(defend_roma[0]+0.75*agility_roma[0])) + (int(total_equites_musuh)*(defend_roma[1]+0.75*agility_roma[1]))
                print ("Total defence musuh: ", defend_roma_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_roma_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (roma[0], ": ", jumlah_imperians)
                        print (roma[1], ": ", jumlah_equites)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_roma_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_roma_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
                
            if puak_musuh == "Galia":
                print (galia[0] + ": ")
                print ("Attack: ", attack_galia[0])
                print ("Defence: ", defend_galia[0])
                print ("Agility: ", agility_galia[0])
                print (galia[1],": ")
                print ("Attack: ", attack_galia[1])
                print ("Defence: ", defend_galia[1])
                print ("Agility: ", agility_galia[1])
                total_swordman_musuh = random.randrange(1,100)
                total_theutates_musuh = random.randrange(1,100)
                print ("Jumlah Swordman musuh: ", total_swordman_musuh)
                print ("Jumlah Theutates Thunder musuh: ", total_theutates_musuh)
                defend_galia_musuh = (int(total_swordman_musuh)*(defend_galia[0]+0.75*agility_galia[0])) + (int(total_theutates_musuh)*(defend_galia[1]+0.75*agility_galia[1]))
                print ("Total defence musuh: ", defend_galia_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_galia_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (roma[0], ": ", jumlah_imperians)
                        print (roma[1], ": ", jumlah_equites)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_galia_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_galia_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
            
            if puak_musuh == "Viking":
                print (viking[0] + ": ")
                print ("Attack: ", attack_viking[0])
                print ("Defence: ", defend_viking[0])
                print ("Agility: ", agility_viking[0])
                print (viking[1], ": ")
                print ("Attack: ", attack_viking[1])
                print ("Defence: ", defend_viking[1])
                print ("Agility: ", agility_viking[1])
                total_clubswinger_musuh = random.randrange(1,100)
                total_teutonic_musuh = random.randrange(1,100)
                print ("Jumlah Clubswinger musuh: ", total_clubswinger_musuh)
                print ("Jumlah Teutonic Knight musuh: ", total_teutonic_musuh)
                defend_viking_musuh = (int(total_clubswinger_musuh)*(defend_viking[0]+0.75*agility_viking[0])) + (int(total_teutonic_musuh)*(defend_viking[1]+0.75*agility_viking[1]))
                print ("Total defence musuh: ", defend_viking_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_viking_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (roma[0], ": ", jumlah_imperians)
                        print (roma[1], ": ", jumlah_equites)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_viking_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_viking_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
                
    if pilihan_puak == "GALIA":
        print (galia[0] + ": ")
        print ("Attack: ", attack_galia[0])
        print ("Defence: ", defend_galia[0])
        print ("Agility: ", agility_galia[0])
        print ("Kebutuhan gandum: ", galia_water_needs[0])
        print ("Kebutuhan air: ", galia_water_needs[0])
        print (galia[1], ": ")
        print ("Attack: ", attack_galia[1])
        print ("Defence: ", defend_galia[1])
        print ("Agility: ", agility_galia[1])
        print ("Kebutuhan gandum: ", galia_wheat_needs[1])
        print ("Kebutuhan air: ", galia_water_needs[1])
        if sd_gandum_galia < 0 or sd_air_galia < 0:
            print ("Jumlah gandum dan air anda tidak cukup untuk memilih pasukan ini")
            print ("Tips: Jika gandum > 200 dan air > 300, pilih Roma; Jika gandum > 100 dan air > 195, pilih Galia; Jika gandum > 265 dan air > 265, pilih Viking")
            return start_game()
        else:
            jumlah_swordman = input("Masukkan jumlah Swordman untuk menyerang: ")
            jumlah_theutates = input("Masukan jumlah Theutates Thunder untuk menyerang: ")
            total_attack = (int(jumlah_swordman)*(attack_galia[0]+0.75*agility_galia[0])) + (int(jumlah_theutates)*(attack_galia[1]+0.75*agility_galia[1]))
            print ("Total attack anda: ", str(total_attack))
            puak_musuh = random.choice(puak)
            print ("Pilihan puak musuh anda adalah ", puak_musuh, "!!!")
            if puak_musuh == "Roma":
                print (roma[0], ": ")
                print ("Attack: ", attack_roma[0])
                print ("Defence: ", defend_roma[0])
                print ("Agility: ", agility_roma[0])
                print (roma[1], ": ")
                print ("Attack: ", attack_roma[1])
                print ("Defence: ", defend_roma[1])
                print ("Agility: ", agility_roma[1])
                total_imperians_musuh = random.randrange(1,100)
                total_equites_musuh = random.randrange(1,100)
                print ("Jumlah Imperians musuh: ", total_imperians_musuh)
                print ("Jumlah Equites Cesaeris musuh: ", total_equites_musuh)
                defend_roma_musuh = (int(total_imperians_musuh)*(defend_roma[0]+0.75*agility_roma[0])) + (int(total_equites_musuh)*(defend_roma[1]+0.75*agility_roma[1]))
                print ("Total defence musuh: ", defend_roma_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_roma_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (galia[0], ": ", jumlah_swordman)
                        print (galia[1], ": ", jumlah_theutates)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_roma_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_roma_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
                
            if puak_musuh == "Galia":
                print (galia[0] + ": ")
                print ("Attack: ", attack_galia[0])
                print ("Defence: ", defend_galia[0])
                print ("Agility: ", agility_galia[0])
                print (galia[1], ": ")
                print ("Attack: ", attack_galia[1])
                print ("Defence: ", defend_galia[1])
                print ("Agility: ", agility_galia[1])
                total_swordman_musuh = random.randrange(1,100)
                total_theutates_musuh = random.randrange(1,100)
                print ("Jumlah Swordman musuh: ", total_swordman_musuh)
                print ("Jumlah Theutates Thunder musuh: ", total_theutates_musuh)
                defend_galia_musuh = (int(total_swordman_musuh)*(defend_galia[0]+0.75*agility_galia[0])) + (int(total_theutates_musuh)*(defend_galia[1]+0.75*agility_galia[1]))
                print ("Total defence musuh: ", defend_galia_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_galia_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (galia[0], ": ", jumlah_swordman)
                        print (galia[1], ": ", jumlah_theutates)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_galia_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_galia_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
            
            if puak_musuh == "Viking":
                print (viking[0], ": ")
                print ("Attack: ", attack_viking[0])
                print ("Defence: ", defend_viking[0])
                print ("Agility: ", agility_viking[0])
                print (viking[1], ": ")
                print ("Attack: ", attack_viking[1])
                print ("Defence: ", defend_viking[1])
                print ("Agility: ", agility_viking[1])
                total_clubswinger_musuh = random.randrange(1,100)
                total_teutonic_musuh = random.randrange(1,100)
                print ("Jumlah Clubswinger musuh: ", total_clubswinger_musuh)
                print ("Jumlah Teutonic Knight musuh: ", total_teutonic_musuh)
                defend_viking_musuh = (int(total_clubswinger_musuh)*(defend_viking[0]+0.75*agility_viking[0])) + (int(total_teutonic_musuh)*(defend_viking[1]+0.75*agility_viking[1]))
                print ("Total defence musuh: ", defend_viking_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_viking_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (galia[0], ": ", jumlah_swordman)
                        print (galia[1], ": ", jumlah_theutates)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_viking_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_viking_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()

    if pilihan_puak == "VIKING":
        print (viking[0], ": ")
        print ("Attack: ", attack_viking[0])
        print ("Defence: ", defend_viking[0])
        print ("Agility: ", agility_viking[0])
        print ("Kebutuhan gandum: ", viking_water_needs[0])
        print ("Kebutuhan air: ", viking_water_needs[0])
        print (viking[1], ": ")
        print ("Attack: ", attack_viking[1])
        print ("Defence: ", defend_viking[1])
        print ("Agility: ", agility_viking[1])
        print ("Kebutuhan gandum: ", viking_wheat_needs[1])
        print ("Kebutuhan air: ", viking_water_needs[1])
        if sd_gandum_viking < 0 or sd_air_viking < 0:
            print ("Jumlah gandum dan air anda tidak cukup untuk memilih pasukan ini")
            print ("Tips: Jika gandum > 200 dan air > 300, pilih Roma; Jika gandum > 100 dan air > 195, pilih Galia; Jika gandum > 265 dan air > 265, pilih Viking")
            return start_game()
        else:
            jumlah_clubswinger = input("Masukkan jumlah Clubswinger untuk menyerang: ")
            jumlah_teutonic = input("Masukan jumlah Teutonic Knight untuk menyerang: ")
            total_attack = (int(jumlah_clubswinger)*(attack_viking[0]+0.75*agility_viking[0])) + (int(jumlah_teutonic)*(attack_viking[1]+0.75*agility_viking[1]))
            print ("Total attack anda: ", str(total_attack))
            puak_musuh = random.choice(puak)
            print ("Pilihan puak musuh anda adalah ", puak_musuh, "!!!")
            if puak_musuh == "Roma":
                print (roma[0], ": ")
                print ("Attack: ", attack_roma[0])
                print ("Defence: ", defend_roma[0])
                print ("Agility: ", agility_roma[0])
                print (roma[1], ": ")
                print ("Attack: ", attack_roma[1])
                print ("Defence: ", defend_roma[1])
                print ("Agility: ", agility_roma[1])
                total_imperians_musuh = random.randrange(1,100)
                total_equites_musuh = random.randrange(1,100)
                print ("Jumlah Imperians musuh: ", total_imperians_musuh)
                print ("Jumlah Equites Cesaeris musuh: ", total_equites_musuh)
                defend_roma_musuh = (int(total_imperians_musuh)*(defend_roma[0]+0.75*agility_roma[0])) + (int(total_equites_musuh)*(defend_roma[1]+0.75*agility_roma[1]))
                print ("Total defence musuh: ", defend_roma_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_roma_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (viking[0], ": ", jumlah_clubswinger)
                        print (viking[1], ": ", jumlah_teutonic)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_roma_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_roma_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
                
            if puak_musuh == "Galia":
                print (galia[0], ": ")
                print ("Attack: ", attack_galia[0])
                print ("Defence: ", defend_galia[0])
                print ("Agility: ", agility_galia[0])
                print (galia[1], ": ")
                print ("Attack: ", attack_galia[1])
                print ("Defence: ", defend_galia[1])
                print ("Agility: ", agility_galia[1])
                total_swordman_musuh = random.randrange(1,100)
                total_theutates_musuh = random.randrange(1,100)
                print ("Jumlah Swordman musuh: ", total_swordman_musuh)
                print ("Jumlah Theutates Thunder musuh: ", total_theutates_musuh)
                defend_galia_musuh = (int(total_swordman_musuh)*(defend_galia[0]+0.75*agility_galia[0])) + (int(total_theutates_musuh)*(defend_galia[1]+0.75*agility_galia[1]))
                print ("Total defence musuh: ", defend_galia_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_galia_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (viking[0], ": ", jumlah_clubswinger)
                        print (viking[1], ": ", jumlah_teutonic)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_galia_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_galia_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
            
            if puak_musuh == "Viking":
                print (viking[0], ": ")
                print ("Attack: ", attack_viking[0])
                print ("Defence: ", defend_viking[0])
                print ("Agility: ", agility_viking[0])
                print (viking[1], ": ")
                print ("Attack: ", attack_viking[1])
                print ("Defence: ", defend_viking[1])
                print ("Agility: ", agility_viking[1])
                total_clubswinger_musuh = random.randrange(1,100)
                total_teutonic_musuh = random.randrange(1,100)
                print ("Jumlah Clubswinger musuh: ", total_clubswinger_musuh)
                print ("Jumlah Teutonic Knight musuh: ", total_teutonic_musuh)
                defend_viking_musuh = (int(total_clubswinger_musuh)*(defend_viking[0]+0.75*agility_viking[0])) + (int(total_teutonic_musuh)*(defend_viking[1]+0.75*agility_viking[1]))
                print ("Total defence musuh: ", defend_viking_musuh)
                print ("Mulai penyerangan? |Ya/Tidak|")
                order = input()
                if order == "Ya":
                    match = total_attack - defend_viking_musuh
                    if match > 0:
                        print ("Selamat anda MENANG!!!")
                        print ("Username: ", username)
                        print ("Puak: ", pilihan_puak)
                        print ("Jumlah Tentara: ")
                        print (viking[0], ": ", jumlah_clubswinger)
                        print (viking[1], ": ", jumlah_teutonic)
                        print ("Total attack: ", total_attack)
                        print ("Total defence musuh: ",defend_viking_musuh)
                        print ("Total kemenangan: ", round(total_attack/defend_viking_musuh))
                    else:
                        print ("anda KALAH, goodluck next time :v")
                        return start_game()
                elif order == "Tidak":
                    return start_game()
                
#REGISTER DAN LOGIN
username = []
password = []
nickname = []
def register():
    nickname.append(input("Masukkan nama panggilan anda:"))
    username.append(input("daftarkan username:"))
    password.append(input("password:"))
def login():
    username1 = input("Username:")
    password1 = input("Password:")
    if username1 in username and password1 in password:
        print("SELAMAT DATANG DI PERMAINAN GLADIATOR!!!")
        start_game()
    else:
        print("Username/Password yang anda masukkam salah!")
while True:
    account_ans = input("pilih menu:  a)Register     b)login     c)Keluar ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        break


# In[ ]:




