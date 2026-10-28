#programa  apoyo familia
sexo=(input("dime tu sexo"))
edad=float(input("dime tu edad"))
estadocivil=(input("dime tu estado civil"))
canthijos=float(input("dime la cantidad de hijos que tienes"))
if sexo=="mujer" and canthijos==1 and edad>18:
    print("eres mujer tienes un hijo y eres menor de edad entonces el apoyo sera de $800")
elif sexo=="mujer" and canthijos>1 and edad>18:
    print("eres mujer tienes un hijo y eres mayor de edad entonces el apoyo sera de $300")
elif sexo=="mujer" and canthijos>1 and edad>18:
    print("eres mujer tienes mas de un hijo y eres maypor de edad entonces el apoyo es de $1500")
elif sexo=="hombre" and canthijos>=1 and estadocivil>="soltero":
    print("eres hombre y tienes hijos el apoyo es de $780")
else:
    print("no valido")