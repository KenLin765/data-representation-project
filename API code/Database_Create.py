import json
import mysql.connector

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name_common VARCHAR(255),
            region VARCHAR(255),
            subregion VARCHAR(255),
            population INT,
            currencies_name VARCHAR(255),
            languages JSON,
            unMember BOOLEAN,
            capital VARCHAR(255),
            car_signs JSON,
            car_side VARCHAR(255)
        )
    ''')

def insert_data(cursor, data):
    for entry in data:
        currencies = entry.get('currencies')
        currencies_name = currencies.get('AUD').get('name') if currencies and currencies.get('AUD') else None

        cursor.execute('''
            INSERT INTO countries (
                name_common, region, subregion, population, currencies_name, languages,
                unMember, capital, car_signs, car_side
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            entry.get('name').get('common'),
            entry.get('region'),
            entry.get('subregion'),
            entry.get('population'),
            currencies_name,
            json.dumps(entry.get('languages')),
            entry.get('unMember'),
            entry.get('capital')[0] if entry.get('capital') else None,
            json.dumps(entry.get('car').get('signs')),
            entry.get('car').get('side')
        ))


def main():
    # Connect to MySQL database (modify the parameters accordingly)
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='countries'
    )
    cursor = conn.cursor()

    # Create table
    create_table(cursor)

    # Load JSON data
    with open('countries.json', 'r', encoding='utf-8') as json_file:
        countries_data = json.load(json_file)

    # Insert data into the database
    insert_data(cursor, countries_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
