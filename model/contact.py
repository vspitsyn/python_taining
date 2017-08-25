from sys import maxsize

class Contact:
    def __init__ (self,
                  firstname = None,
                  middlename = None,
                  lastname = None,
                  nickname = None,
                  title = None,
                  company = None,
                  company_address = None,
                  home_phone = None,
                  mobile_phone = None,
                  work_phone = None,
                  fax = None,
                  email1 = None,
                  email2 = None,
                  email3 = None,
                  homepage = None,
                  birth_day = None,
                  birth_month = None,
                  birth_year = None,
                  anniver_day = None,
                  anniver_month = None,
                  anniver_year = None,
                  home_address = None,
                  home_phone2 = None,
                  notes = None,
                  id=None,
                  hash = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.company_address = company_address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniver_day = anniver_day
        self.anniver_month = anniver_month
        self.anniver_year = anniver_year
        self.home_address = home_address
        self.home_phone2 = home_phone2
        self.notes = notes
        self.id = id

        def str_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string)

        #для строк, после которых следует перенос \n
        def strn_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string) +'\n'

        def hash_str(self):
            self.hash = str_or_no(self.lastname) + str_or_no(self.firstname) + str_or_no(self.company_address) + \
                        strn_or_no(self.email1)+ strn_or_no(self.email2)+ str_or_no(self.email3)+ \
                        strn_or_no(self.home_phone) + strn_or_no(self.mobile_phone) + strn_or_no(self.work_phone) + str_or_no(self.fax)


        if hash is None:
            hash_str(self)
            # self.hash = str_or_no(lastname) + str_or_no(firstname) + str_or_no(company_address) + \
            #             strn_or_no(email1)+ strn_or_no(email2)+ str_or_no(email3)+ \
            #             strn_or_no(home_phone) + strn_or_no(mobile_phone) + strn_or_no(work_phone) + str_or_no(fax)
        else:
            self.hash = hash

        # изменение полей объекта Contact
    def fill_contact_values(self, contact):
        def hash_str(self):
            self.hash = str_or_no(self.lastname) + str_or_no(self.firstname) + str_or_no(self.company_address) + \
                        strn_or_no(self.email1)+ strn_or_no(self.email2)+ str_or_no(self.email3)+ \
                        strn_or_no(self.home_phone) + strn_or_no(self.mobile_phone) + strn_or_no(self.work_phone) + str_or_no(self.fax)

        def str_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string)

        def strn_or_no(string):
            if (string is None) or (string == ""):
                return ""
            else:
                return str(string) +'\n'

        def fill_contact_value(a, b):
            if b is not None:
                return b
            else:
                return a

        self.firstname = fill_contact_value(self.firstname, contact.firstname)
        self.middlename = fill_contact_value(self.middlename, contact.middlename)
        self.lastname = fill_contact_value(self.lastname, contact.lastname)
        self.nickname = fill_contact_value(self.nickname, contact.nickname)
        self.title = fill_contact_value(self.title, contact.title)
        self.company = fill_contact_value(self.company, contact.company)
        self.company_address = fill_contact_value(self.company_address, contact.company_address)
        self.home_phone = fill_contact_value(self.home_phone, contact.home_phone)
        self.mobile_phone = fill_contact_value(self.mobile_phone, contact.mobile_phone)
        self.work_phone = fill_contact_value(self.work_phone, contact.work_phone)
        self.fax = fill_contact_value(self.fax, contact.fax)
        self.email1 = fill_contact_value(self.email1, contact.email1)
        self.email2 = fill_contact_value(self.email2, contact.email2)
        self.email3 = fill_contact_value(self.email3, contact.email3)
        self.homepage = fill_contact_value(self.homepage, contact.homepage)
        # Birthday date
        self.birth_day = fill_contact_value(self.birth_day, contact.birth_day)
        self.birth_month = fill_contact_value(self.birth_month, contact.birth_month)
        self.birth_year = fill_contact_value(self.birth_year, contact.birth_year)
        # Anniversary date
        self.anniver_day = fill_contact_value(self.anniver_day, contact.anniver_day)
        self.anniver_month = fill_contact_value(self.anniver_month, contact.anniver_month)
        self.anniver_year = fill_contact_value(self.anniver_year, contact.anniver_year)
        self.home_address = fill_contact_value(self.home_address, contact.home_address)
        self.home_phone2 = fill_contact_value(self.home_phone2, contact.home_phone2)
        self.notes = fill_contact_value(self.notes, contact.notes)
        hash_str(self)

    #метод, задающий ключ для сортировки списка объектов Контакт
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    # стандартный метод, определяющий вид вывода объекта на консоль
    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname + ' ' + self.firstname)

    # стандартный метод, определяющий правила сравнения объектов
    def __eq__(self, other):
        #return (self.id is None or other.id is None or self.id == other.id) and (self.hash == other.hash)
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname == other.lastname) \
               and (self.firstname == other.firstname)


