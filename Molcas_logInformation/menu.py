import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QMessageBox
from molcas_log import do_write

class LogWriteGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('molcas log 转 excel')
        self.resize(400, 150)
        self.layout = QVBoxLayout()
        self.label = QLabel('请选择 molcas log 文件：')
        self.layout.addWidget(self.label)
        self.button = QPushButton('选择并导出Excel')
        self.button.clicked.connect(self.select_and_write)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def select_and_write(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择 log 文件', '', 'Log Files (*.log);;All Files (*)')
        if file_path:
            self.label.setText(f'已选择: {file_path}')
            try:
                do_write(file_path)
                QMessageBox.information(self, '成功', '已生成Excel文件！')
            except Exception as e:
                QMessageBox.critical(self, '错误', f'生成Excel失败：{e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogWriteGUI()
    window.show()
    sys.exit(app.exec_())
