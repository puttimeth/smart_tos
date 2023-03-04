from PyQt5.QtWidgets import QMainWindow, QPushButton
import data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TOS Android Controller")
        self.resize(200,100)

        self.power_btn = QPushButton("active")
        self.power_btn.setCheckable(True)
        self.power_btn.setChecked(True)        
        data.PROGRAM_LISTEN = self.power_btn.isChecked()
        self.power_btn.setStyleSheet('''
        QPushButton {background-color:#FFD8CE; font-size:25px}
        QPushButton:checked {background-color:#BDFFD6}
        ''')
        self.power_btn.toggled.connect(self.toggle_power_btn)

        self.setCentralWidget(self.power_btn)
        self.show()
    
    def toggle_power_btn(self):
        data.PROGRAM_LISTEN = self.power_btn.isChecked()
        if self.power_btn.isChecked():
            self.power_btn.setText("active")
            print(f'Program is now listen.')
        else:
            self.power_btn.setText("inactive")
            print(f'Program is now deaf.')