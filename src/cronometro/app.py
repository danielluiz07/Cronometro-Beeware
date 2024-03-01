import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import threading

class CronometroApp(toga.App):
    def startup(self):
        # Configuração da Janela
        self.main_window = toga.MainWindow(title='Cronômetro', size=(150, 100))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Configuração dos componentes
        self.tempo = toga.Label('0:00', style=Pack(padding=5))
        self.botao_iniciar = toga.Button("Iniciar", on_press=self.iniciar_cronometro, style=Pack(padding=5))
        self.botao_parar = toga.Button("Parar", on_press=self.parar_cronometro, style=Pack(padding=5))

        main_box.add(
            self.tempo,
            self.botao_iniciar,
            self.botao_parar
        )

        self.main_window.content = main_box
        self.main_window.show()

    def iniciar_cronometro(self, widget):
        self.tempo_segundos = 0
        self.atualizar_tempo()

    def parar_cronometro(self, widget):
        if hasattr(self, 'timer') and self.timer.is_alive():
            self.timer.cancel()

    def atualizar_tempo(self):
        minutos = self.tempo_segundos // 60
        segundos = self.tempo_segundos % 60
        self.tempo.text = f'{minutos}:{segundos:02d}'
        self.tempo_segundos += 1
        self.timer = threading.Timer(1.0, self.atualizar_tempo)
        self.timer.start()

def main():
    return CronometroApp()

if __name__ == '__main__':
    main().main_loop()