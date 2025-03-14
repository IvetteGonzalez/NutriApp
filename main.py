import flet as ft
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart

class UINutricion(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__(route="/")
        self.page = page
        self.page.padding = 0

        ##Define Colors
        self.bg_color = "#1fed6a"
        self.container_color = "#d0f5e5"
        self.color_purple = ft.Colors.TEAL_ACCENT_700
        self.color_navigation_bt = ft.Colors.LIGHT_GREEN_900
        self.color_text_search = "#0c5c39"
        self.color_text_table="#204032"


        #Settings Colors
        self.page.bgcolor = self.bg_color
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)

        # Variables
        self.pacientes_data = pd.DataFrame(pd.read_csv("data/pacientes.csv"))

        ##Config chart
        self.normal_radius = 100
        self.hover_radius = 110
        self.normal_title_style = ft.TextStyle(
            size=12,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=16,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.Colors.BLACK54),
        )
        self.normal_badge_size = 40
        self.hover_badge_size = 50


        ##Configuracion paginado table
        self.rows_per_page = 5  # Número de filas por página
        self.current_page = 0


        page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf",
        }

        #####Componentes Generales ######
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.FAVORITE_ROUNDED,color=ft.Colors.GREEN_400, size=30),
            leading_width=40,
            title=ft.Text("NutriApp",theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,font_family="Kanit" ),
            center_title=True,
            bgcolor=ft.Colors.LIGHT_GREEN_900,
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                #ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="En construcción"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False,
                        ),
                    ]
                ),
            ],
        )

        page.navigation_bar = ft.NavigationBar(
            bgcolor=ft.Colors.LIGHT_GREEN_900,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
                ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.BOOKMARK_BORDER,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="Explore",
                ),
            ]
        )

        self.img_central= ft.Image(
            src="assets/comidaSaludable.png",
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )

        self.container_img_central = ft.Container(
                        expand=True,
                        bgcolor=self.container_color,
                        border_radius=10,
                        width=600,
                        content=ft.Column(
                            controls=[
                                self.img_central,
                            ]
                        ),
                        visible=True
                    )





        ####Componentes de pacientes  ########

        ##Componentes de Tabla
        self.search_pacient = ft.TextField(
            label="Buscar",
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color="ft.Colors.LIGHT_GREEN_900",
            label_style=ft.TextStyle(color=self.color_text_search),
            width=400
        )

        self.data_table = ft.DataTable(
            expand=True,
            border=ft.border.all(2, "green"),
            # data_row_color=(ft.State),
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            show_checkbox_column=True,
            #data_row_max_height=10,
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
            border_radius=0,
            col=8,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=30,
                        content=ft.Row(
                            controls=[
                                ft.Text(" ", width=200),
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

        ## Componentes Padre Paciente
        self.content_element_table = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Stack(
                controls=[
                    self.table
                ]
            ),
            visible=False
        )
        ###  FIN COMPONENTES PACIENTE  ####

        #### COMPONENTES REPORTES  ######

        ##Componentes de Tabla
        self.search_pacient = ft.TextField(
            label="Buscar",
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color="white",
            label_style=ft.TextStyle(color="white"),
            width=400
        )

        self.select_reporte = ft.DropdownM2(
            label="Reportes",
            hint_text="Selecciona el reporte deseado",
            width=600,
            color=self.color_text_search,
            border_color=self.color_text_search,
            border_radius=50,
            bgcolor=ft.Colors.GREEN_200,
            padding=20,
            alignment=ft.alignment.center,
            on_change=lambda e: self.dropdown_changed(e),
            options=[
                ft.dropdownm2.Option(1, "Reporte por Género",),
                ft.dropdownm2.Option(2, "Reporte Movimiento de peso por paciente"),
                ft.dropdownm2.Option(3, "Reporte por edades"),
            ],
            autofocus=True,
        )

        self.grafico_genero = ft.Container(
            content=ft.PieChart(
                sections=[
                    ft.PieChartSection(
                        40,
                        title="40%",
                        title_style=self.normal_title_style,
                        color=ft.Colors.BLUE,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        30,
                        title="30%",
                        title_style=self.normal_title_style,
                        color=ft.Colors.YELLOW,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        15,
                        title="15%",
                        title_style=self.normal_title_style,
                        color=ft.Colors.PURPLE,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT, self.normal_badge_size),
                        badge_position=0.98
                    )
                ],
                sections_space=0,
                center_space_radius=0,
                # on_chart_event=on_chart_event,
                expand=True,
            ),
            visible=False
        )

        self.df_linea = px.data.gapminder().query("continent=='Oceania'")
        #self.df_linea = self.pacientes_data
        self.fig = px.line(self.df_linea, x="year", y="lifeExp", color="country")
        self.grafico_peso = ft.Container(content=PlotlyChart(self.fig, expand=True),
                                            width=700,
                                            visible=False)


        #self.data_canada = px.data.gapminder().query("country == 'Canada'")

        self.fig_barras = px.bar(self.pacientes_data, x='name', y='edad')
        self.grafico_edades = ft.Container(
            content=(PlotlyChart(self.fig_barras, expand=True)),
            width=700,
            alignment=ft.alignment.top_center,
            visible=False
        )

        self.head_reportes = ft.Container(
            ft.Container(
                expand=True,
                border_radius=20,
                margin=80,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.alignment.center,
                    controls=[
                        ft.Text("REPORTES", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, color=self.color_text_search),
                        ft.Text("Seleccione el reporte deseado:",
                                theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=self.color_text_search),
                        ft.Divider(height=2, color="green"),

                        self.select_reporte,
                    ],
                )
            )

        )

        self.graficosframe = ft.Container(
            expand=True,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.grafico_genero,
                    self.grafico_peso,
                    self.grafico_edades
                ],
            )
        )

        self.content_element_chart = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.head_reportes,
                    self.graficosframe
                ]
            )
        )




        ## Componentes Padre Reportes
        self.content_element_reportes= ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Stack(
                controls=[
                    self.table
                ]
            ),
            visible=False
        )

        ####--------------------------------------
        #Config elementos
        self.container_table_paciente = ft.Container(
            expand=True,
            bgcolor = self.container_color,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        bgcolor=self.container_color,
                        #margin=ft.margin.only(left=0, top=150, right=0, bottom=0),
                        #padding=ft.padding.only(left=0, top=100, right=0, bottom=0),
                        border_radius=0,
                        content=ft.Column(
                            controls=[
                                #self.content_main_image,
                                self.content_element_table,
                                self.content_element_reportes
                            ]
                        )
                    ),

            ])
        )

        self.container_chart = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Container(
                        #expand=True,
                        bgcolor=self.container_color,
                        # margin=ft.margin.only(left=0, top=150, right=0, bottom=0),
                        # padding=ft.padding.only(left=0, top=100, right=0, bottom=0),
                        border_radius=20,
                        content=ft.Column(
                            controls=[
                                self.content_element_chart
                            ]
                        )
                    ),
            visible=False

        )

        self.container_3 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,

        )

        self.frame = ft.Container(
            expand=True,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.container_table_paciente,
                    self.container_chart,
                    #self.container_img_central,

                ],
            )
        )

        self.option_paciente_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,1),
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.PERSON, color="white"),
                    ft.Text("PACIENTES",width=120)
                ]
            )
        )
        self.option_2=ft.Container(
            padding=10,
            bgcolor=self.color_navigation_bt,
            border_radius=15,
            offset=ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,2),
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.CALCULATE, color="white"),
                    ft.Text("CONTROL",width=120)
                ]
            )
        )
        self.option_reportes_btn=ft.Container(
            padding=10,
            bgcolor=self.color_navigation_bt,
            border_radius=15,
            offset=ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,3),
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.BOOK, color="white"),
                    ft.Text("REPORTES",width=120)
                ]
            )
        )

        self.navegation=ft.Container(
            padding=20,
            bgcolor=self.container_color,
            animate_size=self.animation_style,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_paciente_btn,
                    self.option_2,
                    self.option_reportes_btn,
                ]
            )
        )


        self.page.add(
            ft.Row(
                expand=True,
                spacing=5,
                controls=[
                    self.navegation,
                    self.frame,
                ]
            )
        )


    def change_page(self, e, n):
        print("Change_ page")
        if n == 1:
            print("Llego al 1")
            self.option_paciente_btn.offset.x = 0.15
            self.option_2.offset.x = 0
            self.option_reportes_btn.offset.x = 0
            self.option_paciente_btn.bgcolor = self.color_purple
            self.option_paciente_btn.update()

            self.container_chart.visible = False
            self.container_table_paciente.visible = True
            self.content_element_table.visible = True
            #self.page.controls.append(self.content_element_table)
            self.page.controls.append(self.container_table_paciente)
            self.page.update()
        elif n == 2:
            self.option_paciente_btn.offset.x = 0
            self.option_2.offset.x = 0.15
            self.option_reportes_btn.offset.x = 0
            self.option_2.bgcolor = self.color_purple
            self.option_2.update()
        elif n == 3:
            print("Llego al 3")
            self.option_paciente_btn.offset.x = 0
            self.option_2.offset.x = 0
            self.option_paciente_btn.offset.x = 0
            self.option_reportes_btn.offset.x = 0.15
            self.option_reportes_btn.bgcolor = self.color_purple
            self.option_reportes_btn.update()

            self.container_table_paciente.visible = False
            self.container_chart.visible = True

            self.page.controls.append(self.container_chart)
            self.page.update()
        self.page.update()

    ##Functions pacientes
    def show_data(self):
        self.data_table.rows = []

        for i in range(len(self.pacientes_data)):
            print(i)
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(self.pacientes_data.iloc[i]["id"]),color=self.color_text_table)),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['name'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['apellidos'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(str(self.pacientes_data.iloc[i]['edad']),color=self.color_text_table)),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['genero'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(self.pacientes_data.iloc[i]['peso'],color=self.color_text_table)),
                    ]
                )
            )
        self.update()




    ##Functions Graficos
    def show_data_2(self):
        self.data_table.rows = []
        for i in range(len(self.pacientes_data)):
            print(i)

    def badge(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.Colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.Colors.WHITE,
        )

    def badgefunction(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.Colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.Colors.WHITE,
        )


    def dropdown_changed(self,e):
        print("on change en construcción")
        print(self.select_reporte.value)
        self.grafico_genero.visible = False
        self.grafico_edades.visible = False
        self.grafico_peso.visible = False


        if self.select_reporte.value == "1":
            self.grafico_genero.visible = True
            self.page.controls.append(self.grafico_genero)
        elif self.select_reporte.value == "2":
            self.grafico_peso.visible = True
            self.page.controls.append(self.grafico_peso)
        elif self.select_reporte.value == "3":
            self.grafico_edades.visible = True
            self.page.controls.append(self.grafico_edades)
        self.page.update()





ft.app(target=lambda page:UINutricion(page))