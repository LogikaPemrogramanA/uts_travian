# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:27:04 2022

@author: Aura Putri Mahabah
"""

userid = "Aura"
password = "kucing"

uid = input("Enter username:")
pwd = input("Enter password:")
if uid == userid and pwd == password:
    print("Anda Telah Login") 
    print("Selamat bermain")
    print("Silakan pilih puak")
    print ("roma" , "galia" , "viking")
    input("puak :")
    puak = ["roma" , "galia" , "viking"]
    
else:        
    print ("Username atau Password Anda Salah")

data = {
    "roma": {
        "imperian": {
            "attack" : 80,
            "defend" : 70,
            "agility": 30,
        },
        "equites cesaeris": {
            "attack" : 125,
            "defend" : 85,
            "agility": 40,
        }
    },
    "galia": {
        "swordman": {
            "attack" : 65,
            "defend" : 75,
            "agility": 40,
        },
        "theutaes thunder": {
            "attack" : 95,
            "defend" : 85,
            "agility": 60,
        }
    },
    "viking": {
        "clubswinger": {
            "attack" : 75,
            "defend" : 75,
            "agility": 35,
        },
        "teutonic knight": {
            "attack": 100,
            "defend" : 100,
            "agility": 55,
        }
    },

};

    
# user memilih puak dan jumlah pasukan
def memilih_puak (): input("puak :")
if memilih_puak  : "roma" 
jumlah_pasukan = input("jumlah pasukan imperian: ")
jumlah_pasukan = input("jumlah pasukan equites cesaeris: ")
if memilih_puak : "galia"
jumlah_pasukan = input("jumlah pasukan swordman: ")
jumlah_pasukan = input("jumlah pasukan theutaes thunder: ")
if memilih_puak : "viking"
jumlah_pasukan= input("jumlah pasukan clubswinger: ")
jumlah_pasukan= input("jumlah pasukan teutonic knight: ")


#fungsi random musuh
import random 
print(random.choice(puak))
print(random.choice(jumlah_pasukan))


# 
def perhitungan () :
    jumlah_pasukan = 50
    attack = 80
    agility = 70
    defend = 30
    total_attack = jumlah_pasukan * (attack + (0.75 * agility))
    pertahanan = jumlah_pasukan * (defend + (0.75 * agility))
    
    print(total_attack)
    print(pertahanan)
    
#pemenang
    hasil = total_attack - pertahanan
    print(hasil)
    
    
#Output
#Enter username:Aura
#Enter password:kucing
#Anda Telah Login
#Selamat bermain
#Silakan pilih puak
#roma galia viking
#puak : roma
#jumlah pasukan imperian: 50
#jumlah pasukan equites cesaeris: 50
#total_attack = 6.625
#pertahanan = 4.125
#hasil = 2500
#menang = 1

    
    
    




    
     
    
    

    
    

    
    

     
     
    
