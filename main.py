import flet as ft
import pandas as pd

def main(page: ft.Page):
    normal_border = ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors.WHITE))
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    pacientes_data = pd.read_csv("data/pacientes.csv")
    pacientes_age = pd.read_csv("data/pacientes.csv",usecols=["id","edad"])

    df_pacientes=pd.DataFrame(pacientes_data)
    df_age = pd.DataFrame(pacientes_age)

    normal_badge_size = 40
    normal_title_style = ft.TextStyle(
        size=12, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD
    )

    def badge(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.Colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.Colors.WHITE,
        )



    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.FAVORITE),
        leading_width=40,
        title=ft.Text("NutriApp"),
        center_title=True,
        bgcolor=ft.Colors.GREEN,
        actions=[
            ft.IconButton(ft.Icons.KEYBOARD_RETURN),
        ],
    )

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Consulta Genero",
                content=ft.ResponsiveRow(
            [

                ft.Text("Genero"),
                ft.Row([

                    ft.Container(
                        content=ft.Column(
                            [
                                ft.CupertinoCheckbox(label="Hombre", value=True),
                                ft.CupertinoCheckbox(label="Mujer", value=True),
                                ft.CupertinoCheckbox(label="No especificado", value=True),

                            ]
                        ),
                    ),

                        ft.PieChart(
                            sections=[
                                ft.PieChartSection(
                                    5,
                                    color=ft.colors.BLUE,
                                    radius=80,
                                    border_side=normal_border,
                                    title="5",
                                    title_style=normal_title_style,
                                    badge=badge(ft.Icons.MAN, normal_badge_size),
                                    badge_position=0.98,
                                ),
                                ft.PieChartSection(
                                    4,
                                    color=ft.colors.PINK,
                                    radius=80,
                                    border_side=normal_border,
                                    title="4",
                                    badge=badge(ft.Icons.WOMAN, normal_badge_size),
                                    badge_position=0.98,
                                ),
                                ft.PieChartSection(
                                    2,
                                    color=ft.colors.GREEN,
                                    radius=80,
                                    border_side=normal_border,
                                    title="1",
                                    badge=badge(ft.Icons.QUIZ, normal_badge_size),
                                    badge_position=0.98,
                                )
                            ],
                            sections_space=1,
                            center_space_radius=0,
                            expand=True
                        ),

                ]),
            ]),
            ),

            ft.Tab(
                text="Estadistica",
                content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.DataTable(
                                    columns=[
                                        ft.DataColumn(ft.Text("ID Paciente")),
                                        ft.DataColumn(ft.Text("Edad"), numeric=True),
                                    ],
                                    rows=[
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("1")),
                                                ft.DataCell(ft.Text("43")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("2")),
                                                ft.DataCell(ft.Text("19")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("3")),
                                                ft.DataCell(ft.Text("25")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("4")),
                                                ft.DataCell(ft.Text("28")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("5")),
                                                ft.DataCell(ft.Text("38")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("6")),
                                                ft.DataCell(ft.Text("25")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("7")),
                                                ft.DataCell(ft.Text("30")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("8")),
                                                ft.DataCell(ft.Text("45")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("9")),
                                                ft.DataCell(ft.Text("40")),
                                            ],
                                        ),
                                        ft.DataRow(
                                            cells=[
                                                ft.DataCell(ft.Text("10")),
                                                ft.DataCell(ft.Text("33")),
                                            ],
                                        ),
                                    ],
                                ),
                                padding=5,
                                bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                col={"sm": 6, "md": 4, "xl": 2},

                            ),

                            ft.Container(
                                content=ft.DataTable(
                                columns=[
                                    ft.DataColumn(ft.Text("Operación")),
                                    ft.DataColumn(ft.Text("Resultado")),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Rango")),
                                            ft.DataCell(ft.Text("26")),

                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Media")),
                                            ft.DataCell(ft.Text("32.6")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Mediana")),
                                            ft.DataCell(ft.Text("33")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Moda")),
                                            ft.DataCell(ft.Text("25")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Varianza")),
                                            ft.DataCell(ft.Text("67.44")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("Desviación")),
                                            ft.DataCell(ft.Text("8.2")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("CV")),
                                            ft.DataCell(ft.Text("0.25")),
                                        ],
                                    ),
                                ],),
                                padding=5,
                                bgcolor=ft.Colors.TERTIARY_CONTAINER,
                                col={"sm": 6, "md": 6, "xl": 3},
                            ),
                            ft.Container(
                                content=ft.BarChart(
                                bar_groups=[
                                    ft.BarChartGroup(
                                        x=0,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.AMBER,
                                                tooltip="19",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=1,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=2,
                                                width=40,
                                                color=ft.Colors.BLUE,
                                                tooltip="25",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=2,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.RED,
                                                tooltip="28",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=3,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.GREEN,
                                                tooltip="30",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=4,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.PINK,
                                                tooltip="38",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=5,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.BLUE,
                                                tooltip="40",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=6,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.RED,
                                                tooltip="43",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                    ft.BarChartGroup(
                                        x=7,
                                        bar_rods=[
                                            ft.BarChartRod(
                                                from_y=0,
                                                to_y=1,
                                                width=40,
                                                color=ft.Colors.GREEN,
                                                tooltip="45",
                                                border_radius=0,
                                            ),
                                        ],
                                    ),
                                ],
                                border=ft.border.all(1, ft.Colors.GREY_400),
                                left_axis=ft.ChartAxis(
                                    labels_size=40, title=ft.Text("Cantidad"), title_size=40
                                ),
                                bottom_axis=ft.ChartAxis(
                                    labels=[
                                        ft.ChartAxisLabel(
                                            value=0, label=ft.Container(ft.Text("19"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=1, label=ft.Container(ft.Text("25"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=2, label=ft.Container(ft.Text("28"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=3, label=ft.Container(ft.Text("30"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=4, label=ft.Container(ft.Text("38"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=5, label=ft.Container(ft.Text("40"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=6, label=ft.Container(ft.Text("43"), padding=10)
                                        ),
                                        ft.ChartAxisLabel(
                                            value=7, label=ft.Container(ft.Text("45"), padding=10)
                                        ),
                                    ],
                                    labels_size=40,
                                ),
                                horizontal_grid_lines=ft.ChartGridLines(
                                    color=ft.Colors.GREY_300, width=1, dash_pattern=[3, 3]
                                ),
                                tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY_300),
                                max_y=5,
                                interactive=True,
                                expand=True,

                            ),
                                padding=5,
                                bgcolor=ft.Colors.SECONDARY_CONTAINER,
                                col={"sm": 6, "md": 4, "xl": 7},
                            ),
                        ],
                        ),
            ),



            ft.Tab(
                text= "Todos List",
                icon=ft.Icons.TABLET,
                content=ft.Container(
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Name")),
                            ft.DataColumn(ft.Text("Apellidos")),
                            ft.DataColumn(ft.Text("Edad"), numeric=True),
                            ft.DataColumn(ft.Text("Genero")),
                            ft.DataColumn(ft.Text("Peso"), numeric=True),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Juan")),
                                    ft.DataCell(ft.Text("Smith")),
                                    ft.DataCell(ft.Text("43")),
                                    ft.DataCell(ft.Text("M")),
                                    ft.DataCell(ft.Text("55")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Jaime")),
                                    ft.DataCell(ft.Text("Brown")),
                                    ft.DataCell(ft.Text("19")),
                                    ft.DataCell(ft.Text("M")),
                                    ft.DataCell(ft.Text("85")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Alicia")),
                                    ft.DataCell(ft.Text("Blanco")),
                                    ft.DataCell(ft.Text("25")),
                                    ft.DataCell(ft.Text("F")),
                                    ft.DataCell(ft.Text("75")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Juan")),
                                    ft.DataCell(ft.Text("Martinez")),
                                    ft.DataCell(ft.Text("28")),
                                    ft.DataCell(ft.Text("M")),
                                    ft.DataCell(ft.Text("67")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Mario")),
                                    ft.DataCell(ft.Text("Diaz")),
                                    ft.DataCell(ft.Text("38")),
                                    ft.DataCell(ft.Text("M")),
                                    ft.DataCell(ft.Text("100")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Karla")),
                                    ft.DataCell(ft.Text("Montes")),
                                    ft.DataCell(ft.Text("25")),
                                    ft.DataCell(ft.Text("F")),
                                    ft.DataCell(ft.Text("55")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Ana")),
                                    ft.DataCell(ft.Text("Vazquez")),
                                    ft.DataCell(ft.Text("30")),
                                    ft.DataCell(ft.Text("F")),
                                    ft.DataCell(ft.Text("57")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Mario")),
                                    ft.DataCell(ft.Text("Morales")),
                                    ft.DataCell(ft.Text("45")),
                                    ft.DataCell(ft.Text("N")),
                                    ft.DataCell(ft.Text("85")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Angelica")),
                                    ft.DataCell(ft.Text("Hernandez")),
                                    ft.DataCell(ft.Text("40")),
                                    ft.DataCell(ft.Text("F")),
                                    ft.DataCell(ft.Text("60")),
                                ],
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Fernando")),
                                    ft.DataCell(ft.Text("Montes")),
                                    ft.DataCell(ft.Text("33")),
                                    ft.DataCell(ft.Text("M")),
                                    ft.DataCell(ft.Text("78")),
                                ],
                            ),
                        ],
                    ),
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)


ft.app(main)