import json
from moduleant import antipublic
import sqlite3
import re
    
def Choose_mode(): #1 - Проверка на паблик. 2- выгрузить базу в txt. 
    print("1. Проверка базы\n2. Выгрузить базу в txt.")
    Answer = int(input())
    return Answer

def Start_antipublic(database):
    
    print('Всего строк в базе: ' + str(antipublic.base_info(database)))
    InputFile = input()
    InputFile= re.sub(r'["]','', InputFile)
    inputmassive = antipublic.input_file(input_txt=InputFile.strip())
    uniq_strs = antipublic.check_public(database,inputmassive)
    perc_of_unic = antipublic.perc_of_uniq(uniq_strs,inputmassive)
    print("Процент уникальных строк: " + str(perc_of_unic))
    if perc_of_unic == 0:
        print("К сожалению, добавлять нечего.")
    else:
        print("Хочешь добавить данные в БД? Д/н")
        answer = input()
        if answer == "Д" or answer == "д":
            sas = antipublic.add_to_base(database,uniq_strs)
            print(sas)
        elif answer == "н" or answer == "Н":
            print("Окей. Работа завершается.")
        else:
            print("Ты че блять, тебе не понятно? Д или Н нахуй, Д БЛЯТЬ ИЛИ Н")

def Print_base(database):
    massive = antipublic.base_in_massive(database)
    with open ("Actual_base.txt", "w") as file:
        for i in massive:
            file.write("\n".join(i)+"\n")
def main():
    database = "database.db"
    ans = Choose_mode()
    if ans == 1:
        Start_antipublic(database)
    elif ans == 2:
        Print_base(database)
    else:
        print("s")











if __name__ == "__main__":
    main()