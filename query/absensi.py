from datetime import datetime
import locale

# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class absen_pegawai :
    def __init__(self, db):
        self.db = db

    def absen_datang(self, Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen datang hari ini")
            jam_datang = datetime.now().time()
            Jam_selesai = None
            Absen = "Alpha"
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen Datang pada \nTanggal :{tanggal} \nJam \t:{jam_datang}")
        except Exception as e :
            print(e)

    def absen_pulang(self, Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            Jam_selesai = datetime.now().time()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][3]
                if test is None :
                    raise ValueError("Anda belum absen datang hari ini")
            if not result :
                raise ValueError("Anda belum absen datang hari ini")
            Absen = "Hadir"
            query = """
                UPDATE `absen_pegawai` 
                SET
                `Jam_selesai` = %s,
                `Absen` = %s 
                WHERE `Tanggal` = %s AND `Id_pegawai` = %s
            """
            data = (Jam_selesai, Absen, tanggal, Id_pegawai)
            self.db.insertValue(query, data)
            print(f"Anda Berhasil Absen Pulang pada \nTanggal :{tanggal} \nJam \t:{Jam_selesai}")
        except Exception as e :
            print(e)

    
    def absen(self) :
        while True:
            print("\n=== Izin ===")
            print("1. Sakit")
            print("2. Izin")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1:
                return "Sakit"
            elif pilih == 2:
                return "Izin"
            else:
                print("pilihan tidak tersedia harap pilih yang benar")
    
    def izin(self,Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen hari ini")
            jam_datang = None
            Jam_selesai = None
            Absen = self.absen()
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen pada {tanggal}")
        except Exception as e :
            print(e)

class absen_guru :
    def __init__(self, db):
        self.db = db

    def absen_datang(self, Id_guru) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_guru` WHERE `Id_guru`=%s"""
            result = self.db.selectValue(query, (Id_guru,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen datang hari ini")
            jam_datang = datetime.now().time()
            Jam_selesai = None
            Absen = "Alpha"
            query = """INSERT INTO `absen_guru`(`Id_guru`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_guru, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen Datang pada \nTanggal :{tanggal} \nJam \t:{jam_datang}")

        except Exception as e :
            print(e)

    def absen_pulang(self, Id_guru) :
        try :
            tanggal = datetime.now().date()
            Jam_selesai = datetime.now().time()
            query = """SELECT * FROM `absen_guru` WHERE `Id_guru`=%s"""
            result = self.db.selectValue(query, (Id_guru,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][3]
                if test is None :
                    raise ValueError("Anda belum absen datang hari ini")
            if not result :
                raise ValueError("Anda belum absen datang hari ini")
                
            Absen = "Hadir"
            query = """
                UPDATE `absen_guru` 
                SET
                `Jam_selesai` = %s,
                `Absen` = %s 
                WHERE `Tanggal` = %s AND `Id_guru` = %s
            """
            data = (Jam_selesai, Absen, tanggal, Id_guru)
            self.db.insertValue(query, data)
            print(f"Anda Berhasil Absen Datang pada \nTanggal :{tanggal} \nJam \t:{Jam_selesai}")
        except Exception as e :
            print(e)

    def absen(self) :
        while True:
            print("\n=== Izin ===")
            print("1. Sakit")
            print("2. Izin")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1:
                return "Sakit"
            elif pilih == 2:
                return "Izin"
            else:
                print("pilihan tidak tersedia harap pilih yang benar")
    
    def izin(self,Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen hari ini")
            jam_datang = None
            Jam_selesai = None
            Absen = self.absen()
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen pada {tanggal}")

        except Exception as e :
            print(e)
    
    def absen_s(self) :
        while True :
            print("\n=== Absensi ===")
            print("1. Hadir")
            print("2. Sakit")
            print("3. Izin")
            print("4. Alpha")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1 :
                return "Hadir"
            elif pilih == 2 :
                return "Sakit"
            elif pilih == 3 :
                return "Izin"
            elif pilih == 4 :
                return "Alpha"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")
    def absen_siswa(self,Id_guru) :
            id_jadwal_guru = int(input("Id jadwal : "))
            i = 0 
            selectabsen = """SELECT * FROM `absen_siswa` WHERE `Id_guru`=%s"""
            result = self.db.selectValue(selectabsen, (Id_guru,))
            list_id_siswa = []
            list_id_jadwal = []
            for i in range(len(result)) :
                id_siswa_tes = result[i][2]
                id_jadwal_tes = result[i][3]
                list_id_siswa.append(id_siswa_tes)
                list_id_jadwal.append(id_jadwal_tes)
                    
            while True :
                try :
                    tanggal = datetime.now().date()

                    
                    i = 0 
                    selectjadwals = """SELECT * FROM jadwal WHERE Id_guru=%s"""
                    resultjadwal = self.db.selectValue(selectjadwals,(Id_guru, ) )
                    print(resultjadwal)
                    list_jadwal = []
                    for i in range(len(resultjadwal)) :
                        id_jadwal = resultjadwal[i][0]
                        check_id_guru = resultjadwal[i][1]
                        list_jadwal.append(id_jadwal)
                    print(list_jadwal)
                    if (id_jadwal_guru not in list_jadwal) and (Id_guru == check_id_guru) :
                        raise ValueError("Id jadwal tidak ada pada jadwal anda")
                    
                    print("Berhasil 1")
                    
                    id_siswa = int(input("Id siswa : "))
                    absen = self.absen_s()
                    if (id_siswa in list_id_siswa) and (id_jadwal in list_id_jadwal):
                        raise ValueError("Anda telah absen hari ini")

                    select_jadwal = """SELECT * FROM `jadwal` WHERE Id_jadwal=%s"""
                    result_jadwal = self.db.selectValue(select_jadwal, (id_jadwal_guru, ))
                    tgl = result_jadwal[0][7]
                    paket_belajar = result_jadwal[0][2]

                    if tgl != tanggal :
                        raise ValueError("Salah tanggal pelajaran")
                    
                    select_siswa = """SELECT * FROM `siswa` WHERE Id_paket_belajar=%s"""
                    select_id = self.db.selectValue(select_siswa, (paket_belajar, ))
                    list_check_siswa = []
                    i = 0
                    for i in range(len(select_id)) :
                        check_id_siswa = select_id[0][0]
                        list_check_siswa.append(check_id_siswa)


                    if id_siswa not in list_check_siswa :
                        raise ValueError("Id siswa tidak mengambil paket belajar ini")
                    

                    query = """INSERT INTO `absen_siswa`(`Id_guru`, `Id_siswa`, `Id_jadwal`, `Tanggal`, `Absen`) 
                    VALUES (%s,%s,%s,%s,%s)"""
                    data = (Id_guru,id_siswa,id_jadwal,tanggal,absen)
                    self.db.insertValue(query, data)
                    print(f"Siswa dengan id siswa {id_siswa} berhasil absen")
                    tambah = str(input("Ingin Absen lagi (y/n) ? "))
                    if tambah.lower() == "y" :
                        continue
                    else :
                        break

                except Exception as e :
                    print(e)
                    tambah = str(input("Ingin Melanjutkan (y/n) ? "))
                    if tambah.lower() == "y" :
                        continue
                    else :
                        break
class absen_siswa :
    def __init__(self, db):
        self.db = db

    def lihat_absen(self, Id_siswa) :
        query = """SELECT * FROM `absen_siswa` WHERE Id_siswa=%s AND Id_jadwal=%s"""
        Id_jadwal = int(input("Masukan Id jadwal : "))
        data = (Id_siswa, Id_jadwal)
        self.db.selectValuepretty(query, data)
