alphabe={"A": "1", "B": "2", "C": "3", "Ç": "4", "D": "5", "E": "6", "F": "7", "G": "8", "H": "9", "Ğ": "10", "I": "11", "İ": "12", "J": "13", "K": "14", "L": "15", "M": "16", "N": "17", "O": "18", "Ö": "19", "P": "20", "R": "21", "S": "22", "Ş": "23", "T": "24", "U": "25", "Ü": "26", "V": "27", "Y": "28", "Z": "29"}
def hizalama(duz_kelimeler):
    def hizzala_yazdir(string, bos_liste, genislik, satir_poz):

        bosluk = " "
        bosluk_sayisi = genislik - len(string)
        try:
            araya_bosluk = str(bosluk) * int(bosluk_sayisi // (len(bos_liste) - 1))
            kalan_bosluk = str(bosluk) * int(bosluk_sayisi % (len(bos_liste) - 1))
            if bosluk_sayisi % (len(bos_liste) - 1) == 0:

                for index in range(len(bos_liste) - 1):
                    print(bos_liste[index], end="")
                    print(araya_bosluk, end="")
                print(bos_liste[index + 1])
            else:
                if satir_poz % 2 == 0:

                    for index in range(len(bos_liste) - 1):
                        print(bos_liste[index], end="")
                        print(araya_bosluk, end="")
                    print(kalan_bosluk, bos_liste[index + 1], sep="")
                else:

                    print(bos_liste[0], kalan_bosluk, araya_bosluk, end="", sep="")
                    for index in range(1, len(bos_liste) - 1):
                        print(bos_liste[index], end="")
                        print(araya_bosluk, end="")
                    print(bos_liste[index + 1])
        except ZeroDivisionError:
            son_bosluk=bosluk*(genislik-len(string))
            print(bos_liste[0],son_bosluk)

    while True:
        genislik=satir_sayisi()
        if genislik==0:
            break
        satir_poz = 1
        start_pos = 0
        while True:
            bosluk = " "
            bos_liste = []
            string = ""
            for i in range(start_pos, len(duz_kelimeler)):
                if len(bos_liste) <= 1:
                    carpim_durumu = 1
                else:
                    carpim_durumu = len(bos_liste) - 1

                if len(string + bosluk * carpim_durumu) >= genislik:
                    durum = 0
                    if len(string + bosluk * carpim_durumu) > genislik:
                        durum = -1
                        bos_liste.pop(len(bos_liste) - 1)
                        son_string = ""
                        for nene in bos_liste:
                            son_string += str(nene)
                        string = son_string
                    hizzala_yazdir(string, bos_liste, genislik, satir_poz)

                    start_pos = i + durum
                    satir_poz += 1
                    bos_liste.clear()
                    break
                else:

                    bos_liste.append(duz_kelimeler[i])
                    string += str(duz_kelimeler[i])
            if i == len(duz_kelimeler) - 1:
                if len(bos_liste) == 0:
                    bos_liste.append(duz_kelimeler[i])
                if len(string + bosluk * (len(bos_liste)-1)) > genislik:
                    son_item = bos_liste[len(bos_liste) - 1]
                    bos_liste.pop(len(bos_liste) - 1)
                    son_string = ""
                    for y in bos_liste:
                        son_string += str(y)
                    string = son_string
                    hizzala_yazdir(string, bos_liste, genislik, satir_poz)
                    print(son_item)
                else:
                    if len(bos_liste) > 1:
                        for t in range(len(bos_liste) - 1):
                            print(bos_liste[t], end=" ")
                        print(bos_liste[len(bos_liste) - 1])
                    else:
                        print(bos_liste[0])
                break

def iki_listeyi_birlestir(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i][0] == arr2[j][0]:
                arr2[j][1] += arr1[i][1]
                break

        else:
            arr2.append(arr1[i])


def satir_sayisi():
    while True:
        try:
            satir_sayi_al=int(input("Lütfen satır genişliğini giriniz, eğer girmek istemiyorsanız 0'a basınız!: "))
            if satir_sayi_al >= 0:
                break
            else:
                print("Hatalı giriş, ",end="")
        except ValueError:
            print("Hatalı giriş, ",end="")
    return satir_sayi_al


def tek_problem_i(liste):
    gecici_liste=[]
    for kelime in liste:
        yedek_string=""
        for index in range(len(kelime)):
            if "i" == kelime[index]:
                yedek_string +="İ"
            else:
                yedek_string += kelime[index].upper()

        gecici_liste.append(yedek_string)
    return    gecici_liste


def listeyi_diz(arr,dict,index):
    def harf_harf_kiyaslama(item1, item2, dict):  ## olursa item 1 < item 2 durum false
        uzunluk1 = len(item1)
        uzunluk2 = len(item2)
        if uzunluk2 > uzunluk1:
            uzunluk = uzunluk1
            durum = False
        else:
            uzunluk = uzunluk2
            durum = True
        for i in range(uzunluk):
            harf_notu1 = int(dict[item1[i]])
            harf_notu2 = int(dict[item2[i]])
            if harf_notu1 > harf_notu2:
                durum = True
                break
            elif harf_notu1 < harf_notu2:
                durum = False
                break
        return durum



    def sayiya_gore_kiyaslama(item1, item2):
        if item1 < item2:
            durum = True
        else:
            durum = False
        return durum

    for i in range(len(arr)):

        minimum = i

        for j in range(i + 1, len(arr)):
            if index == 0:
                durum = harf_harf_kiyaslama(arr[minimum][index], arr[j][index], dict)
            else:
                durum = sayiya_gore_kiyaslama(arr[minimum][index], arr[j][index])

            if durum==True:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]



