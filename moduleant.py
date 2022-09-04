import sqlite3

class antipublic:
    
    def input_file(input_txt): # Метод считывает файл и добавляет в массив кажду строку.
        with open(f"{input_txt}",'r') as inputs:
            input_massive = [i.rstrip() for i in inputs] 
        return input_massive
    
    def base_in_massive(database): # Метод сохраняет всю базу в массив.
        con = sqlite3.Connection(database)
        cur = con.cursor()
        cur.execute("SELECT * FROM base")
        actual_base = cur.fetchall()
        return actual_base  

    def check_public(database, input_massive): # Метод ищет совпадения из файла в БД, выводит массив уник. строк.
        con = sqlite3.Connection(database)
        cur = con.cursor()
        uniq_strs = []
        for i in input_massive:
            cur.execute(f"SELECT * FROM base WHERE obj == \'{i}\'")
            result = cur.fetchone()
            if result == None:
                uniq_strs.append(i)
            else:
                pass
        return uniq_strs
    
    def add_to_base(database, uniq_strs): # Метод добавляет уникальные строки в базу.
        con = sqlite3.Connection(database)
        cur = con.cursor()
        for i in uniq_strs:
            cur.execute(f"INSERT INTO base VALUES(\'{i}\')")
            con.commit()
        return True
    
    #########################ТУТ ВСЯКОЕ НЕНУЖНОЕ НО ПРИКОЛЬНОЕ
    
    def perc_of_uniq(uniq_strs, input_massive): ## Возвращает процент уника.
        perc = int(len(uniq_strs)/len(input_massive) * 100)
        return perc

    def base_info(database): # Метод выводит количество строк базы.
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS base (obj TEXT)")
        con.commit()
        cur.execute("SELECT * FROM base")
        actual_base_info = len(cur.fetchall())
        return actual_base_info 