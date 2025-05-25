import sqlite3


class DbCommands:
    def __init__(self):
        pass

    def impulse(self):
        self.conn_users = sqlite3.connect('db.sqlite3')
        self.c = self.conn_users.cursor()

        #

    def create_main_db(self):
        self.impulse()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "operator" (
                "key_operator"	INTEGER NOT NULL UNIQUE,
                "name_operator"	TEXT,
                PRIMARY KEY("key_operator" AUTOINCREMENT)
               );''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS ispolnitel
                          (
                              key_ispolnitel INTEGER NOT NULL UNIQUE,
                              ispolnitel_name TEXT,
                              PRIMARY KEY (key_ispolnitel AUTOINCREMENT)
                          );''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS zakazchik
                          (
                              key_zakazchik  INTEGER NOT NULL UNIQUE,
                              zakazchik_name TEXT,
                              PRIMARY KEY (key_zakazchik AUTOINCREMENT)
                          );''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS user (
                    key_user INTEGER NOT NULL UNIQUE,
                    fio_user TEXT,
                    phone TEXT,
                    email TEXT,
                    dolznost TEXT,
                    key_ispolnitel INTEGER,
                    FOREIGN KEY (key_ispolnitel) REFERENCES ispolnitel(key_ispolnitel),
                    PRIMARY KEY(key_user AUTOINCREMENT)
                );''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS call
                          (
                              key_call        INTEGER NOT NULL UNIQUE,
                              key_operator    INTEGER,
                              key_user        INTEGER,
                              key_firm        INTEGER,
                              key_zakazchik   INTEGER,
                              start_date_call TEXT DEFAULT (datetime('now', 'localtime')),
                              end_date_call   TEXT DEFAULT (datetime('now', 'localtime')),
                              dlitelnost_call  TEXT,
                              theme           TEXT,
                              naim_ps         TEXT,
                              opis_ps         TEXT,
                              comment         TEXT,
                              FOREIGN KEY (key_operator) REFERENCES operator (key_operator),
                              FOREIGN KEY (key_user) REFERENCES user (key_user),
                              FOREIGN KEY (key_firm) REFERENCES ispolnitel (key_ispolnitel),
                              FOREIGN KEY (key_zakazchik) REFERENCES zakazchik (key_zakazchik),
                              PRIMARY KEY (key_call AUTOINCREMENT)
                          );''')



        self.conn_users.commit()
        self.conn_users.close()

    def insert_operators(self, operator_name):
        self.impulse()
        self.c.execute('''
                           INSERT INTO operator(name_operator)
                           VALUES (?)''', (operator_name,))
        self.conn_users.commit()
        self.conn_users.close()

    def select_db_info(self, sql_request):
        self.impulse()
        self.c.execute(sql_request)

        rows = self.c.fetchall()
        self.conn_users.close()
        return rows


# def add_all_po(self, name, category):
#     self.c.execute('''SELECT * FROM all_po WHERE name_all_po = ?''', (name,))
#     ret = self.c.fetchall()
#     if len(ret) == 0:
#         self.c.execute('''
#                    INSERT INTO all_po(name_all_po,category_all_po)
#                    VALUES (?,?)''', (name, category,))
#         self.conn_users.commit()
#
#
# def select_db_info(sql_request):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#
#     cursor.execute(sql_request)
#
#     rows = cursor.fetchall()
#     conn.close()
#     return rows
#
#
# def insert_sfo(class_id: int, sfo_description, sfo_name, sfo_number):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     sql_script = f'INSERT INTO catapp_sfovvst (class_vvst_id, sfo_description, sfo_name, sfo_number) VALUES ({class_id}, "{sfo_description}", "{sfo_name}", "{sfo_number}");'
#     print(sql_script)
#     cursor.execute(sql_script)
#
#     conn.commit()
#     conn.close()
#
#
# def insert_nops(nops_description, nops_name, nops_number, sfo_vvst_id: int):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     sql_script = f'INSERT INTO catapp_nopsvvst (nops_description, nops_name, nops_number, sfo_vvst_id) VALUES ("{nops_description}", "{nops_name}", "{nops_number}", {sfo_vvst_id});'
#     print(sql_script)
#     cursor.execute(sql_script)
#
#     conn.commit()
#     conn.close()


# def delete_from_db():
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM catapp_predmetsnabzeniavvst")
#     # cursor.execute("DELETE FROM catapp_okpo")
#     # cursor.execute("DELETE FROM catapp_okato")
#     # cursor.execute("DELETE FROM catapp_nopsvvst")
#     # cursor.execute("DELETE FROM catapp_sfovvst")
#
#     conn.commit()
#     conn.close()
#
#
# def insert_okato(code_okato, control_num_okato, name_okato, description_okato):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     sql_script = f'INSERT INTO catapp_okato (code_okato, control_num_okato, name_okato, description_okato) VALUES ("{code_okato}", "{control_num_okato}", "{name_okato}", "{description_okato}");'
#     print(sql_script)
#     cursor.execute(sql_script)
#
#     conn.commit()
#     conn.close()
#
#
# def insert_okpo(region_okpo, code_okpo, name_org_okpo, inn_okpo, ogrn_okpo, okogu_okpo, okato_okpo, oktmo_okpo,
#                 okfs_okpo, okopf_okpo):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     sql_script = f"INSERT INTO catapp_okpo (region_okpo, code_okpo, name_org_okpo, inn_okpo, ogrn_okpo, okogu_okpo, okato_okpo, oktmo_okpo, okfs_okpo, okopf_okpo) VALUES ('{region_okpo}', '{code_okpo}', '{name_org_okpo}', '{inn_okpo}', '{ogrn_okpo}', '{okogu_okpo}', '{okato_okpo}', '{oktmo_okpo}', '{okfs_okpo}', '{okopf_okpo}');"
#     print(sql_script)
#     cursor.execute(sql_script)
#
#     conn.commit()
#     conn.close()
#
#
# def insert_predmetsnabz(nops_id_vvst, predmet_inn, predmet_name, predmet_oboznachenie, predmet_status, format_vvst_id):
#     conn = sqlite3.connect('../db.sqlite3')
#     cursor = conn.cursor()
#     sql_script = f"INSERT INTO catapp_predmetsnabzeniavvst (nops_vvst_id, predmet_inn, predmet_name, predmet_oboznachenie, predmet_status, format_vvst_id) VALUES ({nops_id_vvst}, '{predmet_inn}', '{predmet_name}', '{predmet_oboznachenie}', '{predmet_status}', {format_vvst_id});"
#     print(sql_script)
#     cursor.execute(sql_script)
#
#     conn.commit()
#     conn.close()


if __name__ == "__main__":
    new_db = DbCommands()
    new_db.create_main_db()
    new_db.insert_operators('Леонова Оксана Александровна')
    new_db.insert_operators('Федосов Антон Станиславович')
    new_db.insert_operators('Индюхов Кирилл Александрович')
    operators = new_db.select_db_info('SELECT name_operator FROM operator')
    print(*operators)
