import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host="KennethLinehan132.mysql.pythonanywhere-services.com",
        user="KennethLinehan13",
        password="datareppass",
        database="KennethLinehan13$data-representation-project",
        charset="utf8mb4"
    )

    # Set the cursor class after creating the connection
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    return conn, cursor
