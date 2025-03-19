import flet as ft
import pandas as pd

class MyTable(ft.Container):
    def __init__(self, route):
        super().__init__()
        # Variables
        self.pacientes_data = pd.DataFrame(pd.read_csv(route))
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800
        self.color_text_table = "#204032"
        self.color_text_search = "#0c5c39"

        self.rows_per_page = 10  # Número de filas por página
        self.current_page = 0  # Página actual
        self.total_pages = int(len(self.pacientes_data) /self.rows_per_page)
        print("Total pages",self.total_pages)

        # Botones de paginación
        self.btn_prev = ft.ElevatedButton("Anterior", on_click=self.prev_page)
        self.btn_next = ft.ElevatedButton("Siguiente", on_click=self.next_page)

        # Filtro
        self.search_reg = ft.TextField(
            label="Buscar",
            suffix_icon=ft.icons.SEARCH,
            border=ft.InputBorder.UNDERLINE,
            border_color=ft.Colors.GREEN,
            label_style=ft.TextStyle(color=self.color_text_search),
            width=400,
            prefix_icon=ft.Icons.PERSON
        )



        self.data_table=ft.DataTable(
                    #expand=True,
                    border=ft.border.all(0, "green"),
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
        self.pagination_controls = ft.Row(
            [self.btn_prev, self.btn_next],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.show_data()


        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                self.search_reg,
                self.data_table,
                self.pagination_controls
            ]
        )

    def show_data(self):
        self.data_table.rows.clear()
        self.data_table.rows = []

        init = self.current_page * self.rows_per_page
        end = init + self.rows_per_page
        data = self.pacientes_data[init:end]

        for i in range(len(data)):
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(data.iloc[i]["id"]),color=self.color_text_table)),
                        ft.DataCell(ft.Text(data.iloc[i]['name'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(data.iloc[i]['apellidos'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(str(data.iloc[i]['edad']),color=self.color_text_table)),
                        ft.DataCell(ft.Text(data.iloc[i]['genero'],color=self.color_text_table)),
                        ft.DataCell(ft.Text(data.iloc[i]['peso'],color=self.color_text_table)),
                    ]
                )
            )

        print("current",self.current_page)

        self.btn_prev.disabled = self.current_page == 0
        self.btn_next.disabled = self.current_page >= self.total_pages - 1


    def next_page(self, e):
        """Avanza a la siguiente página."""
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.show_data()
            self.btn_prev.update()
            self.btn_next.update()
            self.data_table.update()

    def prev_page(self, e):
        """Retrocede a la página anterior."""
        if self.current_page > 0:
            self.current_page -= 1
            self.show_data()
            self.btn_prev.update()
            self.btn_next.update()
            self.data_table.update()



