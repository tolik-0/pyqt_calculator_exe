import sys
from typing import Dict
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


ERROR_MSG = "ERROR"


def resource_path(relative: str) -> Path:
    """
    Resolve path to a bundled resource (works in PyInstaller onefile).
    """
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base_path / relative


class PyCalcUi(QWidget):
    """Calculator user interface."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt Calculator")
        self.setFixedSize(300, 300)
        icon_path = resource_path("calculator.ico")
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))
        self.general_layout = QGridLayout()
        self.setLayout(self.general_layout)
        self._create_display()
        self._create_buttons()

    def _create_display(self) -> None:
        """Create calculator display."""
        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.general_layout.addWidget(self.display, 0, 0, 1, 4)

    def _create_buttons(self) -> None:
        """Create calculator buttons."""
        self.buttons: Dict[str, QPushButton] = {}
        buttons_layout = {
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "/": (1, 3),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "*": (2, 3),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "-": (3, 3),
            "0": (4, 0),
            ".": (4, 1),
            "C": (4, 2),
            "+": (4, 3),
            "=": (5, 0),
        }
        for btn_text, pos in buttons_layout.items():
            button = QPushButton(btn_text)
            button.setFixedSize(60, 40)
            self.buttons[btn_text] = button
            if btn_text == "=":
                self.general_layout.addWidget(button, pos[0], pos[1], 1, 4)
            else:
                self.general_layout.addWidget(button, pos[0], pos[1])

    def set_display_text(self, text: str) -> None:
        """Set display text."""
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self) -> str:
        """Get display text."""
        return self.display.text()

    def clear_display(self) -> None:
        """Clear display."""
        self.set_display_text("")


class PyCalc:
    """Controller for the calculator application."""

    def __init__(self, model_eval) -> None:
        self._evaluate = model_eval
        self._ui = PyCalcUi()
        self._connect_signals()

    def _calculate_result(self) -> None:
        """Evaluate the current expression."""
        result = self._evaluate(expression=self._ui.display_text())
        self._ui.set_display_text(result)

    def _build_expression(self, sub_exp: str) -> None:
        """Append a sub-expression to the current expression."""
        expression = self._ui.display_text() + sub_exp
        self._ui.set_display_text(expression)

    def _connect_signals(self) -> None:
        """Connect buttons to actions."""
        for btn_text, button in self._ui.buttons.items():
            if btn_text not in {"=", "C"}:
                button.clicked.connect(lambda _, text=btn_text: self._build_expression(text))
        self._ui.buttons["="].clicked.connect(self._calculate_result)
        self._ui.buttons["C"].clicked.connect(self._ui.clear_display)
        self._ui.display.returnPressed.connect(self._calculate_result)

    def show(self) -> None:
        """Show the calculator UI."""
        self._ui.show()


def evaluate_expression(expression: str) -> str:
    """Evaluate a math expression safely and return result as string."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


def main() -> None:
    """Entry point for the calculator application."""
    pycalc = QApplication(sys.argv)
    icon_path = resource_path("calculator.ico")
    if icon_path.exists():
        pycalc.setWindowIcon(QIcon(str(icon_path)))
    calculator = PyCalc(evaluate_expression)
    calculator.show()
    sys.exit(pycalc.exec())


if __name__ == "__main__":
    main()
