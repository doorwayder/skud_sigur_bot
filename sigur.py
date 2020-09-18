import pymysql.cursors
import time

class Person:

    def __init__(self, tab_param=None, id_param=None, name_param=None):
        if tab_param is not None:
            self.tab = tab_param
        else:
            self.tab = None
        if id_param is not None:
            self.id = id_param
        else:
            self.id = None
        if name_param is not None:
            self.name = name_param
        else:
            self.name = None
        self.zone = None
        self.hostname = '172.25.0.7'

    # def __del__(self):
    #     # TODO ...

    @property
    def person_zone(self):
        if self.id is None:
            if self.tab is None:
                print('Id or Tab is not initialized')
                return False
            else:
                self.id = self.person_id_by_tab

        connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                         db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        try:
             with connection.cursor() as cursor:
                sql = "SELECT NAME, LOCATIONZONE FROM Personal WHERE Id = {}".format(self.id)
                cursor.execute(sql)
        finally:
            connection.close()
        return cursor.fetchone()['LOCATIONZONE']

    @property
    def person_id_by_tab(self):
        connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                     db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                tab_str = str(self.tab)
                sql = 'SELECT Id FROM Personal WHERE TABID = "{}"'.format(tab_str.zfill(10))
                cursor.execute(sql)
        finally:
            connection.close()
        return cursor.fetchone()['Id']

    @property
    def person_zone_name(self):
        if self.person_zone == 1:
            return 'внутренняя территория'
        else:
            return 'внешняя территория'

    def init_person(self):
        if not (self.id or self.tab or self.name):
            print('Parameters Id, Tab or Name not defined')
            return False
        else:
            connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                         db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT NAME FROM Personal WHERE Id = {}".format(id)
                    cursor.execute(sql)


            finally:
                # Закрыть соединение (Close connection).
                connection.close()
            return cursor.fetchone()['NAME']


# TODO Методы получения фото, полной информации о Person, статистику