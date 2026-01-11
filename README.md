# hesap-makinesi

Basit bir Python hesap makinesi.

Çalıştırmak için repo kökünde bulunan `hesap.py` dosyasını kullanabilirsiniz.

Örnek kullanım:

```bash
python3 hesap.py
```

Kod (örnek):

```python
print("hoşgeldiniz")
sayi1=int(input("ilk sayıyı giriniz"))
sayi2=int(input("2. sayıyı giriniz"))
islem=(input("hangi işelm olsun (çarpma,bölme,toplama,çıkarma)"))
if islem=="çarpma":
    print("sonuç=",sayi1*sayi2)
elif islem=="bölme":
    print("sonuc=",sayi1/sayi2)
elif islem=="toplama":
    print("sonuc=",sayi1+sayi2)
elif islem=="çıkarma":
    print("sonuc=",sayi1-sayi2)
else:
    print("geçersiz işlem girdiniz")
```
