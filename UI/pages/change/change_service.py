#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################
class Content(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        code = TextField(label="Код")
        name = TextField(label="Название")
        mkb = TextField(label="МКБ")
        csg = TextField(label="КСГ")
        clinical_minimum = DataTable(
            border_radius=10,
            width=1500,
            border=border.all(2, "black"),
            columns=[
                DataColumn(Text("#")),
                DataColumn(Text("Категории")),
                DataColumn(Text("Название")),
                DataColumn(Text("Время действия (Дней)")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text(value="1")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="2")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="3")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="4")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                ),
                DataRow(
                    cells=[
                        DataCell(Text(value="5")),
                        DataCell(
                            Dropdown(hint_text='Категории', options=[dropdown.Option("Лабораторные исследования")])),
                        DataCell(TextField(label="Название", )),
                        DataCell(TextField(label="Время действия (Дней)")),
                    ]
                )
            ]
        )
        save = FilledButton(text='Сохранить')
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
                content=Column(
                    [
                        Container(
                            Text(value='МКБ - Создать', size=20),
                            padding=padding.only(left=50, right=50, top=15, bottom=7),
                        ),
                        Divider(height=10),
                        Container(code, padding=padding.only(left=50, right=50)),
                        Container(name, padding=padding.only(left=50, right=50)),
                        Container(mkb, padding=padding.only(left=50, right=50)),
                        Container(csg, padding=padding.only(left=50, right=50)),
                        Container(
                            Text(value='Клинический минимум', size=14),
                            padding=padding.only(left=50, right=50, top=5, bottom=2),
                        ),
                        Container(clinical_minimum, padding=padding.only(left=50, right=50)),
                        Container(save, padding=padding.only(left=50, right=50, top=10, bottom=10)),
                    ],
                    )
                )
            )
        )
class change_service:
    def __init__(self, vault, config, db):
        super(change_service, self).__init__()
        self.__vault = vault
        self.__config = config

    def change_service(self, pg: PageData):
        pg.page.title = "Услуги - Создать"
        pg.page.theme_mode = 'dark'
        pg.page.vertical_alignment = MainAxisAlignment.CENTER
        pg.page.horizontal_alignment = CrossAxisAlignment.CENTER
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
                        content=Content(),
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        ),
                    )
                ],
                expand=True,
            )
        )
        pg.page.update()
