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