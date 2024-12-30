import random

mod=open('rolls.txt', 'r')
print("Witaj w programie do rzucania kostkami!")
powrot = 'T'



while powrot == 'T':
    
    leng=0
    suma = 0
    lista=[]
    leng=len(lista)

    while leng != 0:
        del lista[0]
        leng=len(lista())


    m=0
    powrot = 'T'


        
    print('''
Wybierz jedną z opcji poniżej:
1: Rzut D20 + modifier 
2: Zwykły rzut innymi koścmi
3: Rzut różnymi kośćmi naraz
4: Tabela modów
5: Szybki rzut D20
Aby wyjść z programu, wpisz '0' 
    ''')

    m=int(input("A więc która opcja? "))
        

    if m == 1:

        z = 0
        print("Wybrano kostke D20 ")
        a = int(input("Ile razy rzucać (1-300) "))
        rop=str(input("Na co rzucasz "))
        print("\n")
        
        if a <= 0:
            print("bitch?")
            break
        

        
        while a != 0:
            x = random.randint(1,20)
            


            linijka = mod.readlines()
            for linijki in linijka:
                z = z+1
                linijki.split()

                if rop == "str":
                    if z == 1:
                        
                        break

                elif rop == "dex":
                    if z == 2:
                        
                        break

                elif rop == "con":
                    if z == 3:
                      
                        break

                elif rop == "int":
                    if z == 4:
                       
                        break
                
                elif rop == "wis":
                    if z == 5:
                        
                        break
                
                elif rop == "cha":
                    if z == 6:
                        
                        break

            print("Wynik rzutu: ", x)
            print("\n")
            lista.append(x)
            suma = suma + x            
            
            a = a-1
        lista.sort()
        print("\nNajmniejszy element: ", lista[0])
        lista.sort(reverse=True)
        print("\nNajwiększy element: ", lista[0])
        print("\nSuma rzutów: ", suma)
        print("Modyfikator: ", linijki, "\n")
        
            

        print("\nWrócić do menu? ")
        powrot=str(input("T/N "))

    elif m == 2:

        y = int(input("Która kostka "))
        mf = int(input("Ile rzutów "))
        while mf > 0:
            
            x = random.randint(1,y)
            print("\nWynik rzutu: ", x)
            print("\n")
            lista.append(x)
            suma = suma + x            
            
            mf = mf -1

        lista.sort()
        print("Najmniejszy element: ", lista[0])
        lista.sort(reverse=True)
        print("Największy element: ", lista[0])
        print("\nSuma rzutów: ", suma)

        
        print("\nWrócić do menu? ")
        powrot=str(input("T/N "))

    elif m == 3:
        ile=int(input("Ile różnych kostek "))
        z = 0

        if ile <= 0:
            print("Bruh")
            break

        while ile > 0:
            
            poop=int(input("Która kostka "))
            kaka = int(input("Ile razy rzucać (1-300) "))
            print("wyniki rzutów: ")

            while kaka > 0:
                u = random.randint(1, poop)
                kaka = kaka -1
                print(u)
                suma = suma + u     

            ile = ile - 1 

        print("\nSuma rzutów: ", suma)

        
        print("\nWrócić do menu? ")
        powrot=str(input("T/N "))


    elif m == 4:
        print('''
str: Athletics
dex: Acrobatics | Sleight of hand | Stealth
con: :(
int: Arcana | History | Investigation | Nature | Religion
wis: Animal Handling | Insight | Medicine | Perception | Survival
cha: Deception | Intimidation | Performance | Persuasion
''')
        print("\nWrócić do menu? ")
        powrot=str(input("T/N "))

    elif m == 5:
        x = random.randint(1,20)
        print(x)
        print("\nWrócić do menu? ")
        powrot=str(input("T/N "))        

    else:
        break

print("Dziękuje za użycie programu! ")

                    
mod.close()


