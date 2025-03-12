import flet as ft


class UINutricion(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__(expand=True)
        self.page=page
        self.page.padding=0

        ##Define Colors
        self.color_blue = "#73b1fc"
        #self.color_purple = "#bb7efd"
        self.color_purple = ft.Colors.TEAL_ACCENT_700
        self.color_green = ft.Colors.TEAL_ACCENT_700
        self.bg_color = "#396564"
        #self.bg_color = "#3f3965"396564
        #self.container_color = "#362e57"
        self.container_color = ft.Colors.TEAL_800
        #self.color_navigation_bt = "#2a2949"
        self.color_navigation_bt = ft.Colors.LIGHT_GREEN_900
        self.color1_card = "#f46fd8"
        self.color2_card = "#64e4ed"


        #Settings Colors
        self.page.bgcolor = self.bg_color
        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)


        #Config elementos
        self.container_1 = ft.Container(
            expand=True,
            bgcolor = self.container_color,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=True,
                        content=ft.Stack(
                            alignment=ft.alignment.center,
                            controls=[
                                ft.Container(
                                    expand=True,
                                    bgcolor=self.container_color,
                                    margin=ft.margin.only(left=0, top=150, right=0,bottom=0),
                                    padding=ft.padding.only(left=0, top=100, right=0,bottom=0),
                                    border_radius=20,
                                ),
                                ft.Container(
                                    height=180,
                                    width=300,
                                    gradient=ft.LinearGradient(
                                        rotation=.05,
                                        colors=[
                                            self.color1_card,
                                            self.color2_card,
                                            self.color_green
                                        ]
                                    ),
                                    margin=ft.margin.only(left=50, top=50, right=50,bottom=0),
                                    border_radius=20,
                                    padding=10,
                                    content=ft.Column()
                                )
                            ]
                        )
                    ),
                    ft.Container()

            ])
        )
        self.container_2 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset=ft.transform.Offset(2, 0),
            animate_offset=self.animation_style,
        )
        self.container_3 = ft.Container(
            expand=True,
            bgcolor=self.container_color,
            offset=ft.transform.Offset(2, 0),
            animate_offset=self.animation_style,
        )

        self.frame = ft.Container(
            expand=True,
            content=ft.Stack(
               controls=[
                   self.container_1,
                   self.container_2,
                   self.container_3,
               ]
            )
        )

        self.option_1=ft.Container(
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
        self.option_3=ft.Container(
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
                    self.option_1,
                    self.option_2,
                    self.option_3,
                ]
            )
        )



        self.page.add(
            ft.Row(
                expand=True,
                spacing=20,
                controls=[
                    self.navegation,
                    self.frame,
                ]
            )
        )


        self.switch_control_btns ={
            1: self.container_1,
            2: self.container_2,
            3: self.container_3,
        }


    def change_page(self, e, n):
        for page in self.switch_control_btns:
            self.switch_control_btns[page].offset.y = 2
            self.option_1.bgcolor = self.color_navigation_bt,
            self.option_2.bgcolor = self.color_navigation_bt,
            self.option_3.bgcolor = self.color_navigation_bt,

            if n == 1:
                self.option_1.offset.x = 0.15
                self.option_2.offset.x = 0
                self.option_3.offset.x = 0
                self.option_1.bgcolor = self.color_purple
                self.option_1.update()
            elif n == 2:
                self.option_1.offset.x = 0
                self.option_2.offset.x = 0.15
                self.option_3.offset.x = 0
                self.option_2.bgcolor = self.color_purple
                self.option_2.update()
            elif n == 3:
                self.option_1.offset.x = 0
                self.option_2.offset.x = 0
                self.option_3.offset.x = 0.15
                self.option_3.bgcolor = self.color_purple
                self.option_3.update()
            self.page.update()


ft.app(target=lambda page:UINutricion(page))