import ldap3
from ldap3 import Server, Connection, ALL
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
from ldap3 import *
import hashlib
from main import *
LDAP_SERVER_IP = '10.0.0.2'
LDAP_PASSWD = 'Testtest1234'
import mysql.connector
ad_server = Server(LDAP_SERVER_IP, get_info=ALL)
ad_conn = Connection(ad_server, user='bear\\usercreator', password=LDAP_PASSWD)
ad_conn.bind()
username = tp_name
l = last_name
f = one_name
city = gorod
data = pass_generate.passwd
hash = hashlib.md5(data.encode('utf-8'))
hash_print = hash.hexdigest()
print(hash_print)
def mantis_add_user():
    conn2 = mysql.connector.connect(host=host,
                                   database='mantis2',
                                   user=name,
                                   password=password)

    if conn2.is_connected():
        print('Коннектзаебись')
    mycursor = conn2.cursor()
    mycursorinsert = f"INSERT INTO mantis_user_table (username,realname,email,password,cookie_string) VALUES ('{tp_name}','{name_end}','123@123.ru','{hash_print}','{hash_print}');"
    mycursor.execute(mycursorinsert)
    conn2.commit()
    conn2.close()
def ad_create_user(lname, fname, city): #Создание учетки пользователя без паролей
    conn = mysql.connector.connect(host=host,
                                   database='mantis_bot_db',
                                   user=name,
                                   password=password)

    if conn.is_connected():
        print('Connected to MySQL database')
    mycursor = conn.cursor()



    if title == "Агент прямых продаж":
        jobspos = "Агент"
        variable_description = "КД, АПП, агент, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=NEW Агент прямых продаж,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Агент телефонных продаж":
        jobspos = "Телепродажи"
        variable_description = "КД, АТП, агент, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=NEW Агент прямых продаж,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local',
                  'CN=-dir3 Продажи ' + str(gorod) + ',OU=' + str(gorod) + ',OU=Продажи,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local', ]
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Монтажник подключения":
        jobspos = "Монтажник"
        variable_description = "ТР, монтажник подключения, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=installers,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Монтажник подключения,CN=Users,DC=bear,DC=local',
                  'CN=NEW Перемещение оборудования,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Монтажник связи/эксплуатации":
        jobspos = "Монтажник"
        variable_description = "ТР, монтажник связи, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=installers,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Монтажник подключения,CN=Users,DC=bear,DC=local',
                  'CN=NEW Перемещение оборудования,CN=Users,DC=bear,DC=local',
                  'CN=NEW Эксплуатация_сотрудник,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Выездной ИТП":
        jobspos = "Монтажник"
        variable_description = "ТР, Выездной ИТП, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=installers,CN=Users,DC=bear,DC=local',
                  'CN=NEW Выездной АТП,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Монтажник подключения,CN=Users,DC=bear,DC=local',
                  'CN=NEW Перемещение оборудования,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "2ЛТП":
        variable_description = "ИТП, инженер ТП, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=-dir2 Техподдержка,OU=Техподдержка,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Инженер техподдержки,CN=Users,DC=bear,DC=local',
                  'CN=operators,CN=Users,DC=bear,DC=local',
                  'CN=RADIUS,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local',
                  'CN=tacacsadmin,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=Общий доступ,CN=Users,DC=bear,DC=local',
                  'CN=Отдел Администрирования,CN=Users,DC=bear,DC=local',
                  'CN=Отдел Эксплуатации,CN=Users,DC=bear,DC=local']
    if title == "Супервайзер/РРТ":
        jobspos = "Супервайзер"
        variable_description = "КД, АТП, !супервайзер, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=boss,CN=Users,DC=bear,DC=local',
                  'CN=-dir3 Подбор персонала (HR),OU=Подбор персонала (HR),OU=!УК,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=-dir3 Продажи Кемерово,OU=Кемерово,OU=Продажи,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Супервайзер,CN=Users,DC=bear,DC=local',
                  'CN=operators,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Диспетчер":
        jobspos = "Диспетчер"
        variable_description = "КЦ, диспетчер, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=-dir2 Контакт центр,OU=Контакт центр,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=NEW Диспетчер филиала,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=operators,CN=Users,DC=bear,DC=local',
                  'CN=Общий доступ,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Оператор":
        jobspos = "Колл-центр"
        variable_description = "КЦ, оператор, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=-dir2 Контакт центр,OU=Контакт центр,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  #'CN=NEW Оператор,CN=Users,DC=bear,DC=local',
                  'CN=operators,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local',
                  'CN=Колл центр,CN=Users,DC=bear,DC=local',
                  'CN=Общий доступ,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == "Сварщик ВОЛС":
        jobspos = "Монтажник"
        variable_description = "ТР, сварщик ВОЛС, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=agents,CN=Users,DC=bear,DC=local',
                  'CN=NEW Агент прямых продаж,CN=Users,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  'CN=NEW Монтажник подключения,CN=Users,DC=bear,DC=local',
                  'CN=NEW Перемещение оборудования,CN=Users,DC=bear,DC=local',
                  'CN=NEW Эксплуатация_сотрудник,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','{gorod}');"
    if title == 'Менеджер по оттоку':
        jobspos = "Отток"
        variable_description = "КЦ, Менеджер по оттоку, " + gorod
        groups = ['CN=!!!' + str(gorod) + ',CN=Users,DC=bear,DC=local',
                  'CN=-dir2 Контакт центр,OU=Контакт центр,OU=Права NewFileshare,OU=Группы Доступа,DC=bear,DC=local',
                  'CN=NEW Годовой абонемент,CN=Users,DC=bear,DC=local',
                  #'CN=NEW Менеджер оттока,CN=Users,DC=bear,DC=local'
                  'CN=NEW Оператор,CN=Users,DC=bear,DC=local',
                  'CN=operators,CN=Users,DC=bear,DC=local',
                  'CN=rocketusers,CN=Users,DC=bear,DC=local',
                  'CN=Колл центр,CN=Users,DC=bear,DC=local',
                  'CN=Общий доступ,CN=Users,DC=bear,DC=local']
        insertQuary = f"INSERT INTO agents (name,position,department) VALUES ('{name_end}','{jobspos}','УК');"

    mycursor.execute(insertQuary)
    conn.commit()
    conn.close()
    dn_city = ('cn ='+ name_end + ',cn=Users,dc=bear,dc=local')
    print(dn_city)
    add_username_dn = ('cn=' + str(name_end) + ',ou=' + str(city) +',ou=Пользователи,ou=Сибирский медведь,dc=bear,dc=local')
    print("add_username_dn fullpath: ", add_username_dn)
    print("ad_conn.add result: ", ad_conn.add(
        add_username_dn,
        'user',
        {'sn': lname,  # фамилия
         'givenName': fname,  # имя
         'displayName': lname + ' ' + fname,  # cn\displayName
         'name': lname + ' ' + fname,  # имя
         'sAMAccountName': tp_name,  # имя
         'userPrincipalName': tp_name + '@bear.local',
         'userAccountControl': 544,
         'description': variable_description,
         'physicalDeliveryOfficeName': gorod + ', ' + title,
         'telephoneNumber': phone}))
    print(addUsersInGroups(ad_conn,add_username_dn,groups))
print(ad_create_user(l, f, city))
mantis_add_user()