def kucuk_duzeltme(arr):
    bos_liste=[]
    gecici_liste=[]
    try:
        for i in range(len(arr)):
            if arr[i] not in bos_liste:
                gecici_liste.append(arr[i])
                for j in range(i+1,len(arr)):
                    if arr[i][1]==arr[j][1]:
                        gecici_liste.append(arr[j])
                listeyi_diz(gecici_liste,alphabe,0)
                bos_liste+=gecici_liste
                gecici_liste=[]
        return bos_liste
    except IndexError as err:
        print(err)



def islem_merkezi(paragraf, kullanicak_liste):
    kelime = ""

    for harf in paragraf:
        if harf != " ":
            kelime += harf
        else:
            kullanicak_liste.append(kelime)
            kelime = ""
    kullanicak_liste.append(kelime)


def yazdir(listem,listem2):
    print("Kelime                   Tekrar Sayısı      |       Kelime                   Tekrar Sayısı")
    print("------                   -------------      |       ------                   -------------")
    for i in range(len(listem)):
        print(format(listem[i][0],"<20"),end="         ")
        print(format(listem[i][1],"<5"),end="          |       ")
        print(format(listem2[i][0],"<20"),end="         ")
        print(format(listem2[i][1],"<5"))


def konum_yazdir(arr,alphabe):
    konum_matrisi=[]
    for keys in alphabe.keys():
        gecici_liste=[0]*21
        gecici_liste[0]=keys
        konum_matrisi.append(gecici_liste)
    for item in arr:
        stirng=str(item[0])

        for harfin_adi in range(len(stirng)):
            konum_matrisi[int(alphabe[stirng[harfin_adi]])-1][harfin_adi+1]+=1
    print("    ","Kelimelerin konumları")
    print("Harf",end=" ")
    for i in range(1,21):
        print(format(i,"3"),end=" ")
    print("Toplam")
    print("----",end=" ")
    for i in range(1,21):
        print(format("---","3"),end=" ")
    print("------")
    for harf in range(29):
        satir_toplam=0
        print(format(konum_matrisi[harf][0],"<4"),end=" ")
        for konum in range(1,21):
            print(format(konum_matrisi[harf][konum], "3"), end=" ")
            satir_toplam+=konum_matrisi[harf][konum]
        print(format(satir_toplam,"6"))



def iki_boyutlu_liste():
    metin=open("harf_uzayi.txt","r",encoding="utf8")
    karakter_matrisi=[]
    liste_liste=[]
    bos_liste=[]
    for matir in range(50):
        liste_liste.append(metin.readline())
    for item in liste_liste:
        for j in range(50):
            bos_liste.append(item[j])
        yardimci_liste=bos_liste[:]
        bos_liste.clear()
        karakter_matrisi.append(yardimci_liste)
    metin.close()
    return karakter_matrisi



