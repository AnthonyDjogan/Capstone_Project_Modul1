def Call_main_menu():
    print('-----------------------------')
    print('{:^29}'.format('Main Menu'))
    print('-----------------------------')
    print('1. Data Employee')
    print('2. Menambahkan Data Employee')
    print('3. Mengubah Data Employee')
    print('4. Menghapus Data Employee')
    print('5. Exit')
    print('-----------------------------')
    input_main_menu = input('Silahkan Pilih Menu [1-5]: ').strip()
    print()
    return input_main_menu

#==============================================================================================
def Sub_menu_1():       # Data Employee
    print('-----------------------------')
    print("{:^30}".format('Data Employee'))
    print('-----------------------------')
    print('1. Tampilkan Seluruh Data')
    print('2. Tampilkan Data Tertentu')
    print('3. Kembali ke Main Menu')
    print('-----------------------------')
    input_sub_menu_1 = input('Silahkan pilih Sub Menu [1-3]: ').strip()
    print()
    return input_sub_menu_1

#==============================================================================================
def Show_all_data():    
    header = list(employee[0].keys())
    print('===============================================================================================')
    print("{:^85}".format('Daftar Employee'))
    print('===============================================================================================')
    print(f'{header[0]:<12}| {header[1]:<20}| {header[2]:<30}| {header[3]:<7}| {header[4]:<17}|')
    print('-----------------------------------------------------------------------------------------------')

    for index, data in enumerate(employee):     # Memakai enumerate untuk bisa mengakses index. alternatif lain bisa menggunakan range(len(employee))
        print(f"{employee[index]['EMPLOYEE ID']:<12}| {employee[index]['DOMISILI']:<20}| {employee[index]['NAME']:<30}| {employee[index]['GENDER']:<7}| {employee[index]['DEPARTMENT']:<17}|")
        print('===============================================================================================')

#==============================================================================================
def Show_specific_data():    
    ask_input_ID = input('Masukkan EMPLOYEE ID: ').upper().strip()  # Input digunakan sebagai kondisi loop di bawah
    
    header = list(employee[0].keys())
    print('===============================================================================================')
    print("{:^85}".format('Daftar Employee'))
    print('===============================================================================================')
    print(f'{header[0]:<12}| {header[1]:<20}| {header[2]:<30}| {header[3]:<7}| {header[4]:<17}|')
    print('-----------------------------------------------------------------------------------------------')

    id_checker = False      # jika ID ditemukan cheker akan menjadi True. Menghindari output berulang jika ID tidak ditemukan
    for index, ID in enumerate(employee):
        if ask_input_ID == employee[index]['EMPLOYEE ID']:
            print(f"{employee[index]['EMPLOYEE ID']:<12}| {employee[index]['DOMISILI']:<20}| {employee[index]['NAME']:<30}| {employee[index]['GENDER']:<7}| {employee[index]['DEPARTMENT']:<17}|")
            print('===============================================================================================')
            id_checker = True
            break

    if id_checker == False:     # jika setelah loop ID tidak ditemukan (id_checker = False) 
        print('EMPLOYEE ID tidak ditemukan\n')

#==============================================================================================
def SM11_Cari_ID_Lain():
    while True:
        cari_id_lain = input('Apakah anda ingin mencari ID lain [Y/N]:').upper().strip()
        print()
        if cari_id_lain == 'Y':
            Show_specific_data()
        elif cari_id_lain == 'N':
            break
        else:
            print('+++++++++++++++++++++++++++++')
            print(f'Maaf pilihan {cari_id_lain} tidak ada.\nIsi dengan huruf Y/N')
            print('+++++++++++++++++++++++++++++\n')

#==============================================================================================
def Sub_menu_2():       # Menambahkan Data Employee
    print('-----------------------------')
    print("{:^30}".format('Menambah Data Employee'))
    print('-----------------------------')
    print('1. Tambah data employee')
    print('2. Kembali ke Main Menu')
    print('-----------------------------')
    input_sub_menu_2 = input('Silahkan pilih Sub Menu [1-3]: ').strip()
    print()
    return input_sub_menu_2

