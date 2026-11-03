from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Data palsu yang akan dikembalikan oleh fetchall()
    data_palsu = [
        {'id_buku': 1, 'judul': 'Buku Testing', 'penulis': 'Penulis QA', 'tahun_terbit': 2026},
        {'id_buku': 2, 'judul': 'Belajar Python', 'penulis': 'Penulis B', 'tahun_terbit': 2025},
    ]
    mock_cursor.fetchall.return_value = data_palsu

    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()

    # Memverifikasi hasil sama dengan data palsu
    assert hasil == data_palsu
    assert len(hasil) == 2

    # Memverifikasi cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()