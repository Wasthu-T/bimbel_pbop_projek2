# -- Data untuk tabel Pelajar
pelajar = """INSERT INTO Pelajar (Nama, Email, Nomor, Jenjang_pendidikan, Jenis_kelamin, Password) VALUES
('Wasthutatya', 'Wasthutatya@gmail.com', '081234513', 'SMA', 'Laki-laki', 'kepo123'),
('David Bagas Santoso', 'David@gmail.com', '089765423', 'SMP', 'Laki-laki', 'bebas123'),
('Tsani Nur Syabani', 'Tsani@gmail.com', '089764231', 'SD', 'Laki-laki', 'apaaja123');"""

# -- Data untuk tabel Pengajar
pengajar = """INSERT INTO Pengajar (Nama, Email, Nomor, Usia, Jenis_kelamin, Password) VALUES
('Ayu Maulida', 'Ayuma@exsample.com', '555987654', '26', 'Perempuan', 'kepo123'),
('Dimas Anggara', 'Dimas@exsample.com', '555123456', '28', 'Laki-laki', 'bebas123'),
('Anisa Fatmawati', 'Anisa@exsample.com', '555456789', '25', 'Perempuan', 'apaaja123');"""

# -- Data untuk tabel Admin
admin = """INSERT INTO Admin (Nama, Email, Nomor, Usia, Jenis_kelamin) VALUES
('Alano Aditama', 'Alano@example.com', '967123456', '27', 'Laki-laki'),
('Berlian Saputri', 'Berlian@example.com', '967987654', '27', 'Perempuan'),
('Amanda Rizky', 'Amanda@example.com', '967456789', '26', 'Perempuan');"""

def created_data(db) :
    db.create(pelajar)
    db.create(pengajar)
    db.create(admin)
    print("Data Sampel berhasil dibuat")