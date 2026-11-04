# from controllers.buku_controller import BukuController


# if __name__ == "__main__":
#     app = BukuController()
#     app.run()


# from controllers.anggota_controller import AnggotaController

# if __name__ == "__main__":
#     app = AnggotaController()
#     app.run()

from controllers.auth_controller import AuthController

if __name__ == "__main__":
    app = AuthController()
    app.run()

# from models.user_model import UserModel

# m = UserModel()
# print(m.register_user("Aditya", "rahasia123", "anggota"))   # True
# print(m.autentikasi("Aditya", "rahasia123"))                # data user (login berhasil)
# print(m.autentikasi("Aditya", "salah"))                     # None