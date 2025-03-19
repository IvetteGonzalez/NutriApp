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
                        label="Name",
                        autofill_hints=ft.AutofillHint.NAME,
                    ),
                    ft.TextField(
                        label="Email",
                        autofill_hints=[ft.AutofillHint.EMAIL],
                    ),
                    ft.TextField(
                        label="Phone Number",
                        autofill_hints=[ft.AutofillHint.TELEPHONE_NUMBER],
                    ),
                    ft.TextField(
                        label="Street Address",
                        autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,
                    ),
                    ft.TextField(
                        label="Postal Code",
                        autofill_hints=ft.AutofillHint.POSTAL_CODE,
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





