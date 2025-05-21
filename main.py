import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Импортируем сгенерированный UI
from GUI.ui_main import Ui_MainWindow

# Импортируем работу с БД
from db_work import DbCommands as Db


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # инициализируем интерфейс

        self.init_ui()

    def init_ui(self):
        """Инициализация данных и элементов"""
        operators = Db().select_db_info('SELECT name_operator FROM operator')
        for operator in operators:
            self.comboBox_user.addItem(operator[0])  # добавляем оператора в комбобокс

        # Можно подключить сигналы здесь
        self.comboBox_user.currentIndexChanged.connect(self.on_combo_changed)

    def on_combo_changed(self, index):
        print(f"Выбран оператор: {self.comboBox_user.itemText(index)}")

    def closeEvent(self, event):
        """Завершение работы при закрытии окна"""
        print("Приложение закрывается...")
        # Можно вызвать Db().close_connection(), если нужно
        event.accept()
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())