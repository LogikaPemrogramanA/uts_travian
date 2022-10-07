import random;

user = {
    "id": "yehuda",
    "password": "yehuyehu",
    "status_login": "unactive"
};
print ("masukkan id dan password")
id= input ('id :')
password= input ('password :')
def login(id, password): 
    if id == user["id"] and password == user["password"]:
        user['status_login'] = "active";
    else:
        return "error"

data = {
    "roma": {
        "imperian": {
            "attack" : 80,
            "defend" : 70,
            "agility": 30,
        },
        "equites Cesaeris": {
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

# fix
def player(): 
    print("="*5+"Daftar puak"+"="*5,*[f'{i}' for i in data.keys()], sep='\n')
    puak = input("Pilih puak > ");
    print("="*5+"Daftar pasukan"+"="*5,*[f'{i}' for i in data[puak].keys()], sep='\n')
    pasukan = input("Pilih pasukan > ");
    print("="*5+"Jumlah pasukan"+"="*5)
    banyak_pasukan = int(input("Pilih jumlah character > "));
    print("*"*20);

    return {
        "puak": puak,
        "pasukan": pasukan,
        "banyak_pasukan": banyak_pasukan
    }

#fix
def computer():
    puak = random.choice(list(data.keys()));
    pasukan = random.choice(list(data[puak].keys()));
    banyak_pasukan = random.randint(10,20);
    print(f'computer using {banyak_pasukan} {pasukan} from {puak}');
    print("*"*20);

    return {
        "puak": puak,
        "pasukan": pasukan,
        "banyak_pasukan": banyak_pasukan
    }

def akumulasi(status, puak, pasukan, banyak_pasukan):
    attack = data[puak][pasukan]["attack"];
    defend = data[puak][pasukan]["defend"];
    agility = data[puak][pasukan]["agility"];
    total_attack = banyak_pasukan * (attack+ (agility * 0.75));
    total_pertahanan = banyak_pasukan * (defend+ (agility * 0.75));
    print(f'{status} stats: \ntotal attack: {total_attack} \ntotal defend: {total_pertahanan}');
    print("*"*20);

    return {
        "total_attack": total_attack,
        "total_pertahanan": total_pertahanan,
    }

def winner(atk_player, atk_computer, def_player, def_computer): 
    total_atk = atk_player + atk_computer;
    total_def = def_player + def_computer;
    print(f'total attack player and computer: {total_atk} \ntotal defend player and computer: {total_def}');
    print("*"*20);
    if total_atk - total_def >= 0:
        print("Attacker win");
    else:
        print("Defender win");


login(id, password)

if user["status_login"] == "active":

    player_x = player();
    computer_y = computer();

    akumulasi_player = akumulasi("Attacker",player_x["puak"], player_x["pasukan"], player_x["banyak_pasukan"],);
    akumulasi_computer = akumulasi("Defender" ,computer_y["puak"], computer_y["pasukan"], computer_y["banyak_pasukan"],);

    juara = winner(
        akumulasi_player["total_attack"], 
        akumulasi_computer["total_attack"],
        akumulasi_player["total_pertahanan"], 
        akumulasi_computer["total_pertahanan"], 
    )
else:
    raise Exception ('tidak dapat bermain, anda belum login'); 
    