#==============================================================================================
def Input_checker(input, kolom):
    if kolom == 'DOMISILI':  
        check_character_DOMISILI = ''.join(input.split())   # Menggunakan split lalu join untuk mengabaikan spasi di tengah kata
        if check_character_DOMISILI.isalpha():  # Hanya akan True jika semua item alfabet
            return True
        else:
            print('Nama DOMISILI hanya bisa diisi dengan huruf')
            return False
        
    elif kolom == 'NAME':
        if input.isspace():     # Digunakan untuk menghindari input kosong
            print('Harus memasukkan nama, tidak bisa kosong')
            return False
        else:
            return True
        
    elif kolom == 'GENDER':
        if input not in ['M', 'F']:
            print('Input salah, tolong isi dengan huruf M/F')
            return False
        else:
            return True
        
    elif kolom == 'DEPARTMENT':
        if input in DEPARTMENT:
            return True
        else:
            print('DEPARTMENT yang anda masukkan salah')
            return False

#==============================================================================================
def Input_data_employee():
    while True:
        kolom_input_DOMISILI = 'DOMISILI'
        input_DOMISILI = input('Masukkan DOMISILI: ').title().strip()
       
        if Input_checker(input_DOMISILI, kolom_input_DOMISILI) == True:
            break
        else:
            continue

    while True:
        kolom_input_NAME = 'NAME'
        input_NAME = input('Masukkan nama: ').title()   # Tidak menggunakan .strip() karena cek NAME menggunakan .isspace()

        if Input_checker(input_NAME, kolom_input_NAME) == True:
            break
        else:
            continue

    while True:
        kolom_input_GENDER = 'GENDER'
        input_GENDER = input('Masukkan GENDER [M/F]: ').upper().strip()

        if Input_checker(input_GENDER, kolom_input_GENDER) == True:
            break
        else:
            continue

    while True:
        kolom_input_DEPARTMENT = 'DEPARTMENT'
        Show_list_dept()

        input_DEPARTMENT = input('Masukkan DEPARTMENT: ').title().strip()
        if Input_checker(input_DEPARTMENT, kolom_input_DEPARTMENT) == True:
            break
        else:
            continue    

    # ID generator
    DEPARTMENT_initial = ''.join([word[0].upper() for word in input_DEPARTMENT.split()])    # Loop setiap kata dan mengambil index 0 dari kata tersebut

    kode_domisili = ''.join([word[0].upper() for word in input_DOMISILI.split()])
    panjang_nama = len(input_NAME.strip())
    id_generator = f'{DEPARTMENT_initial}{input_GENDER}{kode_domisili}{panjang_nama}'

    for index, id in enumerate(employee):
        if id_generator == employee[index]['EMPLOYEE ID']:
            panjang_nama += 1
            id_generator = f'{DEPARTMENT_initial}{input_GENDER}{kode_domisili}{panjang_nama}'

    new_employee = {}
    new_employee.update({'EMPLOYEE ID': id_generator})
    new_employee.update({'DOMISILI': input_DOMISILI})
    new_employee.update({'NAME': input_NAME.strip()})
    new_employee.update({'GENDER': input_GENDER})
    new_employee.update({'DEPARTMENT': input_DEPARTMENT})

    while True:
        input_konfirmasi_add_data = input(f'Apakah anda yakin ingin menambahkan data dengan ID {id_generator}? [Y/N]: ').upper().strip()
        print()
        if input_konfirmasi_add_data == 'Y':
            employee.append(new_employee)
            print('\nData Tersimpan')
            Show_all_data()
            break
        elif input_konfirmasi_add_data == 'N':
            break
        else:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('Maaf input anda salah. tolong input Y untuk konfirmasi dan N untuk membatalkan')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            
#==============================================================================================
def Sub_menu_3():       # Mengubah Data Employee
    print('-----------------------------')
    print("{:^30}".format('Mengubah Data Employee'))
    print('-----------------------------')
    print('1. Ubah Data Employee')
    print('2. Kembali ke Main Menu')
    print('-----------------------------')
    input_sub_menu_3 = input('Silahkan pilih Sub Menu [1-3]: ').strip()
    print()
    return input_sub_menu_3

