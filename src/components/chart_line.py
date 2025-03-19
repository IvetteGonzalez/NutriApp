import flet as ft
import plotly.express as px
from flet.plotly_chart import PlotlyChart


class MyChart_line(ft.Container):
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

        self.df_linea = data
        self.fig = px.line(self.df_linea, x="mes", y="peso", color="name")
        self.grafico_line = ft.Container(content=PlotlyChart(self.fig, expand=True),
                                         width=700,
                                         height=400,
                                         alignment=ft.alignment.top_center,
                                         visible=True)

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                self.grafico_line
            ]
        )
