import mysql.connector


def get_cursor():
    db = mysql.connector.connect(
        user=str(),
        password=str(),
        database=str(),
        host=str()
    )
    return [db.cursor(), db]
