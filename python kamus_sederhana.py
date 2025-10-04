kamus = {}
while True:
      print("\n=== DAFTAR PILIHAN ===")
      print("1. Tambah Kata")
      print("2. Cari Arti")
      print("3. Tampilkan Semua")
      print("4. Keluar")
      print("5. Cari Kata")
      print("6. Edit Kata")

      pilih = input("Pilih Menu(1-5): ")

      if pilih == "1":
         nama = input("masukkan kata: ")
         arti = input("masukkan artinya: ")
         kamus[nama] = arti
         print("kata berhasil di tambahkan!")

      elif pilih == "2":
         cari_kata = input("masukkan kata yang mau di cari: ")
         if cari_kata in kamus:
            print(f"Arti {cari_kata} adalah {kamus[cari_kata]}")
         else:
            print("kata tidak di temukan!")

      elif pilih == "3":
           print("\n=== TAMPILKAN KAMUS ===")
           if not kamus:
              print("kamus masih kosong")
           else:
              for k, v in kamus.items():
                  print(f"{k}: {v}")

      elif pilih == "4":
          print("terimakasih telah mencoba program ini")
          break

      elif pilih == "5":
          cari = input("masukkan kata yang mau di cari: ")
          ketemu = False
          for k, v in kamus.items():
              if v == cari:
                 print(f"Bahasa Inggris dari kata {cari} adalah {k}")
                 ketemu = True
          if not ketemu:
             print("kata tidak di temukan!")
      elif pilih == "6":
           ubah = input("masukkan kata yang mau diubah: ")
           if ubah in kamus:
              kata_baru = input("masukkan arti baru: ")
              kamus[ubah] = kata_baru
              print("kata behasil di ubah")
           else:
              print("kata tidak ditemukan")

      else:
          print("menu tidak valid!")
