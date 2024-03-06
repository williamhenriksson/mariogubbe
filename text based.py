import time

# Här öppnas alla filer för de olika rummen och blir lästa
with open("textspel.txt", 'r', encoding='utf-8') as Hall:
    hall_text = Hall.readlines()
with open("Köket.txt", 'r', encoding='utf-8') as Kok:
    kok_text = Kok.readlines()
with open("Badrum.txt", 'r', encoding='utf-8') as Bad:
    bad_text = Bad.readlines()
with open("Sovrum.txt", 'r', encoding='utf-8') as Sov:
    sov_text = Sov.readlines()
with open("Förråd.txt", 'r', encoding='utf-8') as For:
    for_text = For.readlines()
with open("Vardagsrum.txt", 'r', encoding='utf-8') as Var:
    var_text = Var.readlines()
with open("savefile.txt", "r") as save_file:
    save_file_text = save_file.readlines()

# koordinater för alla rum (koordinater, Diyar)
Hallen = 0, 0
Badrum = 0, 1
Vardagsrum = 1, 0
Koket = -1, 0
Forrad = 1, 1
Sovrum = 2, 1

# start koordinater
Cordx = 0
Cordy = 0


# funktion för vad player_cords är för något
def player_cords():
    return Cordx, Cordy


# funktionerna för rummen som gör att den printar rätt textfil till de olika rummen beroende på en spelares koordinater
def printa_text_hallen():
    if player_cords() == Hallen:
        for i in hall_text:
            time.sleep(1)
            print(i.strip())


def printa_text_badrum():
    if player_cords() == Badrum:
        for i in bad_text:
            time.sleep(1)
            print(i.strip())


def printa_text_vardags():
    if player_cords() == Vardagsrum:
        for i in var_text:
            time.sleep(1)
            print(i.strip())


def printa_text_koket():
    if player_cords() == Koket:
        for i in kok_text:
            time.sleep(1)
            print(i.strip())


def printa_text_forrad():
    if player_cords() == Forrad:
        for i in for_text:
            time.sleep(1)
            print(i.strip())


def printa_text_sovrum():
    if player_cords() == Sovrum:
        for i in sov_text:
            time.sleep(1)
            print(i.strip())


# funktion som gör att den printar rätt text vid rädd rum
def printa_current_rum_text():
    if player_cords() == Sovrum:
        printa_text_sovrum()
    elif player_cords() == Badrum:
        printa_text_badrum()
    elif player_cords() == Vardagsrum:
        printa_text_vardags()
    elif player_cords() == Koket:
        printa_text_koket()
    elif player_cords() == Forrad:
        printa_text_forrad()
    elif player_cords() == Hallen:
        printa_text_hallen()
    else:
        print("Du hittade en gömd passage fortsätt gå för att se vart den leder")


def save_game(printa_current_room_text):
    game_state = {"printa_current_room_text": printa_current_room_text}
    with open("savefile.txt", "w") as save_file:
        save_file.write(str(game_state))


# while loop för att spelet ska kunna köras mer
while True:
    # anropar funktionen för att printa texten tilldelad till rummet
    printa_current_rum_text()
    # hur man rör sig i spelet (från Diyar)
    Direction = str(input("Vilket håll vill du gå i?""W = Fram, A = Vänster, S = Bak, D = Höger"))
    if Direction == "w" or Direction == "W" or Direction == "Fram" or Direction == "fram":
        Cordy = Cordy + 1
    elif Direction == "a" or Direction == "A" or Direction == "Vänster" or Direction == "vänster":
        Cordx = Cordx - 1
    elif Direction == "s" or Direction == "S" or Direction == "Bak" or Direction == "bak":
        Cordy = Cordy - 1
    elif Direction == "d" or Direction == "D" or Direction == "Höger" or Direction == "höger":
        Cordx = Cordx + 1
    else:
        print("Du hittade en gömd passage fortsätt gå för att se var den leder.")

    print(printa_current_rum_text())

    # Hur man fortsätter spela (Diyar)
    play_more = str(input("Vill du utforska fler rum?(Ja/Nej)").lower())
    if play_more == "Ja".lower():
        Direction = str(input("Vilket håll vill du gå i?""W = Fram, A = Vänster, S = Bak, D = Höger"))
        if Direction == "w" or Direction == "W" or Direction == "Fram" or Direction == "fram":
            Cordy = Cordy + 1
        elif Direction == "a" or Direction == "A" or Direction == "Vänster" or Direction == "vänster":
            Cordx = Cordx - 1
        elif Direction == "s" or Direction == "S" or Direction == "Bak" or Direction == "bak":
            Cordy = Cordy - 1
        elif Direction == "d" or Direction == "D" or Direction == "Höger" or Direction == "höger":
            Cordx = Cordx + 1
        else:
            print("Du hittade en gömd passage fortsätt gå för att se var den leder.")
            print(printa_current_rum_text())
    else:
        break

    save_input = input("vill du spara spelet? (ja eller nej):")
    input(save_input)
    if save_input.lower() == "ja":
        save_game(printa_current_rum_text())
    else:
        print("Du har valt att inte spara")
