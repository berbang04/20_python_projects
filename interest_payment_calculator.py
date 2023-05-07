print("welcome to çiftlik bank hadi kredi çekelim mk")
tür=str(input("Lütfen kredi türünü yazin: "))
kredi=int(input("Lütfen kredi tuttarını yazin: "))
vade=int(input("Lütfen kredi vadesini  yazin(ay olarak,maks 24): "))
if tür== "tasit":
    print("tasit kredisi faizi yüzde 3 tür.")
    if vade>24:
        print("o kadar vade yok ne yazık ki")
    else:
        if vade<=12:
            ödenecek=kredi*((3*vade)/100)+kredi
            print("krediniz: ",kredi)
            print("ödenecek tutar: ",ödenecek)
        else:
            ödenecek=kredi*0.36 +kredi 
            vade=vade-12
            if vade<=12:
                ödenecek=ödenecek*((3*vade)/100)+ödenecek
                print("krediniz: ",kredi)
                print("ödenecek tutar: ",ödenecek)
            else:
                print("siktir git lan nerde buldun bu kadar vade")    

elif tür=="konut":
    print("konut kredisi faizi yüzde 5 tür.")
    if vade>24:
        print("o kadar vade yok ne yazık ki")
    else:
        if vade<=12:
            ödenecek=kredi*((5*vade)/100)+kredi
            print("krediniz: ",kredi)
            print("ödenecek tutar: ",ödenecek)
        else:
            ödenecek=kredi*0.6 +kredi 
            vade=vade-12
            if vade<=12:
                ödenecek=ödenecek*((5*vade)/100)+ödenecek
                print("krediniz: ",kredi)
                print("ödenecek tutar: ",ödenecek)
            else:
                print("siktir git lan nerde buldun bu kadar vade")

                


