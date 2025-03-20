import flet as ft
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
from sklearn.tree import DecisionTreeClassifier, plot_tree


class MyTree(ft.Container):
    def __init__(self, data):
        super().__init__()
        # Variables
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800


        #self.page.title = "Árbol de Decisión Pacientes - Ejercicio"

        # Cargar datos y entrenar un modelo de árbol de decisión
        df = pd.DataFrame(data)
        df.sample(10)

        df = pd.get_dummies(data=df, drop_first=True)
        df.sample(10)

        explicativas = df.drop(columns='ejercicio')  # Se crea un nuevo dataframe sin la columna clase
        objetivo = df.ejercicio  # Se crea un nuevo dataframe solo con la columna clase

        model = DecisionTreeClassifier(max_depth=3)
        model.fit(X=explicativas, y=objetivo)
        # DecisionTreeClassifier()

        # Generar y guardar el gráfico del árbol
        plt.figure(figsize=(8, 5))
        plot_tree(model, feature_names=explicativas.columns, filled=True)
        plt.savefig("arbol_decision.png", bbox_inches="tight")
        plt.close()

        # Mostrar la imagen en la app de Flet
        imagen_arbol = ft.Image(src="arbol_decision.png", width=600, height=400)

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                imagen_arbol
            ]
        )

