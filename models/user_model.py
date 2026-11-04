# Aditya_019
import hashlib
from config.database import Database
from mysql.connector import Error

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Mengubah plain text password menjadi hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)

            # Parameterized Query untuk mencegah SQL Injection
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None

    def register_user(self, username, password, role):
        if self.conn:
            try:
                cursor = self.conn.cursor()

                # 1. Ubah password menjadi hash SHA-256 SEBELUM disimpan
                password_hash = self.hash_password(password)

                # 2. Parameterized query (aman dari SQL Injection)
                query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
                val = (username, password_hash, role)

                # 3. Jalankan, simpan permanen, lalu tutup cursor
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                # Misalnya username sudah ada (kolom UNIQUE)
                print(f"Gagal register user: {e}")
                return False
        return False