import tkinter as tk
import requests
from tkinter import messagebox


class DAO:
    def __init__(self):
        self.__url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def ultimo_dato(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[-1]
        return None


class Ultimo:
    def __init__(self, tilino):
        self.__tilino = tilino
        self.__tilino.title("Último Dato")
        self.__tilino.geometry("300x200")

        self.__etiqueta_datos = tk.Label(self.__tilino, text="Último Dato", justify="left")
        self.__etiqueta_datos.pack(pady=20)

        self.__boton_cargar = tk.Button(self.__tilino, text="Cargar Último Dato", command=self.__mostrar)
        self.__boton_cargar.pack(pady=10)

    def __mostrar(self):
        dao = DAO()
        ultimo_dato = dao.ultimo_dato()

        if ultimo_dato:

            datos = (
                f"ID: {ultimo_dato['id']}\n"
                f"Nombre: {ultimo_dato['nombre']}\n"
                f"Apellido: {ultimo_dato['apellido']}\n"
                f"Ciudad: {ultimo_dato['ciudad']}\n"
                f"Calle: {ultimo_dato['calle']}"
            )
            self.__etiqueta_datos.config(text=datos)
        else:
            messagebox.showerror("Error", "No se pudo obtener el último dato.")
















