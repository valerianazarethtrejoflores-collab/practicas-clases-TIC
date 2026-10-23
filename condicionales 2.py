#Programa que me indica como me fue en calificaciones
calif=float(input("Dame tu calif"))
if calif==10:
    print("Excelenteee")
elif calif==9:
    print("muy bien")
elif calif==8:
    print("muy bien")
elif calif==7:
    print("puedes mejorar")
elif calif==6:
    print("ay mijo")
else:
    print("chanclazooo")


#Solicitar temperatura
temp=float(input("Dame la temp"))
if temp>40:
    print("Hace mucho< calor")
elif temp==30 and temp<40:
    print("Esta templadito")
elif temp==20 and temp<30:
    print("Esta fresco")
elif temp<=10:
    print("Hace frio")


#Programa para sacar cartilla militar
sexo=(input("dime tu sexo"))
edad=int(input("dime tu edad"))
if sexo=="hombre" and edad>=18:
    print("puedes sacar tu cartilla militar")
else:
    print("no puedes")
    
