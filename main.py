from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
window = loader.load("UI/main.ui")
window.show()
app.exec()