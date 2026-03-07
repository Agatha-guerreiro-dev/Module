from useful.string import edit
from useful.data import validation
import os
import csv

options = ['view registered people','register new people', 'exit the system']
finish = len(options)
while True:
    edit.menumaker('Main menu',30,*options)
    menu = validation.readint('Your option: ')
    if menu == finish:
        print('\033[32mThank you!\n'
              'Until next time ;)\033[m')
        break
    if menu == 2:
        edit.headline('New Register',28)
        file_exists = os.path.isfile('register.csv') and os.path.getsize('register.csv') > 0

        with open('register.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            p_name = validation.readstr('Name: ')
            p_age = validation.readint('Age: ')
            writer.writerow({'name': p_name, 'age': p_age})
        print(f'\033[32m{p_name} registered successfully!\033[m')
    if menu == 1:
        edit.headline('Registered People', 22)
        with open('register.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f'{row["name"]:<27}{row["age"]:>3} years')
    else:
        print('\033[31m Invalid Option\033[m')
