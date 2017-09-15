from model.group import Group
from model.contact import Contact


def clear_double_space(s):
    index_space = s.find('  ')
    if index_space > -1:
        s = clear_double_space(s[0:index_space] + s[index_space + 1:len(s)])
    return s

# def test_group_list(app,db):
#     ui_list = app.group.get_group_list()
#     #def clean(group):
#     #    return Group(id = group.id, name = clear_double_space(group.name).strip())
#     #db_list = map(clean, db.get_group_list())
#     db_list = map(app.group.clean_spaces, db.get_group_list())
#     assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = map(app.contact.clean_spaces, db.get_contact_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# from timeit import timeit
# def test_check_load_time(app,db):
#     print(timeit(lambda:app.group.get_group_list(), number=1))
#     print(timeit(lambda: db.get_group_list(), number=1000))
#     assert False