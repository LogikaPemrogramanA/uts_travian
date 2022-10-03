**Mari Bermain** <br />
----------------------------------------
1. Buatlah fungsi register akun dengan detail
```
id      : string 
password: string
```

2. Buatlah sebuah fungsi Login dimana jika salah id / password munculkan pesan status error, mencocokan data dari hasil register tadi<br/>
jika berhasil buatlah variabel untuk menyimpan ```status_login = active```
3. jika ```status_login = active``` maka dosen tersebut dapatmemulai permainan <br/>
permainan ini merupakan sebuah simulasi pertandingan gladiator
dimana terdiri dari dari puak dan tentara sebagai beriku </br>
**Roma :** <br/>
```
imperian
attack : 80
defend : 70
agility: 30

Equites Cesaeris
attack : 125
defend : 85
agility: 40
```
**Galia:** </br>
```
swordman
attack : 65
defend : 75
agility : 40

Theutaes Thunder
attack : 95
defend : 85
agility 60

```
**Viking**
```
clubswinger
attack : 75
defend : 75
agility: 35

Teutonic Knight
attack 100
defend : 100
agiligty: 55
```
4. Buatlah fungsi dimana user memilih / input sendiri mau puak apa, setelah itu baru muncul otomatis </br>
tentara yang tersedia pada puak itu.. lalu user diminta untuk input berapa jumlah masing masing tentara

5. Buatlah fungsi random dimana player computer / lawan dari user kita dalam memilih puak dan menentukan sendiri jumlah tentara nya. user selalu berada dalam sisi penyerang

6. rumus total_attack = jumlah_pasukan x (attack + (0.75 x agility))
  rumus pertahanan = jumlah_pasukan x (defend + (0.75 x agility)) </br>
  misalkan penyeranng 100 clubswinger dan 20 Teutonic knight
  ```
  total_attack = 100 * (75 + (0.75x335)) + 20 x (100 + (0.75 x 55))
  berlaku juga untuk pertahanan
  ```
7. Tentukan pemenangnya dengan cara
```
pemenang = total_attack - pertahanan
jika hasil pemenang adalah positif maka penyerang pemenangnya
```
8. lakukan penyerangan terus menerus sampai penyerang kalah
9. munculkan hasil pertandingan akhirnya
```
user : bunga
puak : roma
jumlah tentara
Imperian : 100
Equites Cecaris : 50
Total attack : sekian (hitung)
Total defend : sekian (hitung)
Total kemenangan : 10 Ronde
```

pertanyaan bonus : jika ada yang bisa menyelesaikan akan mendapatkan tambahan 15 point
-------
1. setiap user memiliki sumber daya alamnya sendiri yakni gandum dan air, setiap login random kan jumlah gandum dan air
2. user hanya dapat melakukan train tentara jika gandum dan air cukup
```
Imperian
gandum : 50
air : 100

Equites Cesairis
gandum : 150
air 200

swordman
gandum : 50
air : 45

Theutates Thunder
gandum : 50
air : 150

clubswinger
gandum: 65
air : 65

Teutonic Knight
gandum : 200
air : 200
```
jika sumber daya tidak cukup, maka input user ditolak. lakukan perhuitungan rekomendasi jumlah pasukan yang dapat
dilatih dengan sumber daya terbatas tersebut namun memiliki total attack optimal

3. buatkan laporan pertempuran yang telah terjadi (soal paling susah, jangan terpaku pada soal ini)

----
**lakukan git clone menggunakan https pada repository ini, untuk mengarahkan origin folder anda pada repo ini<br/> lalu buatlah branch anda sendiri dan lakukan pull request**
----