#==============================================================================================
def Input_data_to_change():
    while True:     
        input_id_update = input('Masukkan EMPLOYEE ID: ').upper().strip()   # Cek EMPLOYEE ID
        id_change_cheker = False
        for index, person in enumerate(employee):       
            if input_id_update == employee[index]['EMPLOYEE ID']:
                index_to_update = index
                id_change_cheker = True

                header = list(employee[0].keys())
                print('===============================================================================================')
                print("{:^85}".format(f'Data EMPLOYEE {input_id_update}'))
                print('===============================================================================================')
                print(f'{header[0]:<12}| {header[1]:<20}| {header[2]:<30}| {header[3]:<7}| {header[4]:<17}|')
                print('-----------------------------------------------------------------------------------------------')
                print(f"{employee[index_to_update]['EMPLOYEE ID']:<12}| {employee[index_to_update]['DOMISILI']:<20}| {employee[index_to_update]['NAME']:<30}| {employee[index_to_update]['GENDER']:<7}| {employee[index_to_update]['DEPARTMENT']:<17}|")
                print('===============================================================================================')
                break

        if id_change_cheker == False:
            print('\n++++++++++++++++++++++++++++++++++++')
            print(f'Tidak ada Employee dengan ID : {input_id_update}')
            print('++++++++++++++++++++++++++++++++++++\n')
            break
                
        kolom_to_update = None      # None karena user belum memberi input               
        while True:                 # Konfirmasi EMPLOYEE ID
            input_konfirmasi_change_data = input('Tekan [Y] untuk melanjutkan atau [N] untuk membatalkan: ').upper().strip()
    
            if input_konfirmasi_change_data == 'Y':
                while True:
                    input_kolom_change = input('Masukkan kolom keterangan yang ingin diubah: ').upper().strip()
                    
                    if input_kolom_change in employee[index_to_update].keys():      # tidak perlu enumerate karena hanya looping kolom
                        kolom_to_update = input_kolom_change
                        break

                    else:
                        print('\n+++++++++++++++++++++++++++++++++++++++++++++')
                        print(f'Kolom {input_kolom_change} tidak ada.\n')
                        print('+++++++++++++++++++++++++++++++++++++++++++++\n')
                        continue
                          
                if kolom_to_update == 'DOMISILI':
                    while True:
                        input_new_DOMISILI = input(f'Masukkan {input_kolom_change} baru: ').title().strip()

                        if Input_checker(input_new_DOMISILI, kolom_to_update) == True:
                            Update_data(index_to_update, kolom_to_update, input_new_DOMISILI)
                            return
                        else:
                            continue

                elif kolom_to_update == 'NAME':
                    while True:
                        input_new_NAME = input(f'Masukkan {input_kolom_change} baru: ').title()

                        if Input_checker(input_new_NAME, kolom_to_update) == True:
                            Update_data(index_to_update, kolom_to_update, input_new_NAME.strip())
                            return
                        else:
                            continue

                elif kolom_to_update == 'GENDER':
                    while True:
                        input_new_GENDER = input(f'Masukkan {input_kolom_change} baru: ').upper().strip()

                        if Input_checker(input_new_GENDER, kolom_to_update) == True:
                            Update_data(index_to_update, kolom_to_update, input_new_GENDER)
                            return
                        else:
                            continue

                elif kolom_to_update == 'DEPARTMENT':
                    while True:
                        Show_list_dept()

                        input_new_DEPARTMENT = input(f'Masukkan {input_kolom_change} baru: ').title().strip()

                        if Input_checker(input_new_DEPARTMENT, kolom_to_update) == True:
                            Update_data(index_to_update, kolom_to_update, input_new_DEPARTMENT)
                            return
                        else:
                            continue

                elif input_kolom_change == 'EMPLOYEE ID':
                    print('\n+++++++++++++++++++++++++++++++')
                    print('Tidak bisa mengubah EMPLOYEE ID')
                    print('+++++++++++++++++++++++++++++++\n')

                    return
            
            elif input_konfirmasi_change_data == 'N':
                return
            else:
                print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print('Maaf input anda salah. tolong input Y untuk melanjutkan dan N untuk membatalkan')
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

#==============================================================================================
def Change_ID(DOMISILI, NAME, GENDER, DEPARTMENT, ID):
    DEPARTMENT_initial = ''.join([word[0].upper() for word in DEPARTMENT.split()])

    gender = GENDER
    kode_domisili = ''.join([word[0].upper() for word in DOMISILI.split()])     
    panjang_nama = len(NAME.strip())

    id_generator = f'{DEPARTMENT_initial}{gender}{kode_domisili}{panjang_nama}'

    for index, id in enumerate(employee):                               
        if id_generator == employee[index]['EMPLOYEE ID']:
            panjang_nama += 1
            id_generator = f'{DEPARTMENT_initial}{gender}{kode_domisili}{panjang_nama}'

    employee[ID]['EMPLOYEE ID'] = id_generator
    return id_generator
            
