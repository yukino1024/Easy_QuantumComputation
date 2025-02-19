import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox, QComboBox, QLabel, QTabWidget, QTextEdit
from PyQt5.QtGui import QFont
from DirGeneration import DTF_gen, CAS_gen
from config import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('自动创建 .in 文件')
        self.setFixedWidth(WINDOW_WIDTH)  # 设置固定宽度
        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_dft_tab(), "DFT")
        self.tabs.addTab(self.create_cas_tab(), "CAS")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def create_dft_tab(self):
        dft_tab = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        font = QFont()
        font.setPointSize(12)

        self.path_input = QLineEdit()
        self.path_input.setFont(font)
        self.path_button = QPushButton('选择路径')
        self.path_button.setFont(font)
        self.path_button.clicked.connect(self.select_path)

        self.nprocshared_input = QLineEdit('8')
        self.nprocshared_input.setFont(font)
        self.charge_input = QLineEdit('0')
        self.charge_input.setFont(font)
        self.multiplicity_input = QLineEdit('1')
        self.multiplicity_input.setFont(font)
        self.title_input = QLineEdit('No Title')
        self.title_input.setFont(font)

        self.func_input = QComboBox()
        self.func_input.setFont(font)
        self.func_input.addItems(DFT_FUNCTIONS)

        self.basis_input = QComboBox()
        self.basis_input.setFont(font)
        self.basis_input.addItems(DFT_BASIS_SETS)

        self.type_input = QComboBox()
        self.type_input.setFont(font)
        self.type_input.addItems(DFT_TYPES)

        self.solvent_input = QLineEdit('False')
        self.solvent_input.setFont(font)

        form_layout.addRow(QLabel('路径:', font=font), self.path_input)
        form_layout.addRow('', self.path_button)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('核数:', font=font))
        hbox1.addWidget(self.nprocshared_input)
        form_layout.addRow(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('电荷:', font=font))
        hbox2.addWidget(self.charge_input)
        hbox2.addWidget(QLabel('多重性:', font=font))
        hbox2.addWidget(self.multiplicity_input)
        form_layout.addRow(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('标题:', font=font))
        hbox3.addWidget(self.title_input)
        form_layout.addRow(hbox3)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(QLabel('函数:', font=font))
        hbox4.addWidget(self.func_input)
        form_layout.addRow(hbox4)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(QLabel('基组:', font=font))
        hbox5.addWidget(self.basis_input)
        form_layout.addRow(hbox5)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(QLabel('类型:', font=font))
        hbox6.addWidget(self.type_input)
        form_layout.addRow(hbox6)

        hbox7 = QHBoxLayout()
        hbox7.addWidget(QLabel('溶剂:', font=font))
        hbox7.addWidget(self.solvent_input)
        form_layout.addRow(hbox7)

        layout.addLayout(form_layout)

        self.generate_dft_button = QPushButton('生成 .in 文件')
        self.generate_dft_button.setFont(font)
        self.generate_dft_button.clicked.connect(self.generate_dft_file)
        layout.addWidget(self.generate_dft_button)

        dft_tab.setLayout(layout)
        return dft_tab

    def create_cas_tab(self):
        cas_tab = QWidget()
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        font = QFont()
        font.setPointSize(12)

        self.path_input_cas = QLineEdit()
        self.path_input_cas.setFont(font)
        self.path_button_cas = QPushButton('选择路径')
        self.path_button_cas.setFont(font)
        self.path_button_cas.clicked.connect(self.select_path_cas)

        self.nprocshared_input_cas = QLineEdit('8')
        self.nprocshared_input_cas.setFont(font)
        self.charge_input_cas = QLineEdit('0')
        self.charge_input_cas.setFont(font)
        self.multiplicity_input_cas = QLineEdit('1')
        self.multiplicity_input_cas.setFont(font)
        self.title_input_cas = QLineEdit('No Title')
        self.title_input_cas.setFont(font)

        self.ele_input = QLineEdit('4')
        self.ele_input.setFont(font)
        self.orb_input = QLineEdit('4')
        self.orb_input.setFont(font)
        self.basis_input_cas = QComboBox()
        self.basis_input_cas.setFont(font)
        self.basis_input_cas.addItems(CAS_BASIS_SETS)
        self.opt_input = QLineEdit('False')
        self.opt_input.setFont(font)

        self.chk_input = QComboBox()
        self.chk_input.setFont(font)
        self.chk_input.addItems(CHK_OPTIONS)
        self.chk_input.currentIndexChanged.connect(self.toggle_chk)

        self.alter_input = QComboBox()
        self.alter_input.setFont(font)
        self.alter_input.addItems(ALTER_OPTIONS)
        self.alter_input.currentIndexChanged.connect(self.toggle_alter)

        self.alter_text = QTextEdit()
        self.alter_text.setFont(font)
        self.alter_text.setVisible(False)

        form_layout.addRow(QLabel('路径:', font=font), self.path_input_cas)
        form_layout.addRow('', self.path_button_cas)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('核数:', font=font))
        hbox1.addWidget(self.nprocshared_input_cas)
        form_layout.addRow(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('电荷:', font=font))
        hbox2.addWidget(self.charge_input_cas)
        hbox2.addWidget(QLabel('多重性:', font=font))
        hbox2.addWidget(self.multiplicity_input_cas)
        form_layout.addRow(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(QLabel('标题:', font=font))
        hbox3.addWidget(self.title_input_cas)
        form_layout.addRow(hbox3)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(QLabel('电子:', font=font))
        hbox4.addWidget(self.ele_input)
        hbox4.addWidget(QLabel('轨道:', font=font))
        hbox4.addWidget(self.orb_input)
        form_layout.addRow(hbox4)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(QLabel('基组:', font=font))
        hbox5.addWidget(self.basis_input_cas)
        form_layout.addRow(hbox5)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(QLabel('优化（填优化圈数）:', font=font))
        hbox6.addWidget(self.opt_input)
        form_layout.addRow(hbox6)

        hbox7 = QHBoxLayout()
        hbox7.addWidget(QLabel('使用chk文件:', font=font))
        hbox7.addWidget(self.chk_input)
        form_layout.addRow(hbox7)

        hbox8 = QHBoxLayout()
        hbox8.addWidget(QLabel('调换轨道:', font=font))
        hbox8.addWidget(self.alter_input)
        form_layout.addRow(hbox8)

        self.alter_text_label = QLabel('调换轨道列表:', font=font)
        self.alter_text_label.setVisible(False)
        form_layout.addRow(self.alter_text_label, self.alter_text)

        layout.addLayout(form_layout)

        self.generate_cas_button = QPushButton('生成 .in 文件')
        self.generate_cas_button.setFont(font)
        self.generate_cas_button.clicked.connect(self.generate_cas_file)
        layout.addWidget(self.generate_cas_button)

        cas_tab.setLayout(layout)
        return cas_tab

    def toggle_chk(self):
        pass  # 可以在这里添加任何需要的逻辑

    def toggle_alter(self):
        if self.alter_input.currentText() == '是':
            self.alter_text.setVisible(True)
            self.alter_text_label.setVisible(True)
        else:
            self.alter_text.setVisible(False)
            self.alter_text_label.setVisible(False)

    def select_path(self):
        path = QFileDialog.getExistingDirectory(self, '选择文件夹', '')
        if path:
            self.path_input.setText(path)

    def select_path_cas(self):
        path = QFileDialog.getExistingDirectory(self, '选择文件夹', '')
        if path:
            self.path_input_cas.setText(path)

    def generate_dft_file(self):
        path = self.path_input.text()
        nprocshared = int(self.nprocshared_input.text())
        charge = int(self.charge_input.text())
        multiplicity = int(self.multiplicity_input.text())
        title = self.title_input.text()
        func = self.func_input.currentText()
        basis = self.basis_input.currentText()
        type_ = self.type_input.currentText()
        solvent = self.solvent_input.text()

        generator = DTF_gen(path, nprocshared, charge, multiplicity, title, func, basis, type_, solvent)
        generator.creat_file()

        QMessageBox.information(self, '成功', '文件生成成功！')

    def generate_cas_file(self):
        path = self.path_input_cas.text()
        nprocshared = int(self.nprocshared_input_cas.text())
        charge = int(self.charge_input_cas.text())
        multiplicity = int(self.multiplicity_input_cas.text())
        title = self.title_input_cas.text()
        ele = int(self.ele_input.text())
        orb = int(self.orb_input.text())
        basis = self.basis_input_cas.currentText()
        opt = self.opt_input.text()
        chk = self.chk_input.currentText() == '是'
        alter = self.alter_input.currentText() == '是'
        alter_list = self.alter_text.toPlainText().split('\n') if alter else False

        generator = CAS_gen(path, nprocshared, charge, multiplicity, title, ele, orb, basis, opt, chk, alter_list)
        generator.creat_file()

        QMessageBox.information(self, '成功', '文件生成成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())