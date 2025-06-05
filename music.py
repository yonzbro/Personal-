import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kullanıcı Doğrulama")
        self.setGeometry(300, 300, 400, 200)
        
        # Kullanıcı Adı
        self.username_label = QLabel("Kullanıcı Adı:", self)
        self.username_label.move(50, 50)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 50)
        
        # Şifre
        self.password_label = QLabel("Şifre:", self)
        self.password_label.move(50, 100)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(150, 100)
        
        # Giriş Butonu
        self.login_button = QPushButton("Giriş", self)
        self.login_button.move(150, 150)
        self.login_button.clicked.connect(self.login)
        
        # Kayıt Butonu
        self.register_button = QPushButton("Kayıt", self)
        self.register_button.move(250, 150)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            conn = psycopg2.connect(
                dbname="PYB",
                user="kullanici_adiniz",
                password="1234",
                host="local host"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cur.fetchone()
            if result:
                QMessageBox.information(self, "Başarılı", "Giriş başarılı!")
            else:
                QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı!")
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {e}")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            conn = psycopg2.connect(
                dbname="PYB",
                user="kullanici_adiniz",
                password="1234",
                host="local host"
            )
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt başarılı!")
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {e}")

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec_())
