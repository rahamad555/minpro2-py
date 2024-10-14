from prettytable import PrettyTable

class AnggotaGym:
    def __init__(self, id, nama, alamat, no_telepon):

        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.no_telepon = no_telepon

# class User:
#     def __init__(self, username, password, role):
#         self.username = username
#         self.password = password
#         self.role = role

class SistemPendaftaran:
    def __init__(self):
        self.anggota = []
        self.users = [
            User("admin", "password", "admin"),
            User("user", "password", "user")
        ]

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def tambah_anggota(self):
        id = len(self.anggota) + 1
        nama = input("Masukkan nama anggota: ")
        alamat = input("Masukkan alamat anggota: ")
        no_telepon = input("Masukkan no telepon anggota: ")
        anggota_baru = AnggotaGym(id, nama, alamat, no_telepon)
        self.anggota.append(anggota_baru)
        print("Anggota baru berhasil ditambahkan!")

    def lihat_anggota(self):
        if not self.anggota:
            print("Tidak ada anggota yang terdaftar.")
        else:
            tabel = PrettyTable(["ID", "Nama", "Alamat", "No Telepon"])
            for anggota in self.anggota:
                tabel.add_row([anggota.id, anggota.nama, anggota.alamat, anggota.no_telepon])
            print(tabel)

    def ubah_anggota(self):
        id_anggota = int(input("Masukkan ID anggota yang ingin diubah: "))
        for anggota in self.anggota:
            if anggota.id == id_anggota:
                anggota.nama = input("Masukkan nama baru: ")
                anggota.alamat = input("Masukkan alamat baru: ")
                anggota.no_telepon = input("Masukkan no telepon baru: ")
                print("Anggota berhasil diubah!")
                return
        print("Anggota tidak ditemukan.")

    def hapus_anggota(self):
        id_anggota = int(input("Masukkan ID anggota yang ingin dihapus: "))
        for anggota in self.anggota:
            if anggota.id == id_anggota:
                self.anggota.remove(anggota)
                print("Anggota berhasil dihapus!")
                return
        print("Anggota tidak ditemukan.")

def main():
    sistem = SistemPendaftaran()
    while True:
        print("Sistem Pendaftaran Anggota Gym")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            user = sistem.login(username, password)
            if user:
                print("Login berhasil!")
                if user.role == "admin":
                    while True:
                        print("Menu Admin")
                        print("1. Tambah Anggota")
                        print("2. Lihat Anggota")
                        print("3. Ubah Anggota")
                        print("4. Hapus Anggota")
                        print("5. Keluar")
                        pilihan_admin = input("Masukkan pilihan: ")
                        if pilihan_admin == "1":
                            sistem.tambah_anggota()
                        elif pilihan_admin == "2":
                            sistem.lihat_anggota()
                        elif pilihan_admin == "3":
                            sistem.ubah_anggota()
                        elif pilihan_admin == "4":
                            sistem.hapus_anggota()
                        elif pilihan_admin == "5":
                            break
                        else:
                            print("Pilihan tidak valid.")
                elif user.role == "user":
                    while True:
                        print("Menu User")
                        print("1. Lihat Anggota")
                        print("2. Keluar")
                        pilihan_user = input("Masukkan pilihan: ")
                        if pilihan_user == "1":
                            sistem.lihat_anggota()
                        elif pilihan_user == "2":
                            break
                        else:
                            print("Pilihan tidak valid.")
            else:
                print("Login gagal!")
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()