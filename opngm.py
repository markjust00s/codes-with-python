import webbrowser
sifre=202093884
hak=5
deneme=int(input("Şifre giriniz: "))
if sifre==deneme:
    print("Giriş Başarılı ","Açılıyor...")
    webbrowser.open("itemsatis.com")
else:
    hak=hak-1
    print(hak,"Hakkınız Kaldı")
    if hak==0:
        print("Şifreniz Bloke Olmuştur")
    wait=input("Çıkmak için Enter'a basınız...")




