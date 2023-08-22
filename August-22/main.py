import os
from PyQt5.QtCore import QLibraryInfo
from PyQt5.QtWidgets import *

def set_qt_plugin_path():
    # qta_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
    # qta_path = qta_path.encode("latin").decode("utf-8")
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"


set_qt_plugin_path()

app = QApplication([])
window = QMainWindow()

label = QLabel('Hello from Qt!')

window.setCentralWidget(label)
window.show()
app.exec()
