import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menyimpan id_anggota dari baris yang sedang dipilih
        self.id_terpilih = None

        # Binding tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Binding klik baris tabel
        self.view.table.bind("<<TreeviewSelect>>", self.pilih_baris)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Kosongkan tabel terlebih dahulu
        for item in self.view.table.get_children():
            self.view.table.delete(item)

        # Ambil data dari Model (database)
        data_anggota = self.model.get_all_anggota()

        # Masukkan ke tabel View
        for anggota in data_anggota:
            self.view.table.insert(
                "", "end",
                values=(anggota['id_anggota'], anggota['nama'], anggota['alamat'])
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')
        self.id_terpilih = None
        self.view.table.selection_remove(self.view.table.selection())

    def pilih_baris(self, event):
        """Dipanggil saat pengguna mengklik baris di tabel."""
        pilihan = self.view.table.selection()
        if not pilihan:
            return

        nilai = self.view.table.item(pilihan[0], "values")
        self.id_terpilih = nilai[0]  # id_anggota

        self.view.entry_nama.delete(0, 'end')
        self.view.entry_nama.insert(0, nilai[1])

        self.view.entry_alamat.delete(0, 'end')
        self.view.entry_alamat.insert(0, nilai[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def update_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui!")
            return

        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_anggota(self.id_terpilih, nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            return

        berhasil = self.model.delete_anggota(self.id_terpilih)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()