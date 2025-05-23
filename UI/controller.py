import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        name = self._view.txt_distanza
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return

        self._view.update_page()
