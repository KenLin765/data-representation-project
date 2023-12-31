from flask import Flask, render_template, request, redirect, url_for, jsonify
from db_connection import get_db_connection

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/example')
def example():
    # Display information about Croatia
    conn, cursor = get_db_connection()
    cursor.execute('SELECT * FROM countries WHERE name_common = %s', ('Croatia',))
    country_data = cursor.fetchone()
    conn.close()

    return render_template('create.html', example_data=country_data)

@app.route('/get_country_by_name', methods=['GET'])
def get_country_by_name():
    conn, cursor = get_db_connection()
    country_name = request.args.get('name')
    cursor.execute('SELECT * FROM countries WHERE name_common = %s', (country_name,))
    country_data = cursor.fetchone()
    conn.close()

    return jsonify(country_data)

# Route to add country using AJAX
@app.route('/add_country', methods=['POST'])
def add_country():
    try:
        conn, cursor = get_db_connection()
        data = request.form.to_dict()

        cursor.execute('''
            INSERT INTO countries 
            (name_common, region, subregion, population, currencies_name, languages, unMember, capital, car_signs, car_side)
            VALUES (%(name_common)s, %(region)s, %(subregion)s, %(population)s, %(currencies_name)s, %(languages)s, 
                    %(unMember)s, %(capital)s, %(car_signs)s, %(car_side)s)
        ''', data)
        conn.commit()
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
    
@app.route('/get_countries_by_name', methods=['GET'])
def get_countries_by_name():
    conn, cursor = get_db_connection()
    partial_name = request.args.get('name')
    cursor.execute('SELECT * FROM countries WHERE name_common LIKE %s', ('%' + partial_name + '%',))
    countries_data = cursor.fetchall()
    conn.close()

    return jsonify(countries_data)

# Route to handle the update operation
@app.route('/update', methods=['POST'])
def update_country():
    try:
        conn, cursor = get_db_connection()
        data = request.form.to_dict()

        cursor.execute('''
            UPDATE countries SET
            region=%(region)s, subregion=%(subregion)s, population=%(population)s, 
            currencies_name=%(currencies_name)s, languages=%(languages)s, 
            unMember=%(unMember)s, capital=%(capital)s, car_signs=%(car_signs)s, car_side=%(car_side)s
            WHERE name_common=%(name_common)s
        ''', data)
        conn.commit()
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
    
@app.route('/get_all_countries', methods=['GET'])
def get_all_countries():
    conn, cursor = get_db_connection()
    cursor.execute('SELECT name_common FROM countries ORDER BY name_common ASC')
    countries = cursor.fetchall()
    conn.close()

    return jsonify(countries)

# Route to delete country by name using AJAX
@app.route('/delete_by_name', methods=['POST'])
def delete_by_name():
    try:
        conn, cursor = get_db_connection()
        country_name = request.form['name_common']

        cursor.execute('DELETE FROM countries WHERE name_common = %s', (country_name,))
        conn.commit()
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
