import sys
sys.path.insert(1, 'C:\\Users\\T3lk0m53l\\Documents\\Code\\Stegano')
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.gui.component.ChooseImage import ChooseImage
from src.gui.component.ChooseAssembler import ChooseAssembler
from src.gui.component.ChooseSteganoMethod import ChooseSteganoMethod
from src.gui.component.ChooseEncodeMethod import ChooseEncodeMethod
from src.gui.component.ChooseFolderDestination import ChooseFolderDestination
from src.gui.pages.image.insert_form import InsertForm
from src.gui.pages.image.extract_form import ExtractForm
from src.gui.pages.main_page import MainPage

def main():
   app = QApplication(sys.argv)
   main_widget = QWidget()
   # choose_image = ChooseImage(main_widget)
   # choose_assembler = ChooseAssembler(main_widget)
   # choose_stegano_method = ChooseSteganoMethod(main_widget)
   # choose_encode_method = ChooseEncodeMethod(main_widget)
   # choose_folder_destination = ChooseFolderDestination(main_widget)
   # insert_form = InsertForm(main_widget)
   # extract_form = ExtractForm(main_widget)
   main_page = MainPage(main_widget)
   main_widget.show()
   main_widget.adjustSize()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()