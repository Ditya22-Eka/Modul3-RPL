
import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("800x450")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form Input)
        self.grid_columnconfigure(1, weight=1) # Kolom Kanan (Tabel Data Lebih Lebar)
        self.grid_rowconfigure(0, weight=1)


        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=15)

      
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_nama.pack(pady=10, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat Anggota")
        self.entry_alamat.pack(pady=10, padx=15, fill="x")

        
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

       
        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Update Data", fg_color="blue")
        self.btn_update.pack(pady=10, padx=15, fill="x")

       
        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_hapus.pack(pady=10, padx=15, fill="x")

        
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota", font=("Arial", 16, "bold")).pack(pady=15)

        
        kolom = ("id", "nama", "alamat")
        self.table = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        # Konfigurasi Header Tabel
        self.table.heading("id", text="ID")
        self.table.heading("nama", text="Nama Anggota")
        self.table.heading("alamat", text="Alamat Anggota")

        # Konfigurasi Kolom Tabel
        self.table.column("id", width=50, anchor="center")
        self.table.column("nama", width=200, anchor="w")
        self.table.column("alamat", width=300, anchor="w")

        # Penempatan Tabel
        self.table.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

# Blok Eksekusi Grafis
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()