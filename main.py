from sigur import *

#person = Person(tab_no=2359)
person = Person()
if person.search_init('Булдакова'):
    print(person.name, person.id, person.tab)
    print(person.person_zone_name)
    print(person.person_zone_act)
    person.get_img_info()
