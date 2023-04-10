import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.gui.pages.image.insert_form import InsertForm
from src.gui.pages.image.extract_form import ExtractForm
from src.gui.pages.main_page import MainPage
from src.helper.Navigation import Navigation

def main():
   app = QApplication(sys.argv)
   nav = Navigation()
   insert_form = InsertForm(nav, nav)
   extract_form = ExtractForm(nav, nav)
   main_page = MainPage(nav, nav)
   nav.addWidget("main_page", main_page)
   nav.addWidget("insert_form", insert_form)
   nav.addWidget("extract_form", extract_form)
   nav.go_to("main_page")
   nav.show()
   nav.adjustSize()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()