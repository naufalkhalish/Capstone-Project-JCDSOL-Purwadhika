# Inisialisasi data dalam bentuk list dan dictionary
buku = [
{'judul' : 'Slow Boat', 'penulis' : 'Hideo Furukawa', 'tahun_terbit' : '2017', 'kategori' : 'Fiksi', 'jumlah_stok' : 40}, 
{'judul' :'Beloved', 'penulis' : 'Toni Morrison', 'tahun_terbit' : '2004', 'kategori' : 'Politik & Ilmu Sosial', 'jumlah_stok' : 30}, 
{'judul' : 'Almond', 'penulis' : 'Won Pyung Sohn', 'tahun_terbit' : '2021', 'kategori' : 'Fiksi', 'jumlah_stok' : 20}, 
{'judul' : 'Ikigai', 'penulis' : 'Hector Garcia', 'tahun_terbit' : '2018', 'kategori' : 'Pengembangan Diri', 'jumlah_stok' : 40}, 
{'judul' : 'Quiet', 'penulis' : 'Susan Cain', 'tahun_terbit' : '2013', 'kategori' : 'Edukasi', 'jumlah_stok' : 20}]
peminjaman = []
buku_data = []

# Fungsi untuk kembali ke menu utama

def kembali_ke_menu_utama():
    while True:
        back = input('Ketik "Keluar" untuk kembali ke menu utama: ')
        try:
            if back.lower() == 'keluar':
                menu_utama()
                break
            else:
                print('Masukkan input yang valid ("keluar")')
        except:
            print('Terjadi kesalahan. Pastikan input yang dimasukkan valid.')


# Fungsi untuk menambahkan buku
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun_terbit = int(input("Masukkan tahun terbit buku: "))
    kategori = input("Masukkan kategori buku: ")
    while(True):
        try:
            jumlah_stok = int(input("Masukkan jumlah stok: "))
            if jumlah_stok > 0:
                print('Berhasil masukkan jumlah stok')
                break
            else:
                print('Mohon masukkan angka yang lebih besar dari 0.')
        except ValueError:
            print('Mohon masukkan angka yang valid.')

    buku_data = {
        'judul': judul,
        'penulis': penulis,
        'tahun_terbit': tahun_terbit,
        'kategori': kategori,
        'jumlah_stok': jumlah_stok
    }
    buku.append(buku_data)
    print("Buku berhasil ditambahkan.")
    kembali_ke_menu_utama()

# Fungsi untuk menampilkan daftar buku
def daftar_buku():
    print("Daftar Buku:")
    for i, data in enumerate(buku, start=1):
        print(f"{i}. Judul: {data['judul']}, Penulis: {data['penulis']}, Tahun Terbit: {data['tahun_terbit']}, Kategori: {data['kategori']}, Jumlah Stok: {data['jumlah_stok']}")
    
    kembali_ke_menu_utama()

# Fungsi untuk melakukan peminjaman
def peminjam_buku():
    while(True):
        for i, data in enumerate(buku, start=1):
            print(f"{i}. Judul: {data['judul']}, Penulis: {data['penulis']}, Tahun Terbit: {data['tahun_terbit']}, Kategori: {data['kategori']}, Jumlah Stok: {data['jumlah_stok']}")

        try:
            buku_id = int(input("Pilih buku yang akan dipinjam (masukkan nomor): "))
            if 1 <= buku_id <= len(buku):
                peminjam = input("Masukkan nama peminjam: ")
                
                while(True):
                    try:
                        permintaan_quantity_peminjam = int(input("Masukkan kuantitas buku: "))
                        if permintaan_quantity_peminjam > 0:
                            if buku[buku_id - 1]['jumlah_stok'] >= permintaan_quantity_peminjam:
                                peminjaman_data = {
                                    'buku_id': buku_id - 1,
                                    'peminjam': peminjam,
                                    'kuantitas': permintaan_quantity_peminjam,
                                }
                                peminjaman.append(peminjaman_data)
                    
                                # Mengurangi stok buku
                                buku[buku_id - 1]['jumlah_stok'] -= permintaan_quantity_peminjam
                    
                                print("Peminjaman berhasil.")
                                kembali_ke_menu_utama()
                                break  # Keluar dari loop input kuantitas
                            else:
                                print("Mohon Maaf, stok tidak mencukupi.")
                        else:
                            print('Mohon masukkan angka lebih dari 0')
                    except ValueError:
                        print('Mohon masukkan angka yang valid.')
                
                break  # Keluar dari loop input buku
            else:
                print("Buku tidak ditemukan.")
        except ValueError:
            print('Mohon masukkan angka yang valid.')

