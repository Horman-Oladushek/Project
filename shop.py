import io
import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt5.QtCore import Qt

data = []  # Для работы с username и проверки админа


class Main_Window(QMainWindow):  # Главное окно, с базой данных, поиском, входом, а так же
    # изменением списка базы данных под аккаунтом админа
    def __init__(self):
        super().__init__()
        uic.loadUi('style/Main_Wdindow.ui', self)
        self.loadTable('deleted_files/Base.csv')

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
            self.listOfItems.horizontalHeader().setStretchLastSection(True)  # растягиваем таблицу
            # header.setStretchLastSection(True)
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
            with open('deleted_files/Base_adm.csv', encoding='utf8') as csvfile:
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
        super().__init__()
        uic.loadUi('style/Enter_Window.ui', self)
        # self.password_conf.hide() # ТЕКСТ ПОДТВЕРЖДЕНИЕ ПАРОЛЯ
        # self.password_conf_edit.hide() # ПОЛЕ ПОДТВЕРЖДЕНИЕ ПАРОЛЯ
        # self.reg.clicked.connect(self.registr) БЫЛА КНОПКА РЕГИСТРАЦИИ
        # self.user_enter.clicked.connect(self.enter_user) БЫЛА КНОПКА ВХОДА В АККАУНТ ПОЛЬЗОВАТЕЛЯ
        self.admin_enter.clicked.connect(self.enter_user)

    # def registr(self): #регистрация нового пользователя
    #     data_user = []
    #     log_flag = True
    #
    #     self.admin_enter.hide()
    #     self.user_enter.hide()
    #
    #     self.password_conf.show()
    #     self.password_conf_edit.show()
    #
    #     with open('Base_users.csv', encoding='utf8') as csvfile:
    #         reader = csv.reader(csvfile, delimiter=';')
    #         for j in reader:
    #             data_user.append(j)
    #             if self.login_edit.text() in j: #сверка с базой данных, есть ли уже пользователи с таким логином
    #                 self.format.setText('Такой логин уже зарегестрирован')
    #                 log_flag = False
    #                 break
    #         if self.password_conf_edit.text() == '': #проверка строки с подтверждением пароля
    #             log_flag = False
    #         if self.password_edit.text() == self.password_conf_edit.text() and log_flag is True:
    #             if self.login_edit.text() != '' and self.password_edit.text() != '' and (
    #                     self.password_conf_edit.text() != ''):
    #                 for s in self.login_edit.text(): #проверка на знаки и буквы в логине
    #                     if s.isascii() is True:
    #                         log_flag = True
    #                     else:
    #                         log_flag = False
    #                         self.format.setText('Неверный формат логина')
    #                         break
    #             else:
    #                 self.format.setText('Все строчки пусты')
    #         else:
    #             self.format.setText('Ошибка в логине или пароле')
    #
    #         if log_flag is True:
    #             self.format.setText('Регистрация Успешна!')
    #             self.user_enter.show()
    #             self.password_conf_edit.hide()
    #             self.password_conf.hide()
    #             end = []
    #             end.append(self.login_edit.text())
    #             end.append(self.password_edit.text())
    #             with open("Base_users.csv", mode="w", encoding='utf-8') as w_file:
    #                 file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
    #                 for k in data_user: #перезапись всех логинов и паролей
    #                     file_writer.writerow(k)
    #                 file_writer.writerow(end) #добавление нового пользователя в систему

    def enter_user(self):  # вход в систему
        global data
        log_flag = False
        pass_log = False
        if self.sender().text() == 'Войти как Администратор':
            base_users = 'Base_adm.csv'
        # if self.sender().text() == 'Войти':
        #     base_users = 'Base_users.csv'
        with open(base_users, encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            if self.login_edit.text() == '' and self.password_edit.text() == '':  # Проверка пароля и логина на
                # пустое поле
                self.format.setText('Неверный формат логина или пароля')
            else:
                pass_log = True
            for s in self.login_edit.text():  # проверка знаков на знаки и буквы в логине
                if s.isascii() is False and pass_log is True:
                    log_flag = False
                    self.format.setText('Неверный формат логина')
                    break
                else:
                    log_flag = True
            if self.login_edit.text() != '' and log_flag is True and self.password_edit.text() != '':
                for x in reader:  # проверка на совпадение с базой пользователей
                    if self.login_edit.text() in x:
                        data_1 = x
                        if self.login_edit.text() == data_1[0] and self.password_edit.text() == data_1[1]:  # проверка
                            # совпадения пароля, который записан в системе
                            data = x
                            break
            if log_flag is True:
                form.show()
                Enter_Window.close(self)


class Add_del_Window(QMainWindow):  # окно с добавлением товаров в базу данных
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('style/Add_Dell_Window.ui', self)
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
        with open('deleted_files/Base.csv', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')  # чтение из файла
            for j in reader:
                base.append(j)  # добавление данных в список
            with open("deleted_files/Base.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")  # открытие записи файла
                for k in base:
                    file_writer.writerow(k)  # запись старой информации о товарах
                end = []
                end.append(self.name.text())
                end.append(self.cost.text())
                end.append(self.count.text())
                end.append(self.where.text())
                file_writer.writerow(end)  # добавление нового товара
        form.show()
        Add_del_Window.close(self)

    def dell_col(self):  # процесс удаления товаров
        base = []
        with open('deleted_files/Base.csv', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for j in reader:
                base.append(j)
            with open("deleted_files/Base.csv", mode="w", encoding='utf-8') as w_file:
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
