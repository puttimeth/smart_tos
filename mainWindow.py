from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit
from threading import Thread
import data
from terminalColorize import colorize, Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TOS Android Controller")
        self.resize(200, 100)
        
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        
        self.round_layout = QHBoxLayout()
        self.round_label = QLabel('Round')        
        self.round_layout.addWidget(self.round_label)
        self.round_line_edit = QLineEdit()
        self.round_line_edit.setText("1")
        self.round_layout.addWidget(self.round_line_edit)
        self.layout.addLayout(self.round_layout)

        self.button_layout = QHBoxLayout()
        self.fill_btn = QPushButton("Fill")   
        self.fill_btn.clicked.connect(self.fill_event_btn)
        self.button_layout.addWidget(self.fill_btn)

        self.no_refill_btn = QPushButton("No Refill")
        self.no_refill_btn.clicked.connect(self.no_fill_event_btn)
        self.button_layout.addWidget(self.no_refill_btn)
        self.layout.addLayout(self.button_layout)

        self.status_layout = QHBoxLayout()
        self.status_label = QLabel('status: ')
        self.status_layout.addWidget(self.status_label)
        self.layout.addLayout(self.status_layout)

        self.setCentralWidget(self.widget)
        self.show()

    def event_func(self, action_set, round):
        print(colorize(f'Start {action_set.name}', Color.GREEN))
        for i in range(round):
            print(colorize(f'Round {i+1}', Color.GREEN))
            self.status_label.setText(f'status: {i+1}/{self.get_round()}')
            action_set.resolve()        
        print(colorize(f'End {action_set.name}', Color.GREEN))

    def fill_event_btn(self):
        if data.event_thread and data.event_thread.is_alive():
            data.event_thread_stop = True
            data.event_thread.join()
            data.event_thread_stop = False
        round = self.get_round()
        data.event_thread = Thread(target=self.event_func, args=(data.fill_event_action_set, round))
        data.event_thread.start()

    def no_fill_event_btn(self):
        if data.event_thread and data.event_thread.is_alive():
            data.event_thread_stop = True
            data.event_thread.join()
            data.event_thread_stop = False
        round = self.get_round()
        data.event_thread = Thread(target=self.event_func, args=(data.no_fill_event_action_set, round))
        data.event_thread.start()

    def get_round(self):
        return int(self.round_line_edit.text())