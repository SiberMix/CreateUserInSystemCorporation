import pymysql
from keepass.pykeepass import PyKeePass
import translit
import active_directory
import pass_generate
from config import *

from ldap3 import *
from ldap3.extend import ad_add_members_to_groups

ticket = int(input("Введи заявку: "))
#ticket = 2000254


def generate_account():
    print(name_end)
    print(tp_name)
    print(pass_generate.passwd)
    print(name_sokr2)
# -------------------------------------------------------
def keepass_register():
    # Инициализация базы паролей
    kp = PyKeePass('V:/!УК/IT/ИНФА/bear1.kdbx', password=kp_pass)
    group = kp.find_groups(name='Учетки домена', first=True)
    kp.add_entry(group, name_end, tp_name, pass_generate.passwd)
    kp.save()
    #kp.__exit__()

try:  # Проверка на коннект к базе+ данные
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=name,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Успешный коннект")
    # Функция выборки, с условием заявки.
    try:

        with connection.cursor() as cursor:
            #--------здесь берем номер заявки.--------
            select_custom = 'SELECT value FROM `mantis_custom_field_string_table`' \
                            f'WHERE bug_id = {ticket}  '
            cursor.execute(select_custom)
            row = cursor.fetchall()
            one_name = row[1].get('value')
            last_name = row[0].get('value')
            name_end = (row[0].get('value') + " " + row[1].get('value'))
            name_sokr = name_end.split()
            name_sokr2 = (name_sokr[0] + " " + "".join([s[0].upper() +"." for s in name_sokr[1:] ]))
            # Получение длины фамилии
            flsplit0 = len(name_end.split(' ')[0])
            tp_name = ((translit.transliterate((name_end[flsplit0 + 1:flsplit0 + 2] + '.' + name_end[0:flsplit0]),translit.ts).lower()))
            gorod = row[4].get('value')  # Город
            title = row[2].get("value")
            phone = row[3].get("value")
            generate_account()
            keepass_register()
    # Закрытие соединения после завершения
    finally:
        connection.close()

except Exception as ex:
    print("Ошибка в подключении базы/данная запись уже имеется")
