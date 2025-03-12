import flet as ft
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart


class UIReportes(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__(expand=True)
        self.page = page

        # Variables
        self.pacientes_data = pd.DataFrame(pd.read_csv("data/pacientes.csv"))


        ##Define Colors
        self.color_blue = "#73b1fc"
        self.color_purple = ft.Colors.TEAL_ACCENT_700
        self.color_green = ft.Colors.TEAL_ACCENT_700
        self.bg_color = "#396564"
        self.container_color = ft.Colors.WHITE
        self.color_navigation_bt = ft.Colors.LIGHT_GREEN_900
        self.color1_card = "#f46fd8"
        self.color2_card = "#64e4ed"

        #Config principal
        self.page.bgcolor = self.bg_color
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)


        ##Config chart
        self.normal_radius = 100
        self.hover_radius = 110
        self.normal_title_style = ft.TextStyle(
            size=12, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=16,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.Colors.BLACK54),
        )
        self.normal_badge_size = 40
        self.hover_badge_size = 50

        ## Componentes hijo
        self.option_reportes_menu = ft.Container(
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
                    ft.Icon(ft.icons.BAR_CHART, color="white"),
                    ft.Text("REPORTES",width=120)
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

        self.select_reporte = ft.DropdownM2(
            label="Color",
            hint_text="Choose your favourite color?",
            on_change=self.dropdown_changed(),
            options=[
                ft.dropdownm2.Option("Red"),
                ft.dropdownm2.Option("Green"),
                ft.dropdownm2.Option("Blue"),
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
                        #badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        30,
                        title="30%",
                        title_style=self.normal_title_style,
                        color=ft.Colors.YELLOW,
                        radius=self.normal_radius,
                        #badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        15,
                        title="15%",
                        title_style=self.normal_title_style,
                        color=ft.Colors.PURPLE,
                        radius=self.normal_radius,
                        #badge=self.badge(ft.Icons.AC_UNIT, self.normal_badge_size),
                        badge_position=0.98
                    )
                ],
                sections_space=0,
                center_space_radius=0,
                #on_chart_event=on_chart_event,
                expand=True,
            )
        )
        self.df_linea = px.data.gapminder().query("continent=='Oceania'")
        self.fig = px.line(self.df_linea, x="year", y="lifeExp", color="country")
        self.grafico_peso= PlotlyChart(self.fig, expand=True)

        self.data_canada = px.data.gapminder().query("country == 'Canada'")
        self.fig_barras = px.bar(self.data_canada, x='year', y='pop')
        self.grafico_edades=PlotlyChart(self.fig_barras,expand=True)






        self.graficosframe = ft.Container(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Seleccione el reporte deseado:"),
                    self.select_reporte,
                    self.grafico_genero,
                    self.grafico_peso,
                    self.grafico_edades

                ]
            )
        )



        ## Componentes Padre
        self.navegation = ft.Container(
            content= ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_reportes_menu
                ]
            )
        )
        self.content_element = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content= ft.Stack(
                controls=[
                    self.graficosframe
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

    def badge(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.Colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.Colors.WHITE,
        )

    def dropdown_changed(e):
        print("on change en construcción")

    def badgefunction(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.Colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.Colors.WHITE,
        )


ft.app(target=lambda page:UIReportes(page))