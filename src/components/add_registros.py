import pandas as pd
import flet as ft
import csv


class AddRegistros(ft.Container):
    def __init__(self):
        super().__init__()
        # Variables
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800

        # Campos de entrada
        self.nombre_input = ft.TextField(label="Nombre Completo", width=400, color=ft.colors.BLACK)
        self.edad_input = ft.TextField(label="Edad", width=400, color=ft.colors.BLACK)
        self.genero_input = ft.Dropdown(
            label="Género",
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Femenino"),
                ft.dropdown.Option("No especificado")
            ],
            width=400,
            color=ft.colors.BLACK
        )
        self.peso_input = ft.TextField(label="Peso (kg)", width=400, color=ft.colors.BLACK)
        self.altura_input = ft.TextField(label="Altura (m)", width=400, color=ft.colors.BLACK)


        # Tabla de pacientes
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("NOMBRE")),
                ft.DataColumn(ft.Text("APELLIDOS")),
                ft.DataColumn(ft.Text("EDAD")),
                ft.DataColumn(ft.Text("GÉNERO")),
                ft.DataColumn(ft.Text("PESO")),
                ft.DataColumn(ft.Text("IMC")),
                ft.DataColumn(ft.Text("Acción")),
            ],
            rows=[]
        )

        self.formulario = ft.Container(
            content=ft.Column(
                controls=[
                    self.nombre_input,
                    self.edad_input,
                    self.genero_input,
                    self.peso_input,
                    self.altura_input,
                ]
            ),
            width=700,
            alignment=ft.alignment.top_center,
            margin=ft.margin.only(left=0, top=150, right=0, bottom=0),
            #padding=ft.padding.only(left=0, top=100, right=0, bottom=0),
            visible=True
        )

        # Inicializar CSV y actualizar tabla
        self.inicializar_csv()
        self.actualizar_tabla()


        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                    self.formulario,
                    ft.ElevatedButton("Agregar Paciente", on_click=self.add_paciente()),
                    self.table
            ]
        )

    def inicializar_csv(self):
        """Inicializa el archivo CSV si no existe."""
        try:
            self.df = pd.read_csv("./data/pacientes_imc.csv")
            print("Archivo CSV cargado correctamente.")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["ID", "NOMBRE", "APELLIDOS", "EDAD", "GÉNERO", "PESO", "IMC"])
            self.df.to_csv("./data/pacientes_imc.csv", index=False)
            print("Archivo CSV creado.")

    def actualizar_tabla(self):
        """Carga los datos del CSV en la tabla."""
        self.df = pd.read_csv("./data/pacientes_imc.csv")

        # Verificar si la columna "ID" existe
        if "ID" not in self.df.columns:
            print("Error: La columna 'ID' no existe en el DataFrame")
            return

        self.table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(row["ID"]))),
                    ft.DataCell(ft.Text(str(row["NOMBRE"]))),
                    ft.DataCell(ft.Text(str(row["APELLIDOS"]))),
                    ft.DataCell(ft.Text(str(row["EDAD"]))),
                    ft.DataCell(ft.Text(str(row["GÉNERO"]))),
                    ft.DataCell(ft.Text(str(row["PESO"]))),
                    ft.DataCell(ft.Text(str(row["IMC"]))),
                    ft.DataCell(
                        ft.ElevatedButton("Eliminar", on_click=lambda e, id=row["ID"]: self.eliminar_paciente(id))),
                ]
            )
            for _, row in self.df.iterrows()
        ]
        #self.page.update()

    def agregar_paciente(self, e):
        """Agrega un paciente a la tabla y al CSV."""
        nuevo_paciente = {
            "ID": len(self.df) + 1,
            "NOMBRE": self.nombre_input.value,
            "APELLIDOS": "",
            "EDAD": self.edad_input.value,
            "GÉNERO": self.genero_input.value,
            "PESO": self.peso_input.value,
            "IMC": round(float(self.peso_input.value) / (float(self.altura_input.value) ** 2),
                         2) if self.altura_input.value else "N/A"
        }

        self.df = self.df.append(nuevo_paciente, ignore_index=True)
        self.df.to_csv("./data/pacientes_imc.csv", index=False)
        self.actualizar_tabla()

    def add_paciente(self):
        nuevo_paciente = {
            "ID": len(self.df) + 1,
            "NOMBRE": self.nombre_input.value,
            "EDAD": self.edad_input.value,
            "GÉNERO": self.genero_input.value,
            "PESO": self.peso_input.value,
            "IMC": round(float(self.peso_input.value) / (float(self.altura_input.value) ** 2),
                         2) if self.altura_input.value else "N/A"
        }
        with open("./data/pacientes_imc.csv", mode="a", newline="", encoding="utf-8") as archivo:
            # Definir los nombres de las columnas (deben coincidir con los del CSV)
            nombres_columnas = ["ID", "NOMBRE", "EDAD", "GÉNERO", "PESO", "IMC"]

            # Crear un escritor de diccionarios
            paciente = csv.DictWriter(archivo, fieldnames=nombres_columnas)

            # Si el archivo está vacío, escribir la cabecera
            if archivo.tell() == 0:
                paciente.writeheader()

            # Escribir el nuevo registro
            paciente.writerow(nuevo_paciente)
            self.actualizar_tabla()


    def eliminar_paciente(self, id_paciente):
        """Elimina un paciente del CSV y actualiza la tabla."""
        self.df = self.df[self.df["ID"] != id_paciente]
        self.df.to_csv("./data/pacientes_imc.csv", index=False)
        self.actualizar_tabla()