#==============================================================================================
def ID_generator_menu3(index_ID, kolom, input_change):

    if kolom == 'DOMISILI':
        return Change_ID(DOMISILI= input_change, NAME= employee[index_ID]['NAME'], GENDER= employee[index_ID]['GENDER'], DEPARTMENT= employee[index_ID]['DEPARTMENT'], ID= index_ID)

    elif kolom == 'NAME':
        return Change_ID(DOMISILI= employee[index_ID]['DOMISILI'], NAME= input_change, GENDER= employee[index_ID]['GENDER'], DEPARTMENT= employee[index_ID]['DEPARTMENT'], ID= index_ID)

    elif kolom == 'GENDER':
        return Change_ID(DOMISILI= employee[index_ID]['DOMISILI'], NAME= employee[index_ID]['NAME'], GENDER= input_change, DEPARTMENT= employee[index_ID]['DEPARTMENT'], ID= index_ID)

    elif kolom == 'DEPARTMENT':
        return Change_ID(DOMISILI= employee[index_ID]['DOMISILI'], NAME= employee[index_ID]['NAME'], GENDER= employee[index_ID]['GENDER'], DEPARTMENT= input_change, ID= index_ID)

#==============================================================================================
def Update_data(index_change, kolom_change, updated):   # updated = input user
    while True:
        input_konfirmasi_update_data = input(f"Apakah anda yakin ingin mengganti data pada ID {employee[index_change]['EMPLOYEE ID']} ? [Y/N]: ").upper().strip()
        if input_konfirmasi_update_data == 'Y':
            employee[index_change][kolom_change] = updated

            header = list(employee[0].keys())
            print('===============================================================================================')
            print("{:^85}".format('Updated Data'))
            print('===============================================================================================')
            print(f'{header[0]:<12}| {header[1]:<20}| {header[2]:<30}| {header[3]:<7}| {header[4]:<17}|')
            print('-----------------------------------------------------------------------------------------------')
            print(f"{ID_generator_menu3(index_change, kolom_change, updated):<12}| {employee[index_change]['DOMISILI']:<20}| {employee[index_change]['NAME']:<30}| {employee[index_change]['GENDER']:<7}| {employee[index_change]['DEPARTMENT']:<17}|")
            print('===============================================================================================')
            print('\nData berhasil diupdate\n')
            break
       
        elif input_konfirmasi_update_data == 'N':
            print('\nData batal diupdate\n')
            break

        else:
            print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('Maaf input anda salah. tolong input Y untuk konfirmasi dan N untuk membatalkan')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

#==============================================================================================
def Sub_menu_4():       # Menghapus Data Employee
    print('-----------------------------')
    print("{:^30}".format('Menghapus Data Employee'))
    print('-----------------------------')
    print('1. Hapus Data Employee')
    print('2. Kembali ke Main Menu')
    print('-----------------------------')
    input_sub_menu_4 = input('Silahkan pilih Sub Menu [1-2]: ').strip()
    print()
    return input_sub_menu_4

#==============================================================================================
def Hapus_data():
    input_id_delete = input('Masukkan EMPLOYEE ID: ').upper().strip()   # Digunakan sebagai kondisi untuk loop di bawah

    id_delete_cheker = False
    for index, person in enumerate(employee):
        if input_id_delete == employee[index]['EMPLOYEE ID']:
            index_to_delete = index
            id_delete_cheker = True

    if id_delete_cheker == False:
        print('\n++++++++++++++++++++++++++++++++++++++')
        print(f'Tidak ada Employee dengan ID : {input_id_delete}')
        print('++++++++++++++++++++++++++++++++++++++\n')
        return

    header = list(employee[0].keys())
    print('===============================================================================================')
    print("{:^85}".format('Delete Data'))
    print('===============================================================================================')
    print(f'{header[0]:<12}| {header[1]:<20}| {header[2]:<30}| {header[3]:<7}| {header[4]:<17}|')
    print('-----------------------------------------------------------------------------------------------')
    print(f"{employee[index_to_delete]['EMPLOYEE ID']:<12}| {employee[index_to_delete]['DOMISILI']:<20}| {employee[index_to_delete]['NAME']:<30}| {employee[index_to_delete]['GENDER']:<7}| {employee[index_to_delete]['DEPARTMENT']:<17}|")
    print('===============================================================================================')

    while True:
        input_konfirmasi_delete_data = input(f"Apakah anda yakin ingin menghapus data dengan ID {employee[0]['EMPLOYEE ID']} ? [Y/N]: ").upper().strip()
        if input_konfirmasi_delete_data == 'Y':
            employee.pop(index_to_delete)
            print('\nData berhasil dihapus\n')
            break

        elif input_konfirmasi_delete_data == 'N':
            print('\nData batal dihapus\n')
            break
        
        else:
            print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('Maaf input anda salah. tolong input Y untuk konfirmasi dan N untuk membatalkan')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
            continue

