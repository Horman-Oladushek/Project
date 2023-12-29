import io
import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt5.QtCore import Qt

# СЮДА UIC
# вид главного окна "Main_Window"
main_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1115</width>
    <height>862</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>20</y>
      <width>661</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>36</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Магазин Электронники</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="listOfItems">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>160</y>
      <width>1011</width>
      <height>591</height>
     </rect>
    </property>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <row>
     <property name="text">
      <string>New Row</string>
     </property>
    </row>
    <column>
     <property name="text">
      <string>New Column</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>112</string>
     </property>
    </column>
   </widget>
   <widget class="QPushButton" name="EnterBTN_Main">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>80</y>
      <width>81</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
    <property name="checkable">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLineEdit" name="SearchLine">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>130</y>
      <width>811</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>130</y>
      <width>81</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Поиск:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="SearchBTN">
    <property name="geometry">
     <rect>
      <x>980</x>
      <y>127</y>
      <width>81</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Найти</string>
    </property>
   </widget>
   <widget class="QLabel" name="login">
    <property name="geometry">
     <rect>
      <x>910</x>
      <y>10</y>
      <width>181</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="update">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>90</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Обновить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>760</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="dell">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>760</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Удалить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1115</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
# Вид окна со входом в аккаунт
enter_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>656</width>
    <height>418</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>30</y>
      <width>81</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>22</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Вход</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login_edit">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>130</y>
      <width>451</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="login">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>130</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Логин:</string>
    </property>
   </widget>
   <widget class="QLabel" name="password">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>210</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Пароль:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="password_edit">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>210</y>
      <width>451</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="admin_enter">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>0</y>
      <width>261</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Sitka Small</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Войти как Администратор</string>
    </property>
   </widget>
   <widget class="QPushButton" name="user_enter">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>280</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLabel" name="format">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>240</y>
      <width>501</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Times New Roman</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>656</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
# окно с добавлением новых товаров в базу данных
add_del_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>697</width>
    <height>258</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="name">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>40</y>
      <width>511</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="cost">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>80</y>
      <width>511</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="count">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>120</y>
      <width>511</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="where">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>150</y>
      <width>511</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_name">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>40</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Наименование товара:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_cost">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>80</y>
      <width>81</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Цена товара:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_count">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>120</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Количество товара:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_where">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>150</y>
      <width>161</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Где доступен для вывоза:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="addButton">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>180</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_dell">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>70</y>
      <width>611</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>которого вы хотите удалить (пишите название товара полность, в соответствии с базой данных)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="dellButton">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>100</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Удалить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>697</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

# СЮДА UIC


data = []  # Для работы с username и проверки админа


