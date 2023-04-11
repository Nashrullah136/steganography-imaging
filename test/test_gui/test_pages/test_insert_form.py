import sys
sys.path.insert(1, 'C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano')
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.assembler.ImageAssembler import ImageAssembler
from src.encoder.compression.DeflateEncoder import DeflateEncoder
from src.gui.pages.image.insert_form import InsertForm

def main():
   app = QApplication(sys.argv)
   main_widget = QWidget()
   insert_form = InsertForm(main_widget)
   insert_form.choose_secret_image.image = "C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano\\test\\test_sample\\lenna.png"
   insert_form.choose_vessel_image.image = "C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano\\test\\test_sample\\vessel_img.bmp"
   insert_form.choose_assembler.assembler = ImageAssembler()
   insert_form.choose_encoder.encoder.append(DeflateEncoder())
   insert_form.choose_stegano_method.combo_box.setCurrentIndex(1)
   parameter_widget : QDoubleSpinBox = insert_form.choose_stegano_method.all_parameter_ui.currentWidget().findChild(QDoubleSpinBox)
   parameter_widget.setValue(0.3)
   insert_form.choose_folder_destination.folder = "C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano\\test\\test_sample"
   main_widget.show()
   main_widget.adjustSize()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()