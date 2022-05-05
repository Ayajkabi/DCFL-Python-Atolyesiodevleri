import secrets
şifreler=[]

def oluştur():
    sifre_uzunluk  = 16
    A=(secrets.token_urlsafe(sifre_uzunluk))
    b=[]
    b.append(A)
    print(b)
for i in range(31) :
 şifreler.append(oluştur())