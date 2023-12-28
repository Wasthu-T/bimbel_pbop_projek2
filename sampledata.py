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
                    ('Premium', '1SMP', '717500'),
                    ('Premium', '2SMP', '717500'),
                    ('Premium', '3SMP', '717500'),
                    ('Premium', '1SMA IPA', '900000'),
                    ('Premium', '2SMA IPA', '900000'),
                    ('Premium', '3SMA IPA', '900000'),
                    ('Premium', '1SMA IPS', '900000'),
                    ('Premium', '2SMA IPS', '900000'),
                    ('Premium', '3SMA IPS', '900000');"""

# -- Data untuk tabel Pelajar
siswa = """INSERT INTO Siswa(Id_paket_belajar, Nama, Password, Email, Nomor, Kelas, Jenis_kelamin, Alamat, Tagihan) VALUES 
('1', 'Alano Aditama', 'alano123', 'Alano@gmail.com', '082337209867', '4SD', 'Laki-laki', 'Trini', '280000'),
('2', 'Gilang Pratama', 'gilang123', 'Gilang@gmail.com', '082456789345', '5SD', 'Laki-laki', 'Sendangadi', '280000'),
('3', 'Adinda Maheswari', 'dinda123', 'Adinda@gmail.com', '082567432109', '6SD', 'Perempuan', 'Sleman', '280000'),
('4', 'Talita Azahra', 'talita123', 'Alita@gmail.com', '082456757665', '1SMP', 'Perempuan', 'Sinduadi', '430000'),
('5', 'Galang Saputra', 'galang123', 'Galang@gmail.com', '082765890667', '2SMP', 'Laki-laki', 'Sendangadi', '430000'),
('6', 'Fania Agustina', 'fania123', 'Fania@gmail.com', '082765432908', '3SMP', 'Perempuan', 'Bantul', '430000'),
('7', 'Syalma Azum Latifah', 'syalma123', 'Syalma@gmail.com', '082867954678', '1SMA IPA', 'Perempuan', 'Gejayan', '480000'),
('8', 'Atharel Devandra', 'atha123', 'Atharel@gmail.com', '082345678910', '2SMA IPA', 'Laki-laki', 'Sendangadi', '480000'),
('9', 'Salsabila Maheswari', 'salsa123', 'Salsa@gmail.com', '082435879554', '3SMA IPA', 'Perempuan', 'Tlogoadi', '480000'),
('10', 'Amanda Rizky', 'amanda123', 'Amanda@gmail.com', '082421776890', '1SMA IPS', 'Perempuan', 'Tirtoadi', '480000'),
('11', 'Kezia Dilla', 'kezia123', 'Kezia@gmail.com', '082421779657', '2SMA IPS', 'Perempuan', 'Godean', '480000'),
('12', 'Ananda Rizal', 'rizal123', 'Rizal@gmail.com', '082654890223', '3SMA IPS', 'Laki-laki', 'Bantul', '480000'),
('13', 'Rista Alifia', 'rista123', 'Rista@gmail.com', '082675423187', '4SD', 'Perempuan', 'Maguwoharjo', '450000'),
('14', 'Darin Kusumawardani', 'darin123', 'Darin@gmail.com', '082789654321', '5SD', 'Perempuan', 'Babarsari', '450000'),
('15', 'Keano Aditama', 'keano123', 'Ken@gmail.com', '082543678976', '6SD', 'Laki-laki', 'Godean', '450000'),
('16', 'Rahardean Mangkuluhur', 'dean123', 'Dean@gmail.com', '082667895432', '1SMP', 'Laki-laki', 'Gamping', '717500'),
('17', 'Jasmine Rahmania Pramesti', 'jasmine123', 'Jasmine@gmail.com', '082567443568', '2SMP', 'Perempuan', 'Kaliurang', '717500'),
('18', 'Abimanyu', 'abi123', 'Abim@gmail.com', '082431568967', '3SMP', 'Laki-laki', 'Condongcatur', '717500'),
('19', 'Abigail Zebyana', 'abigail123', 'Abigail@gmail.com', '082876904567', '1SMA IPA', 'Perempuan', 'Monjali', '900000'),
('20', 'Adelia Putri', 'adelia123', 'Delia@gmail.com', '082678546789', '2SMA IPA', 'Perempuan', 'Gamping', '900000'),
('21', 'Fathur Setiyawan', 'fathur123', 'Fathur@gmail.com', '082786598034', '3SMA IPA', 'Laki-laki', 'Kronggahan', '900000'),
('22', 'Danela Khanza', 'danela123', 'Danela@gmail.com', '082678554789', '1SMA IPS', 'Perempuan', 'Sinduadi', '900000'),
('23', 'Andina Jolie', 'jolie123', 'Jolie@gmail.com', '082876543210', '2SMA IPS', 'Perempuan', 'Sendangadi', '900000'),
('24', 'Dimas Anggara', 'dimas123', 'Dimas@gmail.com', '082677856754', '3SMA IPS', 'Laki-laki', 'Kronggahan', '900000');"""

# -- Data untuk tabel Pengajar
guru = """INSERT INTO Guru(Nama, Email, Password, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji) VALUES 
('Ratna Setyowati', 'Ratna@gmail.com', 'ratna123', '083456789123', 'Perempuan', '1997-10-21', 'Sleman', 'Tetap', 'Bahasa Indonesia', '870000'),
('Agung Suryadi', 'Agung@gmail.com', 'agung123', '083456787542', 'Laki-laki', '1996-08-13', 'Gamping', 'Tetap', 'Bahasa Inggris', '870000'),
('Muryani', 'Muryani@gmail.com', 'muryani123', '083678543667', 'Perempuan', '1995-05-25', 'Cebongan', 'Tetap', 'Ilmu Pengetahuan Alam', '870000'),
('Selfi Artika', 'Selfi@gmail.com', 'selfi123', '083765342889', 'Perempuan', '1997-11-07', 'Maguwoharjo', 'Tetap', 'Matematika', '1110000'),
('Muryanto', 'Muryanto@gmail.com', 'yanto123', '083986734521', 'Laki-laki', '1994-08-17', 'Bantul', 'Tetap', 'Tes Potensi Skolastik', '870000'),
('Anita Kusumawati', 'Anita@gmail.com', 'anita123', '083654897345', 'Perempuan', '1996-04-27', 'Condongcatur', 'Kontrak', 'Biologi', '510000'),
('Oryza Putri', 'Oryza@gmail.com', 'oryza123', '083654893256', 'Perempuan', '1994-10-01', 'Kaliurang', 'Kontrak', 'Fisika', '750000'),
('Umi Farichah', 'Umi@gmail.com', 'umi123', '083227455098', 'Perempuan', '1992-08-11', 'Godean', 'Kontrak', 'Kimia', '510000'),
('Bambang Wahono', 'Bambang@gmail.com', 'bambang123', '083543768887', 'Laki-laki', '1991-06-21', 'Gejayan', 'Kontrak', 'Geografi', '510000'),
('Sudarmono', 'Sudarmono@gmail.com', 'darmono123', '083476894123', 'Laki-laki', '1993-08-15', 'Kaliurang', 'Kontrak', 'Sejarah', '510000'),
('Sri Lestari', 'Lestari@gmail.com', 'lestari123', '083228904567', 'Perempuan', '1994-05-16', 'Cebongan', 'Kontrak', 'Sosiologi', '670000'),
('Aryanto Syaifullah', 'Aryanto@gmail.com', 'aryan123', '083654789334', 'Laki-laki', '1995-02-17', 'Monjali', 'Kontrak', 'Ekonomi', '510000');"""

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
            ('1', '6','3SMP', 'Bahasa Indonesia', '16:30:00', '18:00:00', '2023-12-29', '1', 'Reguler'),
            ('2', '9','3SMA IPA', 'Bahasa Inggris', '16:30:00', '18:00:00', '2023-12-29', '2', 'Reguler'),
            ('3', '15','3SMP', 'Ilmu Pengetahuan Alam', '18:30:00', '20:00:00', '2024-01-05', '3', 'Premium'),
            ('4', '5','2SMP', 'Matematika', '19:00:00', '20:30:00', '2024-01-05', '4', 'Reguler'),
            ('5',  '11','2SMA IPS','Tes Potensi Skolastik', '16:30:00', '18:00:00', '2023-12-26', '3', 'Reguler');"""

def created_data(db) :
    db.create(paket_belajar)
    db.create(siswa)
    db.create(guru) 
    db.create(pegawai)
    db.create(ruangan) 
    db.create(jadwal)
    print("Data Sampel berhasil dibuat")
