from os import system
from json import dump, load
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Penyimpanan Tiket Kereta
	[1]. Lihat Semua Ticket Yang Tersedia
	[2]. Menambah Ticket Baru
	[3]. Mencari Ticket Tersedia
	[4]. Menghapus Ticket
	[5]. Update Ticket
	[6]. Tentang Aplikasi
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_contact=None, telp=True, hobi=True, all_data=False):
	if id_contact != None and all_data == False:
		print(f"ID : {id_contact}")
		print(f"NAMA : {contacts[id_contact]['nama']}")
		print(f"TELP : {contacts[id_contact]['telp']}")
		print(f"HOBI : {contacts[id_contact]['hobi']}")
	elif hobi == False and all_data == False:
		print(f"ID : {id_contact}")
		print(f"NAMA : {contacts[id_contact]['nama']}")
		print(f"TELP : {contacts[id_contact]['telp']}")
	elif all_data == True:
		for id_contact in contacts: # lists, string, dict
			nama = contacts[id_contact]["nama"]
			telp = contacts[id_contact]["telp"]
			hobi = contacts[id_contact]["hobi"]
			print(f"ID : {id_contact} - NAMA : {nama} - TELP : {telp} - HOBI : {hobi}")

def view_contacts():
	print_header("DAFTAR KONTAK TERSIMPAN")
	if not_empty(contacts):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA KONTAK TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_contact(name, phone):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	counter = len(contacts) + 1
	first = name[0].upper()
	last_4 = phone[-4:]
	
	id_contact = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_contact



def add_contact():
	print_header("MENAMBAHKAN KONTAK BARU")
	nama = input("NAMA \t: ")
	telp = input("TELP \t: ")
	hobi = input("HOBI \t: ")
	respon = input(f"Apakah yakin ingin menyimpan kontak : {nama} ? (Y/N) ")
	if verify_ans(respon):
		id_contact = create_id_contact(name=nama, phone=telp)
		contacts[id_contact] = {
			"nama" : nama,
			"telp" : telp,
			"hobi" : hobi
		}
		saved = save_data_contacts()
		if saved:
			print("Data Kontak Tersimpan.")
		else:
			print("Kesalahan saat menyimpan")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_name(contact):
	for id_contact in contacts:
		if contacts[id_contact]['nama'] == contact:
			return id_contact
	else:
		return False

def find_contact():
	print_header("MENCARI KONTAK")
	nama = input("Nama Kontak yang Dicari : ")
	exists = searching_by_name(nama)
	if exists:
		print("Data Ditemukan")
		print_data(id_contact=exists)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_contact():
	print_header("MENGHAPUS KONTAK")
	nama = input("Nama Kontak yang akan Dihapus : ")
	exists = searching(nama)
	if exists:
		print_data(contact=nama)
		respon = input(f"Yakin ingin menghapus {nama} ? (Y/N) ")
		if verify_ans(respon):
			del contacts[nama]
			saved = save_data_contacts()
			if saved:
				print("Data Kontak Telah Dihapus")
			else:
				print("Kesalahan saat menyimpan")
		else:
			print("Data Kontak Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_contact_nama(contact):
	print(f"Nama Lama : {contact}")
	new_name = input("Masukkan Nama baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		contacts[new_name] = contacts[contact]
		del contacts[contact]
		print("Data Telah di simpan")
		print_data(new_name)
	else:
		print("Data Batal diubah")

def update_contact_telp(contact):
	print(f"Nomor Telpon Lama : {contacts[contact]['telp']}")
	new_telp = input("Masukkan Nomor Telepon Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		contacts[contact]['telp'] = new_telp
		print("Data Telah di simpan")
		print_data(contact)
	else:
		print("Data Batal diubah")

def update_contact_hobi(contact):
	pass

def update_contact():
	print_header("MENGUPDATE INFO KONTAK")
	nama = input("Nama Kontak yang akan di-update : ")
	exists = searching(nama)
	if exists:
		print_data(nama)
		print("EDIT FIELD [1] NAMA - [2] TELP - [3] HOBI")
		respon = input("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_contact_nama(nama)
		elif respon == "2":
			update_contact_telp(nama)
		elif respon == "3":
			update_contact_hobi(nama)
		saved = save_data_contacts()
		if saved:
			print("Data Kontak Telah di-update.")
		else:
			print("Kesalahan saat menyimpan")

	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")


def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_contacts()
	elif char == "2":
		add_contact()
	elif char == "3":
		find_contact()
	elif char == "4":
		delete_contact()
	elif char == "5":
		update_contact()
	elif char == "6":
		pass

def load_data_contacts():
	with open(file_path, 'r') as file:
		data = load(file)
	return data

def save_data_contacts():
	with open(file_path, 'w') as file:
		dump(contacts, file)
	return True


#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "filetxt/contacts.json"
contacts = load_data_contacts()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)