# Menu Filter Buku
def filter_buku():
    
    print("Pilih kriteria filter:")
    print("1. Judul")
    print("2. Penulis")
    print("3. Tahun Terbit")
    print("4. Kategori")
    print("5. Kembali ke menu utama")

    pilihan_filter = input("Masukkan nomor kriteria filter: ")

    if pilihan_filter == '1':
        kata_kunci = input("Masukkan judul yang dicari: ")
        filtered_buku(kata_kunci.lower(), 'judul')
    elif pilihan_filter == '2':
        kata_kunci = input("Masukkan nama penulis yang dicari: ")
        filtered_buku(kata_kunci.lower(), 'penulis')
    elif pilihan_filter == '3':
        kata_kunci = input("Masukkan tahun terbit yang dicari: ")
        filtered_buku(kata_kunci.lower(), 'tahun_terbit')
    elif pilihan_filter == '4':
        kata_kunci = input("Masukkan kategori yang dicari: ")
        filtered_buku(kata_kunci.lower(), 'kategori')
    elif pilihan_filter == '5':
        print("Kembali ke menu utama.")
        menu_utama()
    else:
        print("Pilihan tidak valid. Mohon masukkan input yang sesuai (1-5)")

def filtered_buku(kata_kunci, pilihan):
    filtered = [f for f in buku if kata_kunci.lower() in f[pilihan].lower()]

    if filtered:
        print("Hasil Filter:")
        for i, data in enumerate(filtered, start=1):
            print(f"{i}. Judul: {data['judul']}, Penulis: {data['penulis']}, Tahun Terbit: {data['tahun_terbit']}, Kategori: {data['kategori']}, Jumlah Stok: {data['jumlah_stok']}")
        kembali_ke_menu_utama()
    else:
        print("Tidak ada buku yang sesuai dengan kriteria filter.")
        kembali_ke_menu_utama()

# Menu Edit Buku
def edit_buku():
    print("Daftar Buku:")
    for i, data in enumerate(buku, start=1):
        print(f"{i}. Judul: {data['judul']}, Penulis: {data['penulis']}, Tahun Terbit: {data['tahun_terbit']}, Kategori: {data['kategori']}, Jumlah Stok: {data['jumlah_stok']}")

    try:
        buku_id = int(input("Pilih buku yang akan diedit (masukkan nomor): "))
        if 1 <= buku_id <= len(buku):
            # menambil buku dengan indeks buku_id - 1 karena indeks dimulai dari 0
            buku_terpilih = buku[buku_id - 1]

            # Menu Edit
            print("\nMenu Edit:")
            print("1. Edit Judul")
            print("2. Edit Nama Penulis")
            print("3. Edit Tahun Terbit")
            print("4. Edit Kategori")
            print("5. Edit Jumlah Stok")
            pilihan_edit = input("Pilih nomor menu yang ingin diedit (1-5): ")

            if pilihan_edit == '1':
                buku_terpilih['judul'] = input("Masukkan judul baru: ")
            elif pilihan_edit == '2':
                buku_terpilih['penulis'] = input("Masukkan nama penulis baru: ")
            elif pilihan_edit == '3':
                buku_terpilih['tahun_terbit'] = input("Masukkan tahun terbit baru: ")
            elif pilihan_edit == '4':
                buku_terpilih['kategori'] = input("Masukkan kategori baru: ")
            elif pilihan_edit == '5':
                buku_terpilih['jumlah_stok'] = int(input("Masukkan jumlah stok baru: "))
            else:
                print("Pilihan tidak valid.")
                return

            print(f"\nData buku setelah diedit:\n{buku_terpilih}")
            kembali_ke_menu_utama()
        else:
            print("Buku tidak ditemukan.")
            kembali_ke_menu_utama()
    except ValueError:
        print("Masukkan nomor buku yang valid.")
        kembali_ke_menu_utama()

    menu_utama()

# Menu Delete Buku
def delete_buku():
    print("Daftar Buku:")
    for i, data in enumerate(buku, start=1):
        print(f"{i}. Judul: {data['judul']}, Penulis: {data['penulis']}, Tahun Terbit: {data['tahun_terbit']}, Kategori: {data['kategori']}, Jumlah Stok: {data['jumlah_stok']}")

    try:
        buku_id = int(input("Pilih buku yang akan dihapus (masukkan nomor): "))
        if 1 <= buku_id <= len(buku):
            deleted_book = buku.pop(buku_id - 1)
            print(f"Buku '{deleted_book['judul']}' berhasil dihapus.")
            kembali_ke_menu_utama()
        else:
            print("Buku tidak ditemukan.")
            kembali_ke_menu_utama()
    except ValueError:
        print("Masukkan nomor buku yang valid.")
        kembali_ke_menu_utama()

# Menu Utama
def menu_utama():
    print("\nSelamat Datang di Perpustakaan")
    print("1. Tambah Buku")
    print("2. Daftar Buku")
    print("3. Peminjaman Buku")
    print("4. Filter Buku")
    print("5. Edit Buku")
    print("6. Hapus Buku")
    print("7. Keluar")
    
    pilihan = input("Pilih operasi (masukkan nomor): ")
    
    if pilihan == '1':
        tambah_buku()
    elif pilihan == '2':
        daftar_buku()
    elif pilihan == '3':
        peminjam_buku()
    elif pilihan == '4':
        filter_buku()
    elif pilihan == '5':
        edit_buku()
    elif pilihan == '6':
        delete_buku()
    elif pilihan == '7':
        print("Terima kasih. Sampai jumpa!")
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")

menu_utama()