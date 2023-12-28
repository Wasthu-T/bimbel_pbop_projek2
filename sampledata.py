# -- Data untuk tabel Paket Belajar
paket_belajar = """INSERT INTO paket_belajar(Kategori, Kelas, Biaya) VALUES 
                    ('Reguler', '4SD', '280000'),
                    ('Reguler', '5SD', '280000'),
                    ('Reguler', '6SD', '280000'),
                    ('Reguler', '1SMP', '430000'),
                    ('Reguler', '2SMP', '430000'),
                    ('Reguler', '3SMP', '430000'),
                    ('Reguler', '1SMA IPA', '480000'),
                    ('Reguler', '2SMA IPA', '480000'),
                    ('Reguler', '3SMA IPA', '480000'),
                    ('Reguler', '1SMA IPS', '480000'),
                    ('Reguler', '2SMA IPS', '480000'),
                    ('Reguler', '3SMA IPS', '480000'),
                    ('Premium', '4SD', '450000'),
                    ('Premium', '5SD', '450000'),
                    ('Premium', '6SD', '450000'),
                    ('Premium', '1SMP', '7175000'),
                    ('Premium', '2SMP', '7175000'),
                    ('Premium', '3SMP', '7175000'),
                    ('Premium', '1SMA IPA', '900000'),
                    ('Premium', '2SMA IPA', '900000'),
                    ('Premium', '3SMA IPA', '900000'),
                    ('Premium', '1SMA IPS', '900000'),
                    ('Premium', '2SMA IPS', '900000'),
                    ('Premium', '3SMA IPS', '900000');"""

# -- Data untuk tabel Pelajar
siswa = """INSERT INTO Siswa(Id_paket_belajar, Nama, Password, Email, Nomor, Kelas, Jenis_kelamin, Alamat, Tagihan) VALUES 
('1', 'Alano Aditama', 'alano123', 'Alano11@gmail.com', '082337209867', '4SD', 'Laki-laki', 'Trini', '280000'),
('2', 'Gilang Pratama', 'gilang123', 'Gilang12@gmail.com', '082456789345', '5SD', 'Laki-laki', 'Sendangadi', '280000'),
('3', 'Adinda Maheswari', 'dinda123', 'Adinda13@gmail.com', '082567432109', '6SD', 'Perempuan', 'Sleman', '280000'),
('4', 'Talita Azahra', 'talita123', 'Alita14@gmail.com', '082456757665', '1SMP', 'Perempuan', 'Sinduadi', '430000'),
('5', 'Galang Saputra', 'galang123', 'Galang15@gmail.com', '082765890667', '2SMP', 'Laki-laki', 'Sendangadi', '430000'),
('6', 'Fania Agustina', 'fania123', 'Fania16@gmail.com', '082765432908', '3SMP', 'Perempuan', 'Bantul', '430000'),
('7', 'Syalma Azum Latifah', 'syalma123', 'Syalma17@gmail.com', '082867954678', '1SMA IPA', 'Perempuan', 'Gejayan', '480000'),
('8', 'Atharel Devandra', 'atha123', 'Atharel18@gmail.com', '082345678910', '2SMA IPA', 'Laki-laki', 'Sendangadi', '480000'),
('9', 'Salsabila Maheswari', 'salsa123', 'Salsa19@gmail.com', '082435879554', '3SMA IPA', 'Perempuan', 'Tlogoadi', '480000'),
('10', 'Amanda Rizky', 'amanda123', 'Amanda20@gmail.com', '082421776890', '1SMA IPS', 'Perempuan', 'Tirtoadi', '480000'),
('11', 'Kezia Dilla', 'kezia123', 'Kezia21@gmail.com', '082421779657', '2SMA IPS', 'Perempuan', 'Godean', '480000'),
('12', 'Ananda Rizal', 'rizal123', 'Rizal22@gmail.com', '082654890223', '3SMA IPS', 'Laki-laki', 'Bantul', '480000'),
('15', 'Keano Aditama', 'keano123', 'Ken116@gmail.com', '082543678976', '6SD', 'Laki-laki', 'Godean', '450000'),
('18', 'Abimanyu', 'abi123', 'Abim117@gmail.com', '082431568967', '3SMP', 'Laki-laki', 'Condongcatur', '717500'),
('20', 'Adelia Putri', 'adelia123', 'Delia118@gmail.com', '082678546789', '2SMA IPA', 'Perempuan', 'Gamping', '900000'),
('24', 'Dimas Anggara', 'dimas123', 'Dimas119@gmail.com', '082677856754', '3SMA IPS', 'Laki-laki', 'Kronggahan', '900000');"""

