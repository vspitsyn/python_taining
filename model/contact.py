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
            if string is None:
                return "no"
            else:
                return str(string)

        if hash is None:
            self.hash = str_or_no(lastname) + str_or_no(firstname) + str_or_no(company_address) + \
                        str_or_no(email1) +'\n'+ str_or_no(email2) +'\n'+ str_or_no(email3)+ \
                        str_or_no(home_phone) +'\n'+ str_or_no(mobile_phone) +'\n'+ str_or_no(work_phone) +'\n'+ str_or_no(fax)
        else:
            self.hash = hash

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
        return (self.id is None or other.id is None or self.id == other.id) and (self.hash == other.hash)
#        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname + ' ' + self.firstname) == \
#                                                                                (other.lastname + ' ' + other.firstname)


