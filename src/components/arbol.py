import flet as ft
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
from sklearn.tree import DecisionTreeClassifier, plot_tree
import os
import base64


class MyTree(ft.Container):
    def __init__(self, data):
        super().__init__()
        # Variables
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800
        #self.page.title = "Árbol de Decisión Pacientes - Ejercicio"

        # Ejemplo de datos
        data = [
            {"peso": 70, "altura": 175, "genero": "Hombre"},# 20
            {"peso": 50, "altura": 160, "genero": "Mujer"},
            {"peso": 90, "altura": 170, "genero": "Hombre"},
            {"peso": 60, "altura": 165, "genero": "Mujer"},
            {"peso": 85, "altura": 180, "genero": "Hombre"},
            {"peso": 55, "altura": 150, "genero": "Mujer"},
            {"peso": 75, "altura": 175, "genero": "No especificado"},
            {"peso": 85, "altura": 160, "genero": "Hombre"},
            {"peso": 55, "altura": 156, "genero": "Mujer"},
            {"peso": 65, "altura": 175, "genero": "Hombre"},
        ]


        # Cargar datos y entrenar un modelo de árbol de decisión
        df = pd.DataFrame(data)
        #df.sample(10)

        # Calcular el IMC
        df["IMC"] = df["peso"] / (df["altura"] / 100) ** 2

        # Asumir sobrepeso si el IMC es mayor o igual a 25
        df["sobrepeso"] = (df["IMC"] >= 25).astype(int)

        # Convertir género en variables binarias (one-hot encoding)
        df = pd.get_dummies(data=df, columns=["genero"], drop_first=True)
        #df.sample(10)

        explicativas = df.drop(columns='sobrepeso')  # Se crea un nuevo dataframe sin la columna clase
        objetivo = df.sobrepeso  # Se crea un nuevo dataframe solo con la columna clase

        model = DecisionTreeClassifier(max_depth=5)
        model.fit(X=explicativas, y=objetivo)
        # DecisionTreeClassifier()

        # Generar y guardar el gráfico del árbol
        plt.figure(figsize=(8, 6))
        plot_tree(model, feature_names=explicativas.columns,class_names=["No Sobrepeso", "Sobrepeso"], filled=True)
        plt.savefig("./assets/arbol_decision.png", bbox_inches="tight")
        plt.close()

        # Mostrar la imagen en la app de Flet
        imagen_arbol = ft.Image(src="./assets/arbol_decision.png",
                                width=600,
                                height=400,
                                fit=ft.ImageFit.CONTAIN,
                                error_content=ft.Text("Imagen no encontrada"))

        imagen_arbol_b64 = self.convertir_a_base64("./assets/arbol_decision.png")

        txt_description= ft.Column(
            controls=[
                ft.Text("IMC  :  Indice de Masa Muscular",
                        size=18,
                        color="#000d04",
                        weight=ft.FontWeight.BOLD),
                ft.Text("gini  :  Grado de Confianza",
                        size=18,
                        color="#000d04",
                        weight=ft.FontWeight.BOLD),
                ft.Text("Samples  :  Muestra de Pacientes",
                        size=18,
                        color="#000d04",
                        weight=ft.FontWeight.BOLD),
                ft.Text("Value  :  Cantidad correspondiente a cada nodo",
                        size=18,
                        color="#000d04",
                        weight=ft.FontWeight.BOLD),
                ft.Text("class  :  Resultado",
                        size=18,
                        color="#000d04",
                        weight=ft.FontWeight.BOLD),

            ],
            col={"md": 4}
        )

        arbol_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Valida Sobrepeso", size=32, color="#0c3d1b", weight=ft.FontWeight.BOLD),
                    ft.Text("Se realiza validación de obesidad mediante IMC",
                            size=24,
                            color="#000d04",
                            weight=ft.FontWeight.BOLD),
                    ft.ResponsiveRow(
                        [
                            txt_description,
                            ft.Container(
                                ft.Image(
                                    src_base64=imagen_arbol_b64,
                                    fit=ft.ImageFit.CONTAIN,
                                    error_content=ft.Text("Imagen no encontrada")
                                ),
                                padding=5,
                                #bgcolor=ft.Colors.BLUE,
                                expand=True,
                                col={"md": 4},
                            ),
                        ],
                        run_spacing={"xs": 10},
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
            ),
            #bgcolor= ft.colors.BLUE_500,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
            col={"sm": 12, "md": 6, "lg": 3}
        )


        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                arbol_container,
                #ft.Image(src_base64=imagen_arbol_b64),
        ]
        )

    def convertir_a_base64(self,ruta_imagen):
        with open(ruta_imagen, "rb") as archivo_imagen:
            return base64.b64encode(archivo_imagen.read()).decode("utf-8")


