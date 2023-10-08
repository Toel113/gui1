# system Admin ------------------------------------------------------------------------------------------

# def login(self):
#         username = self.username_input.text()
#         password = self.password_input.text()
#         try:
#             query = "SELECT * FROM admin WHERE username = %s AND password = %s"
#             cursor.execute(query, (username, password))
#             user = cursor.fetchone()

#             if user:
#                 QMessageBox.information(self, 'Login Successful', 'Welcome, {}'.format(username))
#                 self.open_add_product_window()
#                 self.username_input.clear()
#                 self.password_input.clear()
#             else:
#                 QMessageBox.warning(self, 'Login Failed', 'Invalid username or password. Please try again.')
#                 self.password_input.clear()
#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as err:
#             print("Error: {}".format(err))

#     def open_add_product_window(self):
#         self.add_product_window = Add_product()
#         self.add_product_window.show()

# END* --------------------------------------------------------------------------

# AddProduct ---------------------------------------------------------------------------------------------------

# def add_product(self):
#         name = self.name_input.text()
#         barcode = self.barcode_input.text()
#         price = self.price_input.text()
#         quantity = self.quantity_input.text()
#         try:
#             query = "INSERT INTO add_product (name_product, barcode, price, quantity) VALUES (%s, %s, %s, %s)"
#             cursor.execute(query, (name, barcode, price, quantity))
#             connection.commit()

#             QMessageBox.information(self, 'Success', 'Product added successfully.')
#             self.clear_inputs()

#             cursor.close()
#             connection.close()

#             self.load_data()

#         except mysql.connector.Error as err:
#             print("Error: {}".format(err))
#             QMessageBox.warning(self, 'Error', 'An error occurred while adding the product.')

#     def load_data(self):
#         try:
#             query = "SELECT name_product, barcode, price, quantity FROM add_product"
#             cursor.execute(query)
#             data = cursor.fetchall()

#             self.table.setRowCount(len(data))

#             for row_num, row_data in enumerate(data):
#                 for col_num, cell_data in enumerate(row_data):
#                     item = QTableWidgetItem(str(cell_data))
#                     self.table.setItem(row_num, col_num, item)
                    
#                 delete_button = QPushButton('Delete', self)
#                 delete_button.clicked.connect(lambda _, row=row_num: self.delete_product(row))
#                 self.table.setCellWidget(row_num, 4, delete_button)

#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as err:
#             print("Error: {}".format(err))
#             QMessageBox.warning(self, 'Error', 'An error occurred while loading data.')

#     def deleat_product(self,row):  
#         try:
#             name = self.table.item(row, 0).text()
#             reply = QMessageBox.question(self, 'Delete Confirmation', f'Do you want to delete the product "{name}"?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
#             if reply == QMessageBox.Yes:
#                 query = "DELETE FROM add_product WHERE name_product = %s"
#                 cursor.execute(query, (name,))
#                 connection.commit()

#                 self.load_data()

#                 QMessageBox.information(self, 'Success', 'Product deleted successfully.')
#             else:
#                 QMessageBox.information(self, 'Delete Cancelled', 'Product deletion cancelled.')

#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as err:
#             print("Error: {}".format(err))
#             QMessageBox.warning(self, 'Error', 'An error occurred while deleting the product.')

#     def clear_inputs(self):
#         self.name_input.clear()
#         self.barcode_input.clear()
#         self.price_input.clear()
#         self.quantity_input.clear()

# END * -------------------------------------------------

# main -------------------------------------------------

# import sys
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
# from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
# import mysql.connector as mc
# from PyQt5.QtCore import QTimer


# from Change import *

# class MainBigWindow(QMainWindow):
#     def __init__(self):
#         super(MainBigWindow, self).__init__()

#         self.ui = Ui_Change_Bay()
#         self.ui.setupUi(self)
#         # self.showFullScreen()
        
#         #flamelesswindow
#         # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
    
#     style_file = QFile("stylechange.qss")
#     style_file.open(QFile.ReadOnly | QFile.Text)
#     style_stream = QTextStream(style_file)
#     app.setStyleSheet(style_stream.readAll())
    
#     bigwindow = MainBigWindow()
#     bigwindow.show()
     
#     sys.exit(app.exec())

# END ---------------------------------------------------------------------------------------------------