# -- Data untuk tabel Pengajar
guru = """INSERT INTO Guru(Nama, Email, Password, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji) VALUES 
('Ratna Setyowati', 'Ratna11@gmail.com', 'ratna123', '083456789123', 'Perempuan', '1997-10-21', 'Sleman', 'Tetap', 'Bahasa Indonesia', '870000'),
('Agung Suryadi', 'Agung12@gmail.com', 'agung123', '083456787542', 'Laki-laki', '1996-08-13', 'Gamping', 'Tetap', 'Bahasa Inggris', '870000'),
('Muryani', 'Muryani13@gmail.com', 'muryani123', '083678543667', 'Perempuan', '1995-05-25', 'Cebongan', 'Tetap', 'Ilmu Pengetahuan Alam', '870000'),
('Selfi Artika', 'Selfi14@gmail.com', 'selfi123', '083765342889', 'Perempuan', '1997-11-07', 'Maguwoharjo', 'Tetap', 'Matematika', '1110000'),
('Muryanto', 'Muryanto15@gmail.com', 'yanto123', '083986734521', 'Laki-laki', '1994-08-17', 'Bantul', 'Tetap', 'Tes Potensi Skolastik', '870000'),
('Anita Kusumawati', 'Anita16@gmail.com', 'anita123', '083654897345', 'Perempuan', '1996-04-27', 'Condongcatur', 'Kontrak', 'Biologi', '510000'),
('Oryza Putri', 'Oryza17@gmail.com', 'oryza123', '083654893256', 'Perempuan', '1994-10-01', 'Kaliurang', 'Kontrak', 'Fisika', '750000'),
('Umi Farichah', 'Umi18@gmail.com', 'umi123', '083227455098', 'Perempuan', '1992-08-11', 'Godean', 'Kontrak', 'Kimia', '510000'),
('Bambang Wahono', 'Bambang19@gmail.com', 'bambang123', '083543768887', 'Laki-laki', '1991-06-21', 'Gejayan', 'Kontrak', 'Geografi', '510000'),
('Sudarmono', 'Sudarmono20@gmail.com', 'darmono123', '083476894123', 'Laki-laki', '1993-08-15', 'Kaliurang', 'Kontrak', 'Sejarah', '510000'),
('Sri Lestari', 'Lestari21@gmail.com', 'lestari123', '083228904567', 'Perempuan', '1994-05-16', 'Cebongan', 'Kontrak', 'Sosiologi', '670000'),
('Aryanto Syaifullah', 'Aryanto22@gmail.com', 'aryan123', '083654789334', 'Laki-laki', '1995-02-17', 'Monjali', 'Kontrak', 'Ekonomi', '510000');"""

# -- Data untuk tabel Admin
pegawai = """INSERT INTO Pegawai(Nama, Password, Email, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Jabatan, Tunjangan, Gaji) VALUES 
            ('Ayu Maulida', 'ayuma123', 'Ayuma11@gmail.com', '085337200879', 'Perempuan', '1999-12-10', 'Gejayan', 'Tetap', 'Manager', '0', '5000000'),
            ('Ilham Pratama', 'ilham123', 'Ilham12@gmail.com', '085654789543', 'Laki-laki', '2000-05-17', 'Kaliurang', 'Tetap', 'Admin', '0', '3000000'),
            ('Andi Irawan', 'andi123', 'Andi13@gmail.com', '085743209188', 'Laki-laki', '2002-19-17', 'Sleman', 'Kontrak', 'OB', '0', '1000000');"""

# -- Data untuk tabel Ruangan
ruangan = """INSERT INTO ruangan(Kondisi_ruangan, Kapasitas_kursi) VALUES 
            ('Layak', '20'),
            ('Layak', '25'),
            ('Layak', '15'),
            ('Tidak layak', '15'),
            ('Layak', '30');"""

# -- Data untuk tabel Jadwal
jadwal = """INSERT INTO jadwal(Id_guru, Id_paket_belajar , Kelas, Mapel, Jam_mulai,Jam_selesai, Tanggal, Id_ruangan, Paket_belajar) VALUES 
            ('1', '6','3SMP', 'Bahasa Indonesia', '16:30:00', '18:00:00', '2023-12-26', '1', 'Reguler'),
            ('2', '9','3SMA IPA', 'Bahasa Inggris', '16:30:00', '18:00:00', '2023-12-26', '2', 'Reguler'),
            ('3', '15','3SMP', 'Ilmu Pengetahuan Alam', '18:30:00', '20:00:00', '2023-12-26', '3', 'Premium'),
            ('4', '5','2SMP', 'Matematika', '19:00:00', '20:30:00', '2023-12-26', '4', 'Reguler'),
            ('5',  '11','2SMA IPS','Tes Potensi Skolastik', '16:30:00', '18:00:00', '2023-12-26', '3', 'Reguler');"""

def created_data(db) :
    db.create(paket_belajar)
    db.create(siswa)
    db.create(guru) 
    db.create(pegawai)
    db.create(ruangan) 
    db.create(jadwal)
    print("Data Sampel berhasil dibuat")
