import mysql.connector
from model.group import Group
from model.contact import Contact
class DbFixture:
    #все контакты
    sel_all_cont = "select distinct a.id, a.firstname, a.middlename, a.lastname, a.nickname, a.address, " \
                   "a.email, a.email2, a.email3, a.home, a.mobile, a.work, a.phone2 " \
                   "from addressbook as a where a.deprecated = '0000-00-00 00:00:0'"

    #все контакты, состоящие хотя бы в одной группе
    sel_cont_in_groups = "select distinct a.id, a.firstname, a.middlename, a.lastname, a.nickname, a.address, " \
                         "a.email, a.email2, a.email3, a.home, a.mobile, a.work, a.phone2 " \
                         "from addressbook as a inner join address_in_groups on a.id = address_in_groups.id " \
                         "where a.deprecated = '0000-00-00 00:00:0'"

    # id контактов, состоящих хотя бы в одной группе
    sel_id_cont_in_groups = "select distinct a.id " \
                            "from addressbook as a inner join address_in_groups on a.id = address_in_groups.id " \
                            "where a.deprecated = '0000-00-00 00:00:0'"
    # id групп для контакта c id = s
    sel_id_groups_with_contacts = "select group_id from address_in_groups " \
                            "where id = %s"

    # id контактов, не состоящих ни в одной группе
    sel_cont_not_in_groups = sel_all_cont + " and a.id not in (" + sel_id_cont_in_groups + ")"

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_address_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor.fetchall():
                (contact_id, group_id) = row
                list.append([str(contact_id), str(group_id)])
        finally:
            cursor.close()
        return list

    #функция возвращает список контактов из произвольного запроса
    def get_contact_list_from_sel(self,sel):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(sel)
            for row in cursor.fetchall():
                (id, firstname, middlename, lastname, nickname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                    company_address=address, email1=email, email2=email2, email3=email3, home_phone=home, mobile_phone=mobile,
                                    work_phone=work,home_phone2=phone2))
        finally:
            cursor.close()
        return list

#все контакты
    def get_contact_list(self):
        return self.get_contact_list_from_sel(self.sel_all_cont)

# все контакты, состоящие в группах
    def get_contact_list_in_group(self):
        return self.get_contact_list_from_sel(self.sel_cont_in_groups)

# все контакты, не состоящие ни в каких группах
    def get_contact_list_not_in_group(self):
        return self.get_contact_list_from_sel(self.sel_cont_not_in_groups)

# id групп в которых состоит контакт
    def get_group_id_list_with_contact(self,id_contact):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where id = %s"%id_contact)
            for row in cursor.fetchall():
                #(group_id) = row
                list.append(str(row[0]))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
