import json
import os

# 🔹 Cek apakah file data.json sudah ada
if os.path.exists("data.json"):
    try:
        with open("data.json", "r") as file:
            kamus = json.load(file)
    except json.JSONDecodeError:
        kamus = {}
else:
    kamus = {}

while True:
    print("\n=== DAFTAR PILIHAN ===")
    print("1. Tambah Kata")
    print("2. Cari Arti")
    print("3. Tampilkan Semua")
    print("4. Hapus Kata")
    print("5. Edit Kata")
    print("6. Cari Kata dari Arti")
    print("7. Keluar")

    pilih = input("Pilih Menu (1-7): ")

    # 🔸 TAMBAH KATA
    if pilih == "1":
        nama = input("Masukkan kata: ")
        arti = input("Masukkan artinya: ")
        kamus[nama] = arti
        print("Kata berhasil ditambahkan!")

        # autosave
        with open("data.json", "w") as file:
            json.dump(kamus, file, indent=4)

    # 🔸 CARI ARTI
    elif pilih == "2":
        cari_kata = input("Masukkan kata yang mau dicari: ")
        if cari_kata in kamus:
            print(f"Arti '{cari_kata}' adalah '{kamus[cari_kata]}'")
        else:
            print("Kata tidak ditemukan!")

    # 🔸 TAMPILKAN SEMUA
    elif pilih == "3":
        print("\n=== TAMPILKAN KAMUS ===")
        if not kamus:
            print("Kamus masih kosong.")
        else:
            for k, v in kamus.items():
                print(f"{k}: {v}")

    # 🔸 HAPUS KATA
    elif pilih == "4":
        hapus = input("Masukkan kata yang mau dihapus: ")
        if hapus in kamus:
            del kamus[hapus]
            print("Kata berhasil dihapus!")

            # autosave
            with open("data.json", "w") as file:
                json.dump(kamus, file, indent=4)
        else:
            print("Kata tidak ditemukan!")

    # 🔸 EDIT KATA
    elif pilih == "5":
        ubah = input("Masukkan kata yang mau diubah artinya: ")
        if ubah in kamus:
            arti_baru = input("Masukkan arti baru: ")
            kamus[ubah] = arti_baru
            print("Kata berhasil diubah!")

            # autosave
            with open("data.json", "w") as file:
                json.dump(kamus, file, indent=4)
        else:
            print("Kata tidak ditemukan!")

    # 🔸 CARI KATA DARI ARTI
    elif pilih == "6":
        cari_arti = input("Masukkan arti yang ingin dicari: ")
        ketemu = False
        for k, v in kamus.items():
            if v == cari_arti:
                print(f"Bahasa Inggris dari '{cari_arti}' adalah '{k}'")
                ketemu = True
        if not ketemu:
            print("Kata tidak ditemukan!")

    # 🔸 KELUAR
    elif pilih == "7":
        print("Terima kasih telah mencoba program kamus ini!")
        break

    else:
        print("Menu tidak valid!")
