from sigur import *

moa = Person(tab_no=1059)
if moa.init_data():
    print(moa.name, moa.id, moa.tab)
    print(moa.person_zone_name)
    moa.get_img_info()


