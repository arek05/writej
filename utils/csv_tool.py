import csv

class SaveDataToFile:
    def __init__(self):
        pass

    def save_user_data_to_file(self, name, surname, email, password):
        with open('tests/newdata.csv', 'a+', newline='') as file:
            fieldnames = ['imie', 'nazwisko', 'email', 'haslo']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'imie':name, 'nazwisko':surname, 'email':email, 'haslo':password})

    def read_user_data(self):
        with open('tests/newdata.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_email = f'{row['email']}'
                user_password = f'{row['haslo']}'
                mylist = [user_email, user_password]
                return mylist
