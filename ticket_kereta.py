from os import system
from json import dump, load
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Penyimpanan ticket Kereta
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
	if len(container) !=0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_ticket=None, all_data=False):
	if id_ticket != None and all_data == False:
		print(f"ID : {id_ticket}")
		print(f"DESTINASI : {tickets[id_ticket]['destinasi']}")
		print(f"KERETA_API : {tickets[id_ticket]['kereta_api']}")
		print(f"TERMINAL : {tickets[id_ticket]['terminal']}")
	elif all_data == True:
		for id_ticket in tickets:# lists, string, dict
			print(f"ID : {id_ticket}")
			print(f"DESTINASI : {tickets[id_ticket]['destinasi']}")
			print(f"KERETA_API : {tickets[id_ticket]['kereta_api']}")
			print(f"TERMINAL : {tickets[id_ticket]['terminal']}")

def view_tickets():
	print_header("DAFTAR TIKET TERSEDIA")
	if not_empty(tickets):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA TIKET TERSEDIA")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_ticket(ticket, train):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	counter = len(ticket) + 1
	first = ticket[0].upper()
	last_4 = train[-4:]
	
	id_ticket = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_ticket

def add_ticket():
	print_header("MENAMBAHKAN ticket BARU")
	destinasi = input("DESTINASI \t: ")
	kereta_api = input("KERETA_API \t: ")
	terminal = input("TERMINAL \t: ")
	respon = input(f"Apakah yakin ingin menambahkan ticket : {destinasi} ? (Y/N) ")
	if verify_ans(respon):
		id_ticket = create_id_ticket(ticket=destinasi, train=kereta_api)
		tickets[id_ticket] = {
			"destinasi" : destinasi,
			"kereta_api" : kereta_api,
			"terminal" : terminal
		}
		saved= save_data_tickets()
		if saved:
			print("Data ticket Tersimpan.")
		else:
			print("Kesalahan saat menyimpan")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_destinasi(ticket):
	for id_ticket in tickets:
		if tickets[id_ticket]['destinasi'] == ticket:
			return id_ticket
	else:
		return False

def find_ticket():
	print_header("MENCARI TICKET")
	destinasi = input("destinasi ticket yang Dicari : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print("Data Ditemukan")
		print_data(id_ticket=exists)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_ticket():
	print_header("MENGHAPUS ticket")
	destinasi = input("Destinasi Ticket yang akan Dihapus : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print_data(id_ticket=exists)
		respon = input(f"Yakin ingin mengapus {destinasi} ? (Y/N) ")
		if verify_ans(respon):
			del tickets[exists]
			saved= save_data_tickets()
			if saved:
				print("Data ticket Telah Dihapus.")
			else:
				print("Kesalahan saat menyimpan")
		else:
			print("Data ticket Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_ticket_destinasi(id_ticket):
	print(f"Destinasi Lama : {tickets[id_ticket]['destinasi']}")
	new_destinasi = input("Masukkan Destinasi baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		tickets[id_ticket]['destinasi'] = new_destinasi
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")

def update_ticket_kereta_api(id_ticket):
	print(f"kereta api Lama : {tickets[id_ticket]['kereta_api']}")
	new_kereta_api = input("Masukkan kereta api Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result:
		tickets[ticket]['kereta_api'] = new_kereta_api
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")

def update_ticket_terminal(ticket):
	print(f"Terminal sebelumnya : {tickets[ticket]['terminal']}")
	new_terminal = input("Masukkan Terminal Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result:
		tickets[ticket]['terminal'] = new_terminal
		print("Data Telah di simpan")
		print_data(ticket)
	else:
		print("Data Batal diubah")

def update_ticket():
	print_header("MENGUPDATE INFO ticket")
	destinasi = input("Destinasi yang akan di-update : ")
	exists = searching_by_destinasi(destinasi)
	if exists:
		print_data(exists)
		print("EDIT FIELD [1] DESTINASI - [2] KERETA_API - [3] TERMINAL")
		respon = input ("MASUKAN PILIHAN (1/2/3) : ")
		if respon == "1":
			update_ticket_destinasi(exists)
		elif respon == "2":
			update_ticket_kereta_api(exists)
		elif respon == "3":
			update_ticket_terminal(exists)
		saved = save_data_tickets()
		if saved:
			print("Data ticket Telah di-update.")
		else:
			print("Kesalahan saat menyimpan")
	
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def tent_app():
	print_header("App ini dibuat untuk memudahkan pengguna dalam menyimpan, mencari, menambah, dan menghapus data ticket kereta api yang ada")
	input("Tekan ENTER untuk kembali ke MENU")
	
def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("Terima kasih telah berkunjung!")
		return True
	elif char == "1":
		view_tickets()
	elif char == "2":
		add_ticket()
	elif char == "3":
		find_ticket()
	elif char == "4":
		delete_ticket()
	elif char == "5":
		update_ticket()
	elif char == "6":
		tent_app()

def load_data_tickets():
	with open(file_path, 'r') as file:
		data = load(file)
	return data

def save_data_tickets():
	with open(file_path, 'w') as file:
		dump(tickets, file)
	return True

#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "filetxt/tiketz.json"
tickets = load_data_tickets()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)
	