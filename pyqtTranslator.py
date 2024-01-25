import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QWidget, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QApplication, QMessageBox
from googletrans import Translator


class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.translator = Translator()

        self.current_language_label = QLabel('Current Language:')
        self.target_language_label = QLabel('Target Language:')
        self.input_label = QLabel('Type to translate:')
        self.output_label = QLabel('Output:')

        self.current_language_combo = QComboBox()
        self.target_language_combo = QComboBox()

        self.input_text = QTextEdit()
        self.output_text = QTextEdit()

        self.translate_button = QPushButton('Translate')
        self.translate_button.clicked.connect(self.translate_text)

        # You can add more languages here
        # And you can find more languages in:
        # https://github.com/ssut/py-googletrans/blob/master/googletrans/constants.py#L76-L182
        languages = ['en', 'zh-CN', 'fr']
        self.current_language_combo.addItems(languages)
        self.target_language_combo.addItems(languages)

        default_input_language = 'en'
        default_output_language = 'zh-CN'

        self.current_language_combo.setCurrentText(default_input_language)
        self.target_language_combo.setCurrentText(default_output_language)

        layout = QVBoxLayout()
        layout.addWidget(self.current_language_label)
        layout.addWidget(self.current_language_combo)
        layout.addWidget(self.target_language_label)
        layout.addWidget(self.target_language_combo)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.translate_button)

        self.setLayout(layout)

        font = QFont("Arial", 12)
        self.setFont(font)

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Translator By PyQt')

    def translate_text(self):
        input_text = self.input_text.toPlainText()
        current_language = self.current_language_combo.currentText()
        target_language = self.target_language_combo.currentText()

        if not input_text.strip():
            QMessageBox.warning(self, 'Warn', 'Please type in contents！', QMessageBox.Ok)
            return

        translation = self.translator.translate(input_text, src=current_language, dest=target_language)

        self.output_text.setPlainText(translation.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
