import sqlite3

def add_data(account_number, fio, address, ipu_info, comments):
    conn = sqlite3.connect('ves_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ves_data (account_number, fio, address, ipu_info, comments)
        VALUES (?, ?, ?, ?, ?)
    ''', (account_number, fio, address, ipu_info, comments))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_data('12345', 'Иванов Иван', 'ул. Примерная 1', 'ИПУ_Инфо_1', 'Комментарий к данным 1')
    add_data('67890', 'Петров Петр', 'ул. Тестовая 2', 'ИПУ_Инфо_2', 'Комментарий к данным 2')
