from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Создаем базу данных и таблицу
conn = sqlite3.connect('ves_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ves_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number TEXT,
        fio TEXT,
        address TEXT,
        ipu_info TEXT,
        comments TEXT
    )
''')
conn.commit()
conn.close()

# Определение маршрутов
@app.route('/')
def index():
    # Чтение данных из базы данных
    conn = sqlite3.connect('ves_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ves_data')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Получение данных из базы данных для редактирования
    conn = sqlite3.connect('ves_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ves_data WHERE id = ?', (id,))
    data = cursor.fetchone()

    if request.method == 'POST':
        # Обновление данных в базе данных
        new_account_number = request.form['account_number']
        new_fio = request.form['fio']
        new_address = request.form['address']
        new_ipu_info = request.form['ipu_info']
        new_comments = request.form['comments']

        cursor.execute('''
            UPDATE ves_data 
            SET account_number = ?, fio = ?, address = ?, ipu_info = ?, comments = ? 
            WHERE id = ?
        ''', (new_account_number, new_fio, new_address, new_ipu_info, new_comments, id))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
