import tkinter as tk
import subprocess
import winreg

class BuscadorGoogle:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Buscador Google")
        self.ventana.geometry("300x300")
        self.ventana.wm_minsize(300, 300)

        label_google = tk.Label(self.ventana, text="GOOGLE", font=("Arial", 24))
        label_google.pack(pady=20)

        self.entry_busqueda = tk.Entry(self.ventana)
        self.entry_busqueda.pack(pady=10)

        self.configurar_botones()

    def configurar_botones(self):
        boton_buscar = tk.Button(self.ventana, text="Buscar", command=self.buscar)
        boton_buscar.pack(pady=10)

        boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
        boton_limpiar.pack(pady=5)

    def is_url(self, termino):
        if termino.startswith(("http://", "https://", "www.")):
            return True
        if "." in termino:
            parts = termino.split(".")
            if len(parts[-1]) == 3 and parts[-1].isalpha():
                return True
        return False

    def abrir_google_chrome(self, url):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe") as key:
                chrome_path = winreg.QueryValue(key, None)
                subprocess.call([chrome_path, url])
        except Exception as e:
            print(f"Error al abrir Google Chrome: {e}")

    def buscar(self):
        termino_busqueda = self.entry_busqueda.get()
        if self.is_url(termino_busqueda):
            self.abrir_google_chrome(termino_busqueda)
        else:
            url_google = f"https://www.google.com/search?q={termino_busqueda}"
            self.abrir_google_chrome(url_google)

    def limpiar(self):
        self.entry_busqueda.delete(0, tk.END)

def main():
    ventana = tk.Tk()
    app = BuscadorGoogle(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
