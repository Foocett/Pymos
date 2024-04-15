import sys
import numpy as np
import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphing Software")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Equation Entry
        self.equation_label = QLabel("Enter Equation:")
        self.equation_entry = QLineEdit()
        layout.addWidget(self.equation_label)
        layout.addWidget(self.equation_entry)

        # Plot Button
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        # Graph Display
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.central_widget.setLayout(layout)

    def plot_graph(self):
        equation = self.equation_entry.text()
        x = np.linspace(-10, 10, 400)
        try:
            y = eval(equation)
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Graph of " + equation)
            ax.set_aspect('equal', adjustable='box')
            self.canvas.draw()
        except Exception as e:
            print("Error:", e)


def main():
    app = QApplication(sys.argv)
    window = GraphingApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
