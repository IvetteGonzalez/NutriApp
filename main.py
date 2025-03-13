import flet as ft
from home import UINutricion
from pacientes import  UIPacientes
from reportes import UIReportes

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change  # Detectar cambios de ruta
        self.page.go(page.route)  # Cargar la ruta inicial

    def route_change(self, e):
        self.page.views.clear()  # Limpiar vistas antes de agregar la nueva

        if self.page.route == "/":
            self.page.views.append(UINutricion(self.page))
        elif self.page.route == "/pacientes":
            self.page.views.append(UIPacientes(self.page))
        elif self.page.route == "/reportes":
            self.page.views.append(UIReportes(self.page))

        self.page.update()  # Actualizar la UI

# Ejecutar la aplicación
def main(page: ft.Page):
    MyApp(page)

ft.app(target=main)