yonler=[["Kuzeybatı",-1,-1],["Kuzey",-1,0],["Kuzeydoğu",-1,1],["Doğu",0,1],["Güneydoğu",1,1],["Güney",+1,0],["Güneybatı",+1,-1],["Batı",0,-1]]

def uzayda_kelime_ara(item,karakter_matrisi,yonler):
    def yone_gore(x, y, yon, item, karakter_matrisi, a, yonler):
        x += yonler[yon][1]
        y += yonler[yon][2]

        try:
            if karakter_matrisi[x][y] == item[a]:

                durum = yone_gore(x, y, yon, item, karakter_matrisi, a + 1, yonler)
            else:
                return False
        except IndexError:
            if len(item) == a:
                return True
            else:
                return False
        return durum

    bulunanlar=[]
    uzunluk=len(item)
    for satir in range(50):
        for sutun in range(50):
            if karakter_matrisi[satir][sutun] == item[0]:
                #8 yon

                for yon in range(8):
                    a=yone_gore(satir,sutun,yon,item,karakter_matrisi,1,yonler)
                    if a == True:
                        bulunanlar.append([item,satir+1,sutun+1,yonler[yon][0]])


    return bulunanlar


tum_kelimeler=[]

def main():
    while True:
        ikid_liste = []
        kelimeler = []
        duz_kelimeler = []
        buyuk_kelimeler = []

        paragraf = input("Paragrafı giriniz : ")
        islem_merkezi(paragraf, duz_kelimeler)

        gecici_liste=tek_problem_i(duz_kelimeler)
        hizalama(gecici_liste)
        for kelime in gecici_liste:
            if kelime not in buyuk_kelimeler:
                buyuk_kelimeler.append(kelime)
                ikid_liste.append([kelime,gecici_liste.count(kelime)])
        iki_listeyi_birlestir(ikid_liste,tum_kelimeler)
        soldaki_liste=ikid_liste[:]
        sagdaki_liste=ikid_liste[:]
        listeyi_diz(soldaki_liste,alphabe,0)
        listeyi_diz(sagdaki_liste,alphabe,1)
        bos_liste=kucuk_duzeltme(sagdaki_liste)
        sagdaki_liste=bos_liste.copy()
        yazdir(soldaki_liste,sagdaki_liste)

        while True :
            devam = input("Girmek istediğiniz başka bir paragraf var mı ?(E/e/H/h)")
            if devam in ["e", "E","h","H"]:
                break
        if devam in ["h","H"]:
            break
main()
tum_kelimeler_sol=tum_kelimeler[:]
tum_kelimeler_sag=tum_kelimeler[:]
listeyi_diz(tum_kelimeler_sag,alphabe,1)
listeyi_diz(tum_kelimeler_sol,alphabe,0)
bos_liste=kucuk_duzeltme(tum_kelimeler_sag)
tum_kelimeler_sag=bos_liste.copy()
print("paragraflardaki tüm kelimeler yazdırılıyor")
yazdir(tum_kelimeler_sol,tum_kelimeler_sag)
konum_yazdir(tum_kelimeler,alphabe)
karakter_matrisi = iki_boyutlu_liste()


yazdirilcak=[]
for indexi in range(len(tum_kelimeler_sol)):

    bulunan= uzayda_kelime_ara(str(tum_kelimeler_sol[indexi][0]), karakter_matrisi, yonler)

    if len(bulunan)==0:
        bulunan.append([tum_kelimeler_sol[indexi][0],"---Bulunamadı---"])
    simdilik=bulunan[:]
    for liss in simdilik:
        yazdirilcak.append(liss)
    bulunan.clear()
print(format("Kelime","<20"),end=" ")
print("Satır No","Sütun No",end=" ")
print("Yönü")
print("-------------------- -------- -------- ---------")
for index1 in range(len(yazdirilcak)):
    if len(yazdirilcak[index1])==2:
        print(format(yazdirilcak[index1][0], "<20"), end="        ")
        print(yazdirilcak[index1][1])
    else:
        print(format(yazdirilcak[index1][0],"<20"),end=" ")
        print(format(yazdirilcak[index1][1],"6"),end="   ")
        print(format(yazdirilcak[index1][2],"6"),end="   ")
        print(format(yazdirilcak[index1][3],"9"))



