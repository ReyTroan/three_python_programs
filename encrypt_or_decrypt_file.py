from pyAesCrypt import encryptFile, decryptFile


def Crypt():
    enc_dec = input('Зашифровать или Расшифровать файл? (З/Р): ')
    if enc_dec == 'З':
        file_name = input('Введите имя файла для зашифровки: ')
        password = input('Введите пароль для файла: ')
        try:
            encryptFile(f'{file_name}', f'{file_name}.aes', password)
            print('Файл успешно зашифрован!')
        except:
            print('Введен несуществующий файл')
            Crypt()
    elif enc_dec == 'Р':
        file_name = input('Введите имя файла для расшифровки: ')
        password = input('Введите пароль для файла: ')
        try:
            decryptFile(f'{file_name}', 'outfile.txt', password)
            print('Файл успешно расшифрован!')
        except:
            print('Введен неверный файл или пароль')
            Crypt()
    else:
        print('Неверный ввод.')
        Crypt()
Crypt()

