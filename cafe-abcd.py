from prettytable import PrettyTable

print("============================")
print("       Caffe ABCD           ")
print("============================")
print("Cafe ABCD yang menyediakan makanan dan minuman di Kota Karawang. Berikut daftar menu makanan yang tersedia:\n")

daftar_makanan = [
    {"kode makanan": '01', "menu makanan": 'steak ayam', "tarif": 25000},
    {"kode makanan": '02', "menu makanan": 'steak sirlon sapi', "tarif": 45000},
    {"kode makanan": '03', "menu makanan": 'steak kambing', "tarif": 45000},
    {"kode makanan": '04', "menu makanan": 'nasi gurih', "tarif": 15000},
    {"kode makanan": '05', "menu makanan": 'nasi goreng', "tarif": 25000},
    {"kode makanan": '06', "menu makanan": 'mie ayam', "tarif": 15000},
    {"kode makanan": '07', "menu makanan": 'dimsum ayam', "tarif": 15000},
    {"kode makanan": '08', "menu makanan": 'dimsum sapi', "tarif": 20000},
    {"kode makanan": '09', "menu makanan": 'dimsum jamur', "tarif": 15000},
    {"kode makanan": '10', "menu makanan": 'kripik ubi', "tarif": 5000}
]

tabel1_makanan = PrettyTable()
tabel1_makanan.field_names = ["Kode Makanan", "Menu Makanan", "Tarif"]

for makanan in daftar_makanan:
    tabel1_makanan.add_row(
        [makanan["kode makanan"], makanan["menu makanan"], makanan["tarif"]])

print(tabel1_makanan)

print("\ndaftar minuman:")
daftar_minuman = [
    {"kode minuman": '01', "menu minuman": 'jus apel', "tarif": 15000},
    {"kode minuman": '02', "menu minuman": 'Jus Jeruk', "tarif": 15000},
    {"kode minuman": '03', "menu minuman": 'Jus Alpukat', "tarif": 15000},
    {"kode minuman": '04', "menu minuman": 'jus mangga', "tarif": 15000},
    {"kode minuman": '05', "menu minuman": 'cappuccino', "tarif": 15000},
    {"kode minuman": '06', "menu minuman": 'air mineral', "tarif": 10000},
    {"kode minuman": '07', "menu minuman": 'kopi tubruk', "tarif": 10000}
]

tabel2_minuman = PrettyTable()
tabel2_minuman.field_names = ["Kode Minuman", "Menu Minuman", "Tarif"]

for minuman in daftar_minuman:
    tabel2_minuman.add_row(
        [minuman["kode minuman"], minuman["menu minuman"], minuman["tarif"]])

print(tabel2_minuman)

print("\nmenu tambahan: ")
daftar_tambahan = [
    {"kode menu tambahan": 'A', "menu tambahan": 'nasi uduk', "tarif": 5000},
    {"kode menu tambahan": 'B', "menu tambahan": 'nasi putih', "tarif": 5000},
    {"kode menu tambahan": 'C', "menu tambahan": 'kuah soto', "tarif": 5000}
]

tabel3_tambahan = PrettyTable()
tabel3_tambahan.field_names = ["Kode Menu Tambahan", "Menu Tambahan", "Tarif"]

for tambahan in daftar_tambahan:
    tabel3_tambahan.add_row(
        [tambahan["kode menu tambahan"], tambahan["menu tambahan"], tambahan["tarif"]])

print(tabel3_tambahan)

print("\n\tINPUT PEMBAYARAN")
print("==============================")
daftar_pembayaran = []

