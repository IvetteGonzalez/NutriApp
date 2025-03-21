import flet as ft
import pandas as pd
from table import MyTable
from components.chart_pie import MyChart_pie
from components.chart_line import MyChart_line
from components.chart_barras import MyChart_barras
from components.registros import MyForm
from components.arbol import MyTree
from components.add_registros import AddRegistros


class UINutricion(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/")
        self.page = page
        self.page.padding = 0
        self.page.adaptive = True

        # Define Colors
        self.bg_color = "#1fed6a"
        self.container_color = "#d0f5e5"
        self.color_purple = ft.Colors.TEAL_ACCENT_700
        self.color_navigation_bt = "#27c3ea"
        self.color_text_search = "#0c5c39"
        self.color_text_table = "#204032"
        self.bg_color_head = "#005954"

        # Configuración pagina
        self.page.bgcolor = ft.Colors.WHITE
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)

        self.pacientes_data = pd.DataFrame(pd.read_csv("data/pacientes.csv"))
        self.pacientes_data_peso = pd.DataFrame(pd.read_csv("data/pacientes_peso_mensual.csv"))
        self.pacientes_data_ejercicio = pd.read_csv("data/pacientes_ejercicio.csv")


        # Componentes Generales #
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.FAVORITE_ROUNDED, color=ft.Colors.WHITE, size=30),
            leading_width=40,
            title=ft.Text("N u t r i A p p",
                          theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                          italic=True,
                          weight=ft.FontWeight.BOLD),
            center_title=False,
            bgcolor=self.bg_color_head,
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                # ft.IconButton(ft.Icons.FILTER_3),
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

        '''
        page.navigation_bar = ft.NavigationBar(
            bgcolor=self.bg_color_head,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.FREE_BREAKFAST, label="Alimentos"),
                ft.NavigationBarDestination(icon=ft.Icons.SCALE, 
                                            label="InBody"),
                ft.NavigationBarDestination(icon=ft.Icons.STARS, label="Favoritos"),
            ]
        )
        '''

        # Contenedor de tabla
        self.content_element_table = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Stack(
                controls=[
                    MyTable(route="data/pacientes.csv")
                ]
            ),
            visible=False
        )
        # FIN COMPONENTES TABLA--------------------------------

        # Componentes de GRAFICOS
        self.chart_pie = MyChart_pie(data=self.pacientes_data)
        self.chart_line = MyChart_line(data=self.pacientes_data_peso)
        self.chart_barras = MyChart_barras(data=self.pacientes_data)

        self.chart_pie.visible = False
        self.chart_line.visible = False
        self.chart_barras.visible = False

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
                ft.dropdownm2.Option(1, "Reporte por Género", ),
                ft.dropdownm2.Option(2, "Reporte Movimiento de peso por paciente"),
                ft.dropdownm2.Option(3, "Reporte por edades"),
            ],
            autofocus=True,
        )

        self.head_reportes = ft.Container(
            ft.Container(
                expand=True,
                border_radius=20,
                margin=80,
                bgcolor="#9bf2b5",
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

        # Pantalla de reportes
        self.content_element_chart = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.head_reportes,
                    self.chart_pie,
                    self.chart_line,
                    self.chart_barras
                ]
            )
        )

        self.container_chart = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Container(
                # expand=True,
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

        self.form_paciente = MyForm()
        self.form_paciente.visible = False

        self.registro_container = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            #padding=100,
            margin=ft.margin.only(left=30, top=150, right=30, bottom=0),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.form_paciente,
                ]
            ),
            visible=True
        )

        # Contenedor de árbol
        self.content_tree = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Stack(
                controls=[
                    MyTree(self.pacientes_data_ejercicio)
                ]
            ),
            visible=False
        )

        # Contenedor de New registro
        self.content_AddReg = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            content=ft.Stack(
                controls=[
                    AddRegistros()
                ]
            ),
            visible=False
        )


        self.frame = ft.Container(
            expand=True,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                controls=[
                    self.content_element_table,
                    self.container_chart,
                    #self.registro_container,
                    self.content_tree,
                    self.content_AddReg
                ],
            )
        )

        # boton pacientes
        self.option_paciente_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,
            on_click=lambda e: self.change_page(e, 1),
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.PERSON, color="white"),
                    ft.Text("PACIENTES",
                            width=120,
                            color=self.color_text_search,
                            size=20,
                            weight=ft.FontWeight.BOLD)
                ]
            )
        )
        # boton Registros
        self.option_registro_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,
            on_click=lambda e: self.change_page(e, 2),
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.CALCULATE, color="white"),
                    ft.Text("REGISTROS",
                            width=120,
                            color=self.color_text_search,
                            size=20,
                            weight=ft.FontWeight.BOLD)
                ]
            )
        )

        # boton Reportes-Graficas  3
        self.option_reportes_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,
            on_click=lambda e: self.change_page(e, 3),
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.BOOK, color="white"),
                    ft.Text("REPORTES",
                            width=120,
                            color=self.color_text_search,
                            size=20,
                            weight=ft.FontWeight.BOLD)
                ]
            )
        )

        # boton Inbody  4
        self.option_inbody_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,
            on_click=lambda e: self.change_page(e, 4),
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.SCALE, color="white"),
                    ft.Text("inBody",
                            width=120,
                            color=self.color_text_search,
                            size=20,
                            weight=ft.FontWeight.BOLD)
                ]
            )
        )

        # árbol 5
        self.option_tree_btn = ft.Container(
            padding=10,
            bgcolor=self.color_purple,
            border_radius=15,
            offset=ft.transform.Offset(0, 0),
            animate_offset=self.animation_style,
            on_click=lambda e: self.change_page(e, 5),
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.icons.ACCOUNT_TREE, color="white"),
                    ft.Text("Validación",
                            width=120,
                            color=self.color_text_search,
                            size=18,
                            weight=ft.FontWeight.BOLD)
                ]
            )
        )

        self.navegation = ft.Container(
            padding=20,
            bgcolor=self.container_color,
            animate_size=self.animation_style,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_paciente_btn,
                    self.option_registro_btn,
                    self.option_reportes_btn,
                    self.option_inbody_btn,
                    self.option_tree_btn
                ]
            )
        )

        # Pagina principal
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
        self.content_element_table.visible = False
        self.container_chart.visible = False
        #self.registro_container.visible = False
        self.content_AddReg.visible= False
        self.content_tree.visible = False

        self.option_paciente_btn.offset.x = 0
        self.option_registro_btn.offset.x = 0
        self.option_reportes_btn.offset.x = 0
        self.option_inbody_btn.offset.x = 0
        self.option_tree_btn.offset.x = 0

        self.option_paciente_btn.bgcolor = self.color_purple
        self.option_registro_btn.bgcolor = self.color_purple
        self.option_reportes_btn.bgcolor = self.color_purple
        self.option_inbody_btn.bgcolor = self.color_purple
        self.option_tree_btn.bgcolor = self.color_purple

        if n == 1:
            print("Llego al 1")
            self.option_paciente_btn.offset.x = 0.15
            self.option_paciente_btn.bgcolor = self.color_navigation_bt
            self.option_paciente_btn.update()
            self.content_element_table.visible = True
            self.page.controls.append(self.content_element_table)
        elif n == 2:
            print("Llego al 2")
            self.option_registro_btn.offset.x = 0.15
            self.option_registro_btn.bgcolor = self.color_navigation_bt
            self.option_registro_btn.update()
            self.form_paciente.visible = True
            #self.registro_container.visible = True
            #self.page.controls.append(self.registro_container)
            self.content_AddReg.visible =True
            self.page.controls.append(self.content_AddReg)
        elif n == 3:
            print("Llego al 3")
            self.option_reportes_btn.offset.x = 0.15
            self.option_reportes_btn.bgcolor = self.color_navigation_bt
            self.option_reportes_btn.update()
            self.container_chart.visible = True
            self.page.controls.append(self.container_chart)
        elif n == 4:
            print("Llego al 4")
            self.option_inbody_btn.bgcolor = self.color_navigation_bt
            self.option_inbody_btn.offset.x = 0.15
            self.option_inbody_btn.update()
            #self.container_chart.visible = True
            #self.page.controls.append(self.container_chart)
        elif n == 5:
            print("Llego al 5")
            self.option_tree_btn.offset.x = 0.15
            self.option_tree_btn.bgcolor = self.color_navigation_bt
            self.option_tree_btn.update()
            self.content_tree.visible = True
            self.page.controls.append(self.content_tree)
        self.page.update()

    def dropdown_changed(self,e):
        print("on change dropdown_changed")
        print(self.select_reporte.value)
        self.chart_pie.visible = False
        self.chart_line.visible = False
        self.chart_barras.visible = False

        if self.select_reporte.value == "1":
            self.chart_pie.visible = True
            self.page.controls.append(self.chart_pie)
        elif self.select_reporte.value == "2":
            self.chart_line.visible = True
            self.page.controls.append(self.chart_line)
        elif self.select_reporte.value == "3":
            self.chart_barras.visible = True
            self.page.controls.append(self.chart_barras)
        self.page.update()

    def load_image(self):
        self.page.controls.append(self.images)
        self.page.update()


ft.app(target=lambda page: UINutricion(page))