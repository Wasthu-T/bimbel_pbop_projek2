import mysql.connector

# Membuat koneksi ke MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Membuat objek cursor untuk mengeksekusi perintah SQL
mycursor = mydb.cursor()

# Membuat database baru
mycursor.execute("""CREATE DATABASE Bimbel_pbop;""")
print("\n=== Database berhasil dibuat ===\n")