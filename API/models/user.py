def login(mysql, username, password):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username LIKE %s AND password LIKE %s AND type LIKE %s", (username, password, 'manager'))
    # row = cursor.fetchall()
    # mysql.connection.commit()
    row = cursor.fetchone()
    if row is not None:
        result = {'is_valid': True, 'message': 'Username and Password is valid'}
    else:
        result = {'is_valid': False, 'message': 'Username or Password is invalid'}
    cursor.close()
    return result

