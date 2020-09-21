import pymysql.cursors
from PIL import Image, ImageDraw, ImageFont
import io

class Person:

    def __init__(self, tab_no=None, id_no=None, person_name=None):
        if tab_no is not None:
            self.tab = tab_no
        else:
            self.tab = None
        if id_no is not None:
            self.id = id_no
        else:
            self.id = None
        if person_name is not None:
            self.name = person_name
        else:
            self.name = None
        self.hostname = 'skudsrv'
        self.initialized = False

    # def __del__(self):
    #     # TODO ...

    @property
    def person_zone(self):
        if self.initialized:
            connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                             db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            try:
                 with connection.cursor() as cursor:
                    sql = "SELECT NAME, LOCATIONZONE FROM Personal WHERE Id = {}".format(self.id)
                    cursor.execute(sql)
            finally:
                connection.close()
            return cursor.fetchone()['LOCATIONZONE']
        else:
            print('Person is not initialized')
            return False

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
        if self.initialized:
            if self.person_zone == 1:
                return 'внутренняя территория'
            else:
                return 'внешняя территория'
        else:
            return False

    def init_data(self):
        if not (self.id or self.tab or self.name):
            print('Parameters Id, Tab or Name not defined')
            return False
        else:
            connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                         db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

            if self.id is not None:
                sql = "SELECT Id, TABID, NAME FROM Personal WHERE Id = {}".format(self.id)
            else:
                if self.tab is not None:
                    sql = "SELECT Id, TABID, NAME FROM Personal WHERE TABID = {}".format(self.tab)
                else:
                    if self.name is not None:
                        sql = "SELECT Id, TABID, NAME FROM Personal WHERE NAME = {}".format(self.name)
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            finally:
                connection.close()
            if result:
                self.id = result[0]['Id']
                self.tab = int(result[0]['TABID'])
                self.name = result[0]['NAME']
                self.initialized = True
                return True
            else:
                self.initialized = False
                print('Person not defined')
                return False

    def get_person_photo(self):
        if self.initialized:
            connection = pymysql.connect(host=self.hostname, port=3305, user='root', password='spnx32_0',
                                         db='tc-db-main', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT HIRES_RASTER FROM photo WHERE ID = {}".format(self.id)
                    cursor.execute(sql)

            finally:
                # Закрыть соединение (Close connection).
                connection.close()
            return cursor.fetchone()['HIRES_RASTER']
        else:
            print('Person is not initialized')
            return False

    def get_img_info(self):
        if self.initialized:
            photo = Image.open(io.BytesIO(self.get_person_photo()))
            draw_text = ImageDraw.Draw(photo)
            font = ImageFont.truetype('c:/Windows/Fonts/arial.ttf ', size=16)
            draw_text.text((5, 5), self.name, font=font, fill=('#1C0606'))
            draw_text.text((5, 20), str(self.tab), font=font, fill=('#1C0606'))
            draw_text.text((5, 35), self.person_zone_name, font=font, fill=('#1C0606'))
            photo.show()
        else:
            print('Person is not initialized')
            return False

# TODO Методы получения фото, полной информации о Person, статистику