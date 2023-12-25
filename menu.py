import os 
from connector import database
from createtable import created_table
from sampledata import created_data
from query.aktor import Siswa, Guru, Pegawai
from query.todo import login
from query.akses import akses_Pegawai

db = database()
db.connect()
created_table(db)


while True :
    os.system('cls')
    print("="*22)
    print("=== SELAMAT DATANG ===")
    print("===       DI       ===")
    print("=== RUANG  BELAJAR ===")
    print("="*22)
    print("===== Menu Akses =====")
    print("===[1] Siswa\t   ===")
    print("===[2] Guru \t   ===")
    print("===[3] Pegawai\t   ===")
    print("===[0] Keluar\t   ===")
    print("======================")
    pilih = int(input("Pilih Menu : "))
    if pilih == 1 :
        print("\n\t===== Menu Siswa =====")
        print("\t===[1] Registrasi      ==")
        print("\t===[2] Login           ==")
        print("\t=========================")

        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            print("\n\t==== Menu Registrasi ====")
            print("\t===[1] Pelajar         ==")
            print("\t===[2] Pengajar        ==")
            print("\t=========================")

            pilih = int(input("Pilih Menu : "))
            if pilih == 1:
                pass
            elif pilih == 2:
                pass
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")

        elif pilih == 2 :
            print("\n\t====== Menu  Login ======")
            print("\t===[1] Pelajar         ==")
            print("\t===[2] Pengajar        ==")
            print("\t=========================")

            pilih = int(input("Pilih Menu : "))
            if pilih == 1:
                pass
            elif pilih == 2:
                pass
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")

        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")

    elif pilih == 2 :
        print("\n\t====== Menu  Admin ======")
        print("\t===[1] Registrasi      ==")
        print("\t===[2] Login           ==")
        print("\t=========================")

        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            print("\n\t==== Menu Registrasi ====")
            print("\t===[1] Admin           ==")
            print("\t=========================")

            pilih = int(input("Pilih Menu : "))

        elif pilih == 2 :
           print("\n\t====== Menu  Login ======")
           print("\t===[1] Admin           ==")
           print("\t=========================")

           pilih = int(input("Pilih Menu : "))

        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")

    elif pilih == 3 :
        print("\n\t===== Menu Pegawai =====")
        print("\t===[1] Registrasi      ==")
        print("\t===[2] Login           ==")
        print("\t=========================")

        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            peg = Pegawai(db)
            peg.insert_pegawai()
        elif pilih == 2 :
            id = login(db)
            get_id_name = id.cheking("pegawai")
            id, nama = get_id_name
            my = akses_Pegawai(db,id,nama)
            my.menu()

            
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")

    elif pilih == 99:
        created_data(db)

    elif pilih == 0 :
        print("\n\t=== Terimakasih ===")
        print("=== Jangan Lupa Datang Kembali ===\n")
        break

    else :
        print("Pilihan tidak tersedia")
    os.system('pause')