class Main_Window(QMainWindow):  # Главное окно, с базой данных, поиском, входом, а так же
    # изменением списка, админом
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_window)
        uic.loadUi(f, self)
        self.loadTable('Base.csv')

        self.EnterBTN_Main.clicked.connect(self.enter)
        self.SearchBTN.clicked.connect(self.search)
        self.update.clicked.connect(self.update_data)
        self.add.hide()
        self.dell.hide()
        self.add.clicked.connect(self.add_del)
        self.dell.clicked.connect(self.add_del)

    def loadTable(self, table_name):  # загрузка таблицы базы данных
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.listOfItems.setColumnCount(len(title))
            self.listOfItems.setHorizontalHeaderLabels(title)
            header = self.listOfItems.horizontalHeader()  # растягиваем таблицу
            header.setStretchLastSection(True)
            self.listOfItems.setRowCount(0)
            for i, row in enumerate(reader):
                self.listOfItems.setRowCount(
                    self.listOfItems.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.listOfItems.setItem(
                        i, j, QTableWidgetItem(elem))
        self.listOfItems.resizeColumnsToContents()

    def search(self, s):  # Поиск в базе данных
        # Отчищаем выбранные поля.
        self.listOfItems.setCurrentItem(None)
        s_l = self.SearchLine.text()

        if s_l == '':
            # пусто, ничего не выделяем.
            return

        matching_items = self.listOfItems.findItems(s_l, Qt.MatchContains)
        if matching_items:
            # Что-то нашли.
            for item in matching_items:
                item.setSelected(True)

    def enter(self):  # открытие окна для входа в акаунт
        self.e_w = Enter_Window(self)
        self.e_w.show()
        Main_Window.hide(self)

    def user_update(self):  # Изменение кнопки входа, а так же username в главном окне
        self.login.setText(data[0])
        self.EnterBTN_Main.setText('Войти в другой аккаунт')
        self.EnterBTN_Main.setGeometry(770, 80, 295, 41)
        if self.admin:
            self.add.show()
            self.dell.show()
        else:
            self.add.hide()
            self.dell.hide()

    def update_data(self):  # Обновление базы данных с товаром, а так же проверка аккаунта на админа
        global data
        if data != []:
            self.data_user = data
            with open('Base_adm.csv', encoding='utf8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for j in reader:
                    if self.data_user == j:
                        self.admin = True
                    else:
                        self.admin = False
            self.user_update()
            self.loadTable('Base.csv')
        else:
            self.login.setText('Не удалось войти')

    def add_del(self):  # Окно с добавлением новых и удалением старых товаров в базу данных
        self.a_w = Add_del_Window(self)
        self.a_w.show()
        Main_Window.hide(self)


class Enter_Window(QMainWindow):  # Окно входа в систему
    def __init__(self, parent=None):
        super().__init__(parent)
        f_1 = io.StringIO(enter_window)
        uic.loadUi(f_1, self)
        self.user_enter.clicked.connect(self.enter_user)
        self.admin_enter.clicked.connect(self.enter_user)

    def enter_user(self): #вход в систему
        data_1 = []
        global data
        if self.sender().text() == 'Войти как Администратор':
            base_users = 'Base_adm.csv'
        if self.sender().text() == 'Войти':
            base_users = 'Base_users.csv'
        with open(base_users, encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            if self.login_edit.text() == '' and self.password_edit.text() == '':  # Проверка пароля и логина на
                # пустое поле
                self.format.setText('Неверный формат логина или пароля')
            for s in self.login_edit.text():  # проверка знаков на кириллицу и знаки
                if s.isascii() is False:
                    log_flag = False
                    self.format.setText('Неверный формат логина')
                    break
                else:
                    log_flag = True
            if self.login_edit.text() != '' and log_flag is True and self.password_edit.text() != '':
                for x in reader:
                    if self.login_edit.text() in x:
                        data_1 = x
                        if self.login_edit.text() == data_1[0] and self.password_edit.text() == data_1[1]:  # проверка
                            # совпадения пароля, который записан в системе
                            data = x
                            break
            form.show()
            Enter_Window.close(self)


class Add_del_Window(QMainWindow):  # окно с добавлением товаров в базу данных
    def __init__(self, parent=None):
        super().__init__(parent)
        f_1 = io.StringIO(add_del_window)
        uic.loadUi(f_1, self)
        if self.sender().text() == 'Добавить':
            self.label_dell.hide()
            self.dellButton.hide()
            self.label_cost.show()
            self.cost.show()
            self.label_count.show()
            self.count.show()
            self.label_where.show()
            self.where.show()
            self.addButton.show()
            self.addButton.clicked.connect(self.add_col)
        else:
            self.label_cost.hide()
            self.cost.hide()
            self.label_count.hide()
            self.count.hide()
            self.label_where.hide()
            self.where.hide()
            self.addButton.hide()
        if self.sender().text() == 'Удалить':
            self.label_dell.show()
            self.dellButton.show()
            self.dellButton.clicked.connect(self.dell_col)

    def add_col(self):  # процесс добавление товаров
        base = []
        with open('Base.csv', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for j in reader:
                base.append(j)
            with open("Base.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
                for k in base:
                    file_writer.writerow(k)
                end = []
                end.append(self.name.text())
                end.append(self.cost.text())
                end.append(self.count.text())
                end.append(self.where.text())
                file_writer.writerow(end)
        form.show()
        Add_del_Window.close(self)

    def dell_col(self):
        base = []
        with open('Base.csv', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for j in reader:
                base.append(j)
            with open("Base.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
                for k in base:
                    if self.name.text() == k[0]:
                        pass
                    else:
                        file_writer.writerow(k)
        form.show()
        Add_del_Window.close(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main_Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
