#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
from modules.load_data import LoadData
from modules.utilites import word_wrap, save_export_xlsx


#################################################


class Content(UserControl):
    def __init__(self, load_data):
        super().__init__()
        self.__load_data = load_data

    def build(self):
        return (Container
            (
            padding=padding.only(left=30, right=30, top=15),
            expand=True,
            content=Container
                (
                shadow=BoxShadow
                    (
                    spread_radius=0.5,
                    blur_radius=15,
                    color=colors.BLUE_GREY_300,
                    offset=Offset(0, 0),
                    blur_style=ShadowBlurStyle.OUTER,
                ),
                border_radius=10,
                content=Row(
                    [
                        DataTable(
                            columns=
                            [
                                DataColumn(Text(value='Код', size=15)),
                                DataColumn(Text(value='Название', size=15)),
                                DataColumn(Text(value='МКБ', size=15)),
                                DataColumn(Text(value='КСГ', size=15)),
                                DataColumn(Text(value='', size=15)),
                                DataColumn(Text(value='', size=15)),
                            ],
                            rows=self.generate_carts()
                        )
                    ]
                )
            )
        )
        )

    def switchbnt(self):
        pass

    def generate_carts(self):
        carts = list()
        for cart in self.__load_data.service():
            carts.append(
                DataRow(
                    cells=[
                        DataCell(Text(cart[0])),
                        DataCell(Text(cart[1])),
                        DataCell(Text(cart[2])),
                        DataCell(Text(cart[3])),
                        DataCell(IconButton(icon=icons.MODE_EDIT_OUTLINE_OUTLINED, tooltip='Изменить')),
                        DataCell(IconButton(icon=icons.DELETE, tooltip='Удалить')),
                    ]
                )
            )
        return carts


class service_ui(UserControl):
    def __init__(self, pg, load_data, config):
        super().__init__()
        self.__pg = pg
        self.__load_data = load_data
        self.__config = config

    def add(self, event):
        self.__pg.navigator.navigate('service_change_service', self.__pg.page)

    def create_export(self, event):
        save_export_xlsx(self.__config['export_xlsx_path'], self.__load_data.application(), 'services')

    def build(self):
        # ЗНАЧЕНИЯ#
        btn_create = FilledButton(icon=icons.ADD,
                                  text='Создать', on_click=self.add)  # ЭТО КНОПКА ДЛЯ СОЗДАНИЯ ЗАЯВКИ, НУЖНО СДЕЛАТЬ ПЕРЕХОД С ЭТОЙ КНОПКИ НА ДРУГУЮ СТРАНИЦУ
        pb = PopupMenuButton(
            items=[
                PopupMenuItem(icon=icons.CLOUD_DOWNLOAD, text='Экспорт', on_click=self.create_export)
            ]
        )

        return Container(
            height=1500,
            content=Column(
                [
                    Container(
                        content=Text(value='Услуги', size=20),
                        padding=padding.only(left=60, right=60, top=20)
                    ),
                    Container(
                        content=Row([btn_create, pb]),
                        padding=padding.only(left=50, top=10)
                    ),
                    Container(
                        content=Content(self.__load_data)
                    )
                ],
                scroll=ScrollMode.ALWAYS,
                expand=True,
                alignment=MainAxisAlignment.START,
            ),
        )


class Service:
    def __init__(self, vault, config, db):
        super(Service, self).__init__()
        self.__vault = vault
        self.__config = config
        self.__db = db
        self.__load_data = LoadData(db)

    def service(self, pg: PageData):
        pg.page.title = "Услуги"
        pg.page.theme_mode = 'dark'
        pg.page.add(
            Row(
                [
                    Container(
                        border_radius=10,
                        content=SideBar(self.__vault, pg),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        )
                    ),
                    Container(
                        border_radius=10,
                        expand=True,
                        content=service_ui(pg, self.__load_data, self.__config),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        )
                    )
                ],
                expand=True,
            )
        )
        pg.page.update()