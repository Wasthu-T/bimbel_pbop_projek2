from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from query.aktor import Siswa, Guru, Pegawai
import locale

# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class absen_pegawai :
    pass

class absen_guru :
    pass

class absen_siswa :
    pass