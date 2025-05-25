import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow
from datetime import datetime

# Импортируем сгенерированный UI
from GUI.ui_main import Ui_MainWindow

# Импортируем работу с БД
from db_work import DbCommands as Db


def get_curr_time():
    """Получение текущего времени"""
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # инициализируем интерфейс
        self.start_time = None
        self.end_time = None
        self.init_ui()

    def init_ui(self):
        """Инициализация данных и элементов"""
        operators = Db().select_db_info('SELECT name_operator FROM operator')
        for operator in operators:
            self.comboBox_user.addItem(operator[0])  # добавляем оператора в комбобокс

        self.setWindowTitle('Программа-помощник call-центра Центра катлогизации')
        self.comboBox_user.currentIndexChanged.connect(self.on_combo_changed)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_call_start.clicked.connect(lambda: self.choose_page(page_index=1))
        self.pushButton_call_end.clicked.connect(lambda: self.choose_page(page_index=0))
        self.lineEdit_ispolnitel_poisk.setPlaceholderText('Поле для поиска организации')
        self.lineEdit_ispolnitel.setPlaceholderText('Итоговое поле для заполнения')
        self.pushButton_open_excel.clicked.connect(lambda: self.open_excel())

    def on_combo_changed(self, index):
        print(f"Выбран оператор: {self.comboBox_user.itemText(index)}")

    def closeEvent(self, event):
        """Завершение работы при закрытии окна"""
        print("Приложение закрывается...")
        # Можно вызвать Db().close_connection(), если нужно
        event.accept()
        QApplication.quit()

    def choose_page(self, page_index):
        if page_index == 1:
            self.start_time = get_curr_time()
            self.lineEdit_time_start.setText(self.start_time)
        elif page_index == 0:
            self.end_time = get_curr_time()
            delta_time = datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(self.start_time,
                                                                                                   "%Y-%m-%d %H:%M:%S")
            print(str(delta_time))
        self.stackedWidget.setCurrentIndex(page_index)

    def open_excel(self):
        # Укажи путь к твоему файлу здесь
        file_path = "otchet.xlsx"

        # Открываем файл стандартной программой Windows
        url = QUrl.fromLocalFile(file_path)
        QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
