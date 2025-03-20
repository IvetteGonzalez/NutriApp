import flet as ft
import pandas as pd


class MyChart_pie(ft.Container):
    def __init__(self, data):
        super().__init__()
        # Variables
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800
        self.normal_radius = 100
        self.hover_radius = 110
        self.normal_title_style = ft.TextStyle(
            size=12,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        )

        hombre = (data["genero"] == "M").sum()
        mujer = (data["genero"] == "F").sum()
        na = (data["genero"] == "N").sum()

        self.grafico_pie = ft.Container(
            content=ft.PieChart(
                sections=[
                    ft.PieChartSection(
                        hombre,
                        title=f"Hombre  {hombre}",
                        title_style=self.normal_title_style,
                        color=ft.Colors.BLUE,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        mujer,
                        title=f"Mujer {mujer}",
                        title_style=self.normal_title_style,
                        color=ft.Colors.YELLOW,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT,self.normal_badge_size),
                        badge_position=0.98
                    ),
                    ft.PieChartSection(
                        na,
                        title=f"NA {na}",
                        title_style=self.normal_title_style,
                        color=ft.Colors.PURPLE,
                        radius=self.normal_radius,
                        # badge=self.badge(ft.Icons.AC_UNIT, self.normal_badge_size),
                        badge_position=0.98
                    )
                ],
                sections_space=10,
                center_space_radius=10,
                # on_chart_event=on_chart_event,
                expand=True,
                width=700,
            ),
            #visible=False
        )

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                self.grafico_pie
            ]
        )





