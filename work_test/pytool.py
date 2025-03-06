import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


def load_ui_file(ui_file_path, parent=None):
    loader = QUiLoader()
    file = QFile(ui_file_path)
    if not file.open(QFile.ReadOnly | QFile.Text):
        print(f"Cannot open {ui_file_path}: {file.errorString()}")
        sys.exit(-1)

    window = loader.load(file, parent)
    file.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)

    return window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_path = "testtool.ui"  # 替换为你的 .ui 文件路径
    mainWindow = load_ui_file(ui_file_path)
    mainWindow.show()
    sys.exit(app.exec())
