from PyQt6.QtWidgets import QApplication
from logic import *


def main() -> None:
    """Creates and Runs the GUI."""
    application: QApplication = QApplication([])
    window: Logic = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
