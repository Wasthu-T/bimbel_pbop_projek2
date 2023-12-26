import os 
from connector import database
from query.aktor import Siswa, Guru, Pegawai
from query.absensi import absen_pegawai, absen_guru, absen_siswa

db = database()
db.connect()

class akses_Siswa(Siswa):
    def __init__(self, db, id, nama):
        super().__init__(db)
        self.id = id
        self.nama = nama
    def menu(self) :
        while True :
            print(f"=== Selamat Datang {self.nama} ===")
            print("==[1] Absen ")
            print("==[2] Lihat Jadwal")
            print("==[3] Paket Belajar ")
            print("==[4] Edit Akun")
            print("==[5] Detele")
            print("==[0] logout")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 :
                mur = absen_siswa(db)
                mur.lihat_absen(self.id)
            # elif pilih == 2 :
            #     self.Cari()
            # elif pilih == 3 :
            #     self.Cari()
            # elif pilih == 4 :
            #     self.Cari()
            # elif pilih == 5 :
            #     self.Cari()
            if pilih == 0 :
                print(f"\n\t=== Terimakasih {self.nama} ===")
                print("=== Jangan Lupa Datang Kembali ===\n")
                exit()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')

class akses_Guru(Guru):
    def __init__(self, db, id, nama):
        super().__init__(db)
        self.id = id
        self.nama = nama
        
    def menu(self) :
            while True :
                print(f"=== Selamat Datang {self.nama} ===")
                print("==[1] Absen ")
                print("==[2] Lihat Jadwal ")
                print("==[3] Edit Akun")
                print("==[0] logout")
                pilih = int(input("Pilih menu : "))
                if pilih == 1 :
                    self.Absen_Guru()
                # elif pilih == 2 :
                #     self.Cari()
                # elif pilih == 3 :
                #     self.Cari()
                # elif pilih == 4 :
                #     self.Cari()
                # elif pilih == 5 :
                #     self.Cari()
                elif pilih == 0 :
                    print(f"\n\t=== Terimakasih {self.nama} ===")
                    print("=== Jangan Lupa Datang Kembali ===\n")
                    exit()
                else :
                    print("Pilihan tidak tersedia")
                os.system('pause')

    def Absen_Guru(self) :
        while True :
            print(f"=== Selamat Datang {self.nama} ===")
            print(f"=== Menu Absen ===")
            print(f"=== [1] Izin")
            print(f"=== [2] Absen Jam datang")
            print(f"=== [3] Absen Jam selesai")
            print(f"=== [4] Absen Siswa")
            print(f"=== [0] kembali")
            pilih = int(input("Pilih Menu : "))
            ag = absen_guru(db)
            if pilih == 1 :
                ag.izin(self.id)
            elif pilih == 2 :
                ag.absen_datang(self.id)
            elif pilih == 3 :
                ag.absen_pulang(self.id)
            elif pilih == 4 :
                ag.absen_siswa(self.id)
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')

class akses_Pegawai(Pegawai):
    def __init__(self, db, id, nama):
        super().__init__(db)
        self.id = id
        self.nama = nama
    
    def menu(self) :
        while True :
            print(f"=== Selamat Datang {self.nama} ===")
            print("==[1] Absen ")
            print("==[2] Cari Data")
            print("==[3] Tambah Data")
            print("==[4] Ubah Data")
            print("==[5] Detele")
            print("==[0] logout")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 :
                self.Absen_pegawai() # done
            elif pilih == 2 :
                self.Cari() #not yet test
            elif pilih == 3 :
                self.Insert()
            elif pilih == 4 :
                self.ubah()
            elif pilih == 5 :
                self.delete()
            elif pilih == 0 :
                print(f"\n\t=== Terimakasih {self.nama} ===")
                print("=== Jangan Lupa Datang Kembali ===\n")
                exit()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')

    def Absen_pegawai(self) :
        while True :
            print(f"=== selamat datang {self.nama} ===")
            print(f"=== Menu Absen ===")
            print(f"=== [1] Izin")
            print(f"=== [2] Absen Jam datang")
            print(f"=== [3] Absen Jam selesai")
            print(f"=== [0] kembali")
            pilih = int(input("Pilih Menu : "))
            ab = absen_pegawai(db)
            if pilih == 1 :
                ab.izin(self.id)
            elif pilih == 2 :
                ab.absen_datang(self.id)
            elif pilih == 3 :
                ab.absen_pulang(self.id)
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')


    def Cari(self) :
        while True :
            print(f"=== Selamat Datang {self.nama} ===")
            print(f"=== Menu Cari ===")
            print("=== [1] Pegawai")
            print("=== [2] Guru")
            print("=== [3] Siswa")
            print("=== [0] kembali")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 : 
                self.read_Pegawai()
            elif pilih == 2 : 
                gu = Guru(db)
                gu.read_guru()
            elif pilih == 3 : 
                mu = Siswa(db)
                mu.read_siswa()
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')

        
    def Insert(self) :
        while True :
            print(f"=== Selamat Datang {self.nama} ===")
            print(f"=== Menu Tambah Data ===")
            print("===[1] Transaksi")
            print("===[2] Jadwal Pelajaran")
            print("===[3] Jadwal Pelayanan")
            print("===[4] Ruang")
            print("===[5] Paket Belajar")
            print("===[0] kembali")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 : 
                pass
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")
            os.system('pause')


    def ubah(self) :
        while True :
            print(f"=== selamat datang {self.nama} ===")
            print(f"=== Menu Read ===")
            print("===[1] Ubah data diri")
            print("===[2] Ubah data ruang")
            print("===[3] Ubah Jadwal Pelajaran")
            print("===[4] Ubah Jadwal Pelayanan")
            print("===[5] Ubah Paket Belajar")
            print("===[0] kembali")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 : 
                self.update_pegawai(self.id)
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")

    def delete(self) :
        while True :
            print(f"=== selamat datang {self.nama} ===")
            print(f"=== Menu Hapus ===")
            print("===[1] Hapus data diri")
            print("===[2] Hapus data guru")
            print("===[3] Hapus data siswa")
            print("===[0] kembali")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 : 
                pass
            elif pilih == 0 :
                self.menu()
            else :
                print("Pilihan tidak tersedia")
