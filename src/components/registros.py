import flet as ft


class MyForm(ft.Container):
    def __init__(self):
        super().__init__()
        # Variables
        self.bgcolor = ft.Colors.WHITE
        self.color = ft.Colors.GREEN_800

        self.formulario = ft.AutofillGroup(
            ft.Column(
                controls=[
                    ft.TextField(
                        label="Nombre Completo",
                        autofill_hints=ft.AutofillHint.NAME,
                    ),
                    ft.TextField(
                        label="Edad",
                        autofill_hints=[ft.AutofillHint.BIRTHDAY],
                    ),
                    ft.TextField(
                        label="Genero",
                        autofill_hints=[ft.AutofillHint.GENDER],
                    ),
                    ft.TextField(
                        label="Peso (kg)",
                        autofill_hints=ft.AutofillHint.TRANSACTION_AMOUNT,
                    ),
                    ft.TextField(
                        label="Altura (m)",
                        autofill_hints=ft.AutofillHint.TRANSACTION_AMOUNT,
                    ),
                ]
            )
        )

        self.save = ft.ElevatedButton(text="GUARDAR",
                                      on_click=print("Guardar"))


        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.alignment.center,
            controls=[
                self.formulario,
                self.save
            ]
        )





