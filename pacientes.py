import flet as ft
import pandas as pd


class UIPacientes(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__(route="/pacientes")
        self.page = page

        # Variables
        self.pacientes_data = pd.DataFrame(pd.read_csv("data/pacientes.csv"))


        ##Define Colors
        self.color_blue = "#73b1fc"
        self.color_purple = ft.Colors.TEAL_ACCENT_700
        self.color_green = ft.Colors.TEAL_ACCENT_700
        self.bg_color = "#396564"
        self.container_color = ft.Colors.TEAL_800
        self.color_navigation_bt = ft.Colors.LIGHT_GREEN_900
        self.color1_card = "#f46fd8"
        self.color2_card = "#64e4ed"

        #Config principal
        self.page.bgcolor = self.bg_color
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)


        ## Componentes hijo
        self.option_1 = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0,0),
            #animate_offset= self.animation_style,
            #on_click=lambda e: self.change_page(e,1),
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.PERSON, color="white"),
                    ft.Text("PACIENTES",width=120)
                ]
            )
        )

        ##Componentes de Tabla
        self.search_pacient = ft.TextField(
            label="Buscar",
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color="white",
            label_style=ft.TextStyle(color="white"),
            width= 400
        )

        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, "green"),
            #data_row_color=(ft.State),
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("ID", color="green", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("NOMBRE", color="green", weight="bold")),
                ft.DataColumn(ft.Text("APELLIDOS", color="green", weight="bold")),
                ft.DataColumn(ft.Text("EDAD", color="green", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("GENERO", color="green", weight="bold")),
                ft.DataColumn(ft.Text("PESO", color="green", weight="bold")),
            ]
        )
        self.show_data()


        ## CREACION DE TABLA
        self.table = ft.Container(
            bgcolor="#9bf2b5",
            border_radius=10,
            col=8,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=30,
                        content=ft.Row(
                            controls=[
                                ft.Text(" ",width=200),
                                self.search_pacient,
                                ft.Icon(ft.icons.PERSON, color="white")
                            ],
                            alignment=ft.alignment.top_center
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            self.data_table,
                        ]
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.bottom_left,

            ),
        )



        ## Componentes Padre
        self.navegation = ft.Container(
            content= ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_1
                ]
            )
        )
        self.content_element = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content= ft.Stack(
                controls=[
                    self.table
                ]
            )
        )

        # Add components a panel principal
        self.page.add(
            ft.Row(
                expand=True,
                spacing=20,
                controls=[
                    # Componentes que apareceran
                    self.navegation,
                    self.content_element
                ]
            )
        )

    ## Funciones
    def show_data(self):
        self.data_table.rows = []
        for i in range(len(self.pacientes_data)):
            print(i)
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(self.pacientes_data.iloc[i]["id"]))),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['name'])),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['apellidos'])),
                        ft.DataCell(ft.Text(str(self.pacientes_data.iloc[i]['edad']))),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['genero'])),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['peso'])),
                    ]
                )
            )
        self.update()


ft.app(target=lambda page:UIPacientes(page))