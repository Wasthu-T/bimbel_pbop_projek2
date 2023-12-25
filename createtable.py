paket_belajar ='''CREATE TABLE IF NOT EXISTS Paket_belajar(
   Id_paket_belajar int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Kelas ENUM('SD', 'SMP', 'SMA') NOT NULL,
   Kategori ENUM('Reguler', 'Premium') NOT NULL,
   Biaya int(100)
    );
'''

siswa = '''CREATE TABLE IF NOT EXISTS Siswa(
   Id_siswa int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Password varchar(225) NOT NULL,
   Id_paket_belajar int(10),
   FOREIGN KEY (Id_paket_belajar) REFERENCES Paket_belajar(Id_paket_belajar) ON DELETE CASCADE,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Kelas ENUM('SD', 'SMP', 'SMA') NOT NULL,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
   Alamat varchar(200) NOT NULL,
   Tagihan int(20) NOT NULL
	);
'''


guru ='''CREATE TABLE IF NOT EXISTS Guru(
   Id_guru int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Password varchar(225) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
   Tgl_lahir varchar(30) NOT NULL,
   Alamat varchar(200) NOT NULL,
   Status_pekerja ENUM('Kontrak', 'Tetap') NOT NULL,
   Bidang_mapel ENUM('Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Ilmu Pengetahuan Alam', 'Biologi', 'Kimia', 'Fisika', 'Geografi', 'Ekonomi', 'Sosiologi', 'Sejarah') NOT NULL,
   Gaji varchar(100) NOT NULL
    );
'''

pegawai = '''CREATE TABLE IF NOT EXISTS Pegawai(
   Id_pegawai int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Password varchar(225) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL,
   Tgl_lahir varchar(30) NOT NULL,
   Alamat varchar(200) NOT NULL,
   Status_pekerja ENUM('Kontrak', 'Tetap') NOT NULL,
   Jabatan ENUM('OB', 'Admin', 'Manager') NOT NULL,
   Tunjangan varchar(100) NOT NULL,
   Gaji varchar(100) NOT NULL
    );
'''


absen_pegawai = '''CREATE TABLE IF NOT EXISTS Absen_pegawai (
   Id_absen_pegawai int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_pegawai int(10),
   FOREIGN KEY (Id_pegawai) REFERENCES pegawai(Id_pegawai) ON DELETE CASCADE,
   Tanggal date,
   Jam_datang time,
   Jam_selesai time,
   Absen ENUM('Hadir', 'Izin', 'Sakit', 'Alpha') NOT NULL
    );
'''

absen_guru = '''CREATE TABLE IF NOT EXISTS Absen_guru (
   Id_absen_guru int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_guru int(10),
   FOREIGN KEY (Id_guru) REFERENCES guru(Id_guru) ON DELETE CASCADE,
   Tanggal date,
   Jam_datang time,
   Jam_selesai time,
   Absen ENUM('Hadir', 'Izin', 'Sakit', 'Alpha') NOT NULL
    );
'''


transaksi = '''CREATE TABLE IF NOT EXISTS Transaksi (
   Id_transaksi int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_pegawai int(10),
   FOREIGN KEY (Id_pegawai) REFERENCES pegawai(Id_pegawai) ON DELETE CASCADE,
   Id_siswa int(10),
   FOREIGN KEY (Id_siswa) REFERENCES siswa(Id_siswa) ON DELETE CASCADE,
   Id_paket_belajar int(10),
   FOREIGN KEY (Id_paket_belajar) REFERENCES paket_belajar(Id_paket_belajar) ON DELETE CASCADE,
   Jenis_pembayaran ENUM('Cash', 'Transfer') NOT NULL,
   Bayar int(100) NOT NULL,
   Kembalian int(100) NOT NULL,
   Tgl_transaksi date
    );
'''


ruangan ='''CREATE TABLE IF NOT EXISTS Ruangan(
   Id_ruangan int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Kondisi_ruangan ENUM('Layak', 'Tidak layak') NOT NULL,
   Kapasitas_kursi int(10) NOT NULL
    );
'''

jadwal = '''CREATE TABLE IF NOT EXISTS Jadwal (
   Id_jadwal int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_guru int(10),
   FOREIGN KEY (Id_guru) REFERENCES guru(Id_guru) ON DELETE CASCADE,
   Kelas ENUM('SD', 'SMP', 'SMA') NOT NULL,
   Mapel ENUM('Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Ilmu Pengetahuan Alam', 'Biologi', 'Kimia', 'Fisika', 'Geografi', 'Ekonomi', 'Sosiologi', 'Sejarah') NOT NULL,
   Jam time,
   Tanggal date,
   Id_ruangan int(10) NOT NULL,
   Paket_belajar ENUM('Reguler', 'Premium') NOT NULL
    );
'''
jadwal_pelayanan = '''CREATE TABLE IF NOT EXISTS Jadwal_pelayanan (
   Id_jadwal_pelayanan int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_guru int(10),
   FOREIGN KEY (Id_guru) REFERENCES guru(Id_guru) ON DELETE CASCADE,
   Mapel ENUM('Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Ilmu Pengetahuan Alam', 'Biologi', 'Kimia', 'Fisika', 'Geografi', 'Ekonomi', 'Sosiologi', 'Sejarah') NOT NULL,
   Jam_pelayanan time,
   Id_ruangan int(10),
   FOREIGN KEY (Id_ruangan) REFERENCES ruangan(Id_ruangan) ON DELETE CASCADE
    );
'''
absen_siswa = '''CREATE TABLE IF NOT EXISTS Absen_siswa (
   Id_absen_siswa int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_guru int(10),
   FOREIGN KEY (Id_guru) REFERENCES guru(Id_guru) ON DELETE CASCADE,
   Id_siswa int(10),
   FOREIGN KEY (Id_siswa) REFERENCES siswa(Id_siswa) ON DELETE CASCADE,
   Id_jadwal int(10), 
   FOREIGN KEY (Id_jadwal) REFERENCES jadwal(Id_jadwal) ON DELETE CASCADE,
   Tanggal date,
   Absen ENUM('Hadir', 'Izin', 'Sakit', 'Alpha') NOT NULL
    );
'''

def created_table(db) :
    db.create(paket_belajar)
    db.create(siswa)
    db.create(guru)
    db.create(pegawai)
    db.create(absen_pegawai)
    db.create(transaksi)
    db.create(jadwal)
    db.create(ruangan)
    db.create(absen_siswa)
    db.create(absen_guru)
    db.create(jadwal_pelayanan)
    print("Tabel berhasil dibuat")
