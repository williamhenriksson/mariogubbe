import math

# funktionen för addition
while True:
    def addition(numm1, numm2):
        summa = numm1 + numm2
        return summa

        # funktionen för subtraktion


    def subtraktion(numm1, numm2):
        differens = numm1 - numm2
        return differens

        # funktionen för multiplikation


    def multiplikation(numm1, numm2):
        produkt = numm1 * numm2
        return produkt

        # funktionen för division


    def division(numm1, numm2):
        if numm1 == 0:
            return "error"
        elif numm2 == 0:
            return "error"
        kvot = numm1 / numm2
        return kvot

        # funktionen för potenser


    def exponenter(numm1, numm2):
        if numm2 == 0:
            return "1"
        exponent = math.pow(numm1, numm2)
        return exponent

        # funktionen för roten ur


    def roten_ur(numm1):
        rot = math.sqrt(numm1)
        return rot

        # rester av division


    def beräkna_rest(numm1, numm2):
        rest = numm1 % numm2
        return rest

        # avrunda till heltal efter division


    def avrunda_heltal(numm1, numm2):
        avrunda = numm1 / numm2
        return avrunda


    # instruktioner för räknesätten
    def kalkylator():
            print("1. addition")
            print("2. subtraktion")
            print("3. multiplikation")
            print("4. division")
            print("5. exponenter")
            print("6. roten ur")
            print("7. rest")
            print("8. avrunda")
            user_input = input("välj operation")



                ## på funktionen för addition


            if user_input == "1":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                summa = addition(nummer1, nummer2)
                print(summa)

            # anrop på funktionen för subtraktion


            elif user_input == "2":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                differens = subtraktion(nummer1, nummer2)
                print(differens)

            # anrop på funktionen för multiplikation


            elif user_input == "3":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                produkt = multiplikation(nummer1, nummer2)
                print(produkt)

            # division
            # vad som händer när man skriver in att någon av siffrorna är noll i en division


            elif user_input == "4":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                if nummer1 == 0:
                    print("error")
                elif nummer2 == 0:
                    print("error")
                kvot = division(nummer1, nummer2)
                print(kvot)

            # det här är anropet på min funktion för potenser


            elif user_input == "5":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                exponent = math.pow(nummer1, nummer2)
                print(exponent)

            # anropet för min funktion för roten ur


            elif user_input == "6":
                nummer1 = float(input("välj nummer 1"))
                rot = math.sqrt(nummer1)
                print(rot)

            # få en rest efter division

            elif user_input == "7":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                rest = beräkna_rest(nummer1, nummer2)
                print(rest)

            # avrunda tal

            elif user_input == "8":
                nummer1 = float(input("välj nummer 1"))
                nummer2 = float(input("välj nummer 2"))
                avrunda = avrunda_heltal(nummer1, nummer2)
                print(avrunda)


# vad som händer om man väljer ett räknesätt som inte är med i min kod


            else:
                print("finns inget räknesätt på den siffran, välj 1, 2, 3, 4, 5 eller 6")

    # while loop, hur man kör igen
    print(kalkylator())
    choice = input("köra igen?")
    if choice.lower() != "ja":
        break