while True:
    print("\n=============================")
    nama_pelanggan = input(f"Nama Pelanggan \t: ")
    pesan_makanan = input("\nMau pesan makanan? [y/t]\t: ")
    if pesan_makanan.lower() == "y":
        kode_makanan = input("Kode Makanan\t: ")
        nama_makanan = ""
        tarif_makanan = 0  # Menetapkan nilai default tarif makanan

        for makanan in daftar_makanan:
            if makanan["kode makanan"] == kode_makanan:
                nama_makanan = makanan["menu makanan"]
                tarif_makanan = makanan["tarif"]

        if nama_makanan:
            print("Nama Makanan\t:", nama_makanan)
            print("Tarif Makanan\t:", tarif_makanan)
        else:
            print("Makanan tidak ditemukan. Pesanan tidak ditambahkan.")
    else:
        nama_makanan = ""
        tarif_makanan = 0
        print("Nama Makanan\t:", nama_makanan)
        print("Tarif Makanan\t:", tarif_makanan)

    pesan_minuman = input("\nMau pesan minuman? [y/t]:\t ")
    if pesan_minuman.lower() == "y":
        kode_minuman = input("Kode Minuman\t: ")
        nama_minuman = ""
        tarif_minuman = 0  # Menetapkan nilai default tarif minuman

        for minuman in daftar_minuman:
            if minuman["kode minuman"] == kode_minuman:
                nama_minuman = minuman["menu minuman"]
                tarif_minuman = minuman["tarif"]

        if nama_minuman:
            print("Nama Minuman\t:", nama_minuman)
            print("Tarif Minuman\t:", tarif_minuman)
        else:
            print("Minuman tidak ditemukan. Pesanan tidak ditambahkan.")
    else:
        nama_minuman = ""
        tarif_minuman = 0
        print("Nama Minuman\t:", nama_minuman)
        print("Tarif Minuman\t:", tarif_minuman)

    kode_tambahan = input(
        "\nKode Menu Tambahan (ketik 'tidak' jika tidak ada)\t: ")
    nama_tambahan = ""
    tarif_tambahan = 0  # Menetapkan nilai default tarif tambahan

    if kode_tambahan in ['A', 'B', 'C']:
        for tambahan in daftar_tambahan:
            if tambahan["kode menu tambahan"] == kode_tambahan:
                nama_tambahan = tambahan["menu tambahan"]
                tarif_tambahan = tambahan["tarif"]
        if nama_tambahan:
            print("Nama Menu Tambahan\t:", nama_tambahan)
            print("Tarif Menu Tambahan\t:", tarif_tambahan)
        else:
            print("Minuman tidak ditemukan. Pesanan tidak ditambahkan.")
    else:
        nama_tambahan = ""
        tarif_tambahan = 0
        print("Nama Menu Tambahan\t:", nama_tambahan)
        print("Tarif Menu Tambahan\t:", tarif_tambahan)

    if nama_makanan or nama_minuman or nama_tambahan:
        jumlah_bayar = tarif_makanan + tarif_minuman + tarif_tambahan
        print("\n=================================")
        print("jumlah bayar\t:", jumlah_bayar)
        ppn = 0.11 * jumlah_bayar
        print("PPN 11%\t\t:", ppn)
        total_bayar = jumlah_bayar + ppn
        print("Total Bayar\t:", total_bayar)
        print("====================================")

        daftar_pembayaran.append(
            [nama_pelanggan, nama_makanan, nama_minuman, nama_tambahan, total_bayar])

    pesan_lagi = input("Ada pelanggan lagi? [y/t]: ")
    if pesan_lagi.lower() == "t":
        print("\nDAFTAR PEMBAYARAN MAKANAN")
        if len(daftar_pembayaran) > 0:
            tabel_pembayaran = PrettyTable()
            tabel_pembayaran.field_names = [
                "No", "Nama Pelanggan", "Nama Makanan", "Nama Minuman", "Nama Tambahan", "Total Bayar"]
            for i, pembayaran in enumerate(daftar_pembayaran):
                tabel_pembayaran.add_row(
                    [i + 1, pembayaran[0], pembayaran[1], pembayaran[2], pembayaran[3], pembayaran[4]])

            print(tabel_pembayaran)

            nama_cari = input("\nMasukkan nama yang ingin dicari\t: ")

            pencarian = []
            for i, pembayaran in enumerate(daftar_pembayaran):
                if pembayaran[0] == nama_cari:
                    pencarian.append(pembayaran)

            if len(pencarian) > 0:
                tabel_pencarian = PrettyTable()
                tabel_pencarian.field_names = [
                    "No", "Nama Pelanggan", "Nama Makanan", "Nama Minuman", "Nama Tambahan", "Total Bayar"]
                for i, pembayaran in enumerate(pencarian):
                    tabel_pencarian.add_row(
                        [i + 1, pembayaran[0], pembayaran[1], pembayaran[2], pembayaran[3], pembayaran[4]])

                print("\nHasil Pencarian:")
                print(tabel_pencarian)
            else:
                print("Data tidak ditemukan.")
        else:
            print("Tidak ada pembayaran yang dilakukan.")
        break
