# import xmlrpc bagian client saja
import xmlrpc.client

# import library yg dibutuhkan
import os

# buat stub (proxy) untuk client
s = xmlrpc.client.ServerProxy('http://192.168.1.42:8008')

def main():
    # Fungsi untuk print menu
    def print_menu():
        print("====== KALKULATOR MODERN 2020 ======")
        print("1. Kalkulasi Pertambahan")
        print("2. Kalkulasi Pengurangan")
        print("3. Kalkulasi Perkalian")
        print("4. Kalkulasi Pembagian")        
        print("5. Cari Aktivitas")
        print("6. Keluar")
        print("====================================")

    loop = True
    int_choice = -1

    # perulangan menu hingga false
    while loop:
        print_menu()
        choice = input("Masukan Pilihanmu [1-6]: ")

        # menu operasi tambah
        if choice == '1':
            x = int(input('Masukan angka pertama: '))
            y = int(input('Masukan angka kedua: '))
            # melakukan print hasil fungsi tambah
            print(s.tambah(x,y))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        # menu operasi kurang
        elif choice == '2':
            x = int(input('Masukan angka pertama: '))
            y = int(input('Masukan angka kedua: '))
            # melakukan print hasil fungsi kurang
            print(s.kurang(x,y))
            input()   
            os.system('cls' if os.name == 'nt' else 'clear')
        # menu operasi kali
        elif choice == '3':
            x = int(input('Masukan angka pertama: '))
            y = int(input('Masukan angka kedua: '))
            # melakukan print hasil fungsi kali
            print(s.kali(x,y))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        # menu operasi bagi
        elif choice == '4':
            x = int(input('Masukan angka pertama: '))
            y = int(input('Masukan angka kedua: '))
            # melakukan print hasil fungsi bagi
            print(s.bagi(x,y))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        # menu operasi cari
        elif choice == '5':
            x = input('Kapan aktivitasnya?: ')
            result = s.cari(x)
            # melakukan print hasil fungsi cari menggunakan looping
            for i in range(len(result)):
                print(result[i])
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        # menu keluar dari program
        elif choice == '6':
            int_choice = -1
            print("Exiting..")
            loop = False
            exit.__str__()
        # menu input salah
        else:
            input("Wrong menu selection. Enter any key to try again..")
            os.system('cls' if os.name == 'nt' else 'clear')
  
if __name__== "__main__":
    # memanggil fungsi menu
    main()
