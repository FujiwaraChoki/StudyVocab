import ftplib
import os
import get_cursor


class FTP:

    def __init__(self, host, username, password, db_username):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__session = None
        self.__db_username = db_username

    @property
    def host(self):
        return self.__host

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def session(self):
        return self.__session

    def login(self):
        self.__session = ftplib.FTP(self.__host, self.__username, self.__password)
        self.__session.encoding = "utf-8"

    def logout(self):
        self.session.quit()
        self.__session = None

    def upload(self, filepath, languages):
        self.session.cwd("domains/samihindi.com/public_html/VocabStud/VLists/")
        if os.system == "Windows":
            filepath = filepath.replace("/", "\\")
        filename = filepath[::-1].split('/', 1)[0][::-1]
        try:
            if os.path.isfile(filepath):
                byteR = open(filepath, 'rb')
                self.__session.storbinary(f'STOR {self.__db_username}/{filename}', byteR)
                byteR.close()
                print(f"'{filename}' wurde erfolgreich hochgeladen!")
                vals = get_cursor.get_cursor()
                cursor = vals[0]
                db = vals[1]
                # Getting the user_id through the username from table `user`
                cursor.execute()
                data = cursor.fetchone()
                user_id = data[0]
                cursor.execute()
                db.commit()
            else:
                print(f"'{filename}' existiert nicht!")
        except Exception as error:
            print(f"Ein Fehler ist aufgetreten: {error}")

    # Function to retrieve a file from the server
    def download(self, filename, destination):
        try:
            if os.path.isfile(destination):
                print(f"'{filename}' existiert bereits!")
            else:
                byteW = open(destination, 'wb')
                self.__session.retrbinary('RETR VocabStud/VLists/FujiwaraChoki/' + filename, byteW.write)
                byteW.close()
                print(f"'{filename}' wurde erfolgreich heruntergeladen!")
        except Exception as error:
            print(f"Ein Fehler ist aufgetreten: {error}")