#==============================================================================================
#----------------------------------------------------------------------------------------------
#==============================================================================================
def Main_flow():
    while True:
        main_menu_input = Call_main_menu()
        if main_menu_input == '1':      # Menu Data Employee / Menu Read
            while True:
                sub_menu_1_input = Sub_menu_1() 
                if sub_menu_1_input == '1':     # Menampilkan seluruh data
                    Show_all_data()
                elif sub_menu_1_input == '2':   # Menampilkan data tertentu
                    Show_specific_data()
                    SM11_Cari_ID_Lain()
                elif sub_menu_1_input == '3':   # Kembali ke Main Menu
                    break
                else:
                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                    print(f'Maaf menu {sub_menu_1_input} tidak ada. Masukkan angka [1-3]')
                    print('+++++++++++++++++++++++++++++++++++++++++++++\n')

        elif main_menu_input == '2':    # Menu Menambahkan data employee / Menu Create
            while True:
                sub_menu_2_input = Sub_menu_2() 
                if sub_menu_2_input == '1':     # Tambah data employee
                    Input_data_employee()

                elif sub_menu_2_input == '2':   # Kembali ke Main Menu
                    break
                else:
                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                    print(f'Maaf menu {sub_menu_2_input} tidak ada. Masukkan angka [1-2]')
                    print('+++++++++++++++++++++++++++++++++++++++++++++\n')

        elif main_menu_input == '3':    # Menu mengubah data employee / Menu Update
            while True:
                sub_menu_3_input = Sub_menu_3()
                if sub_menu_3_input == '1':     # Ubah data employee
                    Input_data_to_change()
                elif sub_menu_3_input == '2':   # Kembali ke Main Menu
                    break
                else:
                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                    print(f'Maaf menu {sub_menu_3_input} tidak ada. Masukkan angka [1-2]')
                    print('+++++++++++++++++++++++++++++++++++++++++++++\n')

        elif main_menu_input == '4':    # Menu menghapus data employee / Menu Delete
            while True:
                sub_menu_4_input = Sub_menu_4()
                if sub_menu_4_input == '1':     # Hapus data employee
                    Hapus_data()
                elif sub_menu_4_input == '2':   # Kembali ke Main Menu
                    break
                else:
                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                    print(f'Maaf menu {sub_menu_4_input} tidak ada. Masukkan angka [1-2]')
                    print('+++++++++++++++++++++++++++++++++++++++++++++\n')
                    
        elif main_menu_input == '5':    
            exit()
        else:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(f'Maaf menu {main_menu_input} tidak ada.\nMasukkan angka antara 1 sampai 5 untuk memilih menu')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

employee = [
    {'EMPLOYEE ID': 'FMJ7', 'DOMISILI': 'Jakarta', 'NAME': 'Andrian', 'GENDER': 'M', 'DEPARTMENT': 'Finance'},
    {'EMPLOYEE ID': 'SMJ7', 'DOMISILI': 'Jakarta', 'NAME': 'Marcell', 'GENDER': 'M', 'DEPARTMENT': 'Sales'},
    {'EMPLOYEE ID': 'HRFJ7', 'DOMISILI': 'Jakarta', 'NAME': 'Dianita', 'GENDER': 'F', 'DEPARTMENT': 'Human Resource'},
    {'EMPLOYEE ID': 'PMJ6', 'DOMISILI': 'Jakarta', 'NAME': 'Hendri', 'GENDER': 'M', 'DEPARTMENT': 'Production'},
    {'EMPLOYEE ID': 'PMJ7', 'DOMISILI': 'Jakarta', 'NAME': 'Bambang', 'GENDER': 'M', 'DEPARTMENT': 'Production'}
]

DEPARTMENT = ['Human Resource', 'Finance', 'Marketing', 'Sales', 'Production', 'Customer Service']

def Show_list_dept():
    print('{:^83}'.format('\n------------------=============== List of Department ===============------------------'))
    print('| {:^12} | {:^9} | {:^11} | {:^7} | {:^10} | {:^12} |'.format(DEPARTMENT[0], DEPARTMENT[1], DEPARTMENT[2], DEPARTMENT[3], DEPARTMENT[4], DEPARTMENT[5]))
    print()

Main_flow()