import random
import getpass
from ftp import FTP
import get_cursor

abs_correct = []
alm_correct = []
wrong = []


def check_answer(user_input: str, correct: str):
	# Possible Input Ways of the user
	corrects = [correct,
				correct.lower(),
				correct.upper(),
				correct.capitalize(),
				correct.replace(", ", "/"),
				correct.replace("/", ","),
				correct.replace(" (ugs.)", "")]

	user_inputs = [user_input, user_input.lower(), user_input.upper(), user_input.capitalize(), user_input.replace(", ", "/"), user_input.replace("/", ",")]
	if (_user_input_ in corrects for _user_input_ in user_inputs) and user_input != "" and len(user_input) > len(correct) - 4:
		if user_inputs != correct:
			alm_correct.append(user_input)
			print(f"""Fast richtig!
Deine Antwort: {user_input}
Richtige Antwort: {correct}""")
			print()
		else:
			abs_correct.append(user_input)
			print("Korrekt!")
			print()
	else:
		wrong.append(user_input)
		print("Falsch!")
		print("Korrekte Antwort: " + correct)
		print()


def run():
	sess = FTP()
	print("Bitte wählen Sie eine Option!")
	print("1. Vokabeln lernen")
	print("2. Vokabeln testen")
	print("3. Vokabeln hinzufügen")
	print("4. Vokabeln löschen")
	mode = ""
	try:
		mode = int(input("(Bitte nur Zahlen eingeben) Wahl > "))
	except ValueError:
		print("Bitte nur Zahlen eingeben!")
		exit()
	voci_file = open("Voci.txt", "r", encoding="utf-8")
	lines = voci_file.readlines()
	langs = ["Deutsch", "Französisch"]
	if mode == 2:
		for line in lines:
			language = random.choice(langs)
			woerter = line.split(" - ")
			if language == "Deutsch":
				answer = input(f"Übersetze das Wort {woerter[1]} in die Sprache Französisch > ")
				check_answer(answer, woerter[0])
			else:
				answer = input(f"Übersetze das Wort '{woerter[0]}' in die Sprache Deutsch > ")
				check_answer(answer, woerter[1])
	elif mode == 1:
		counter = 0
		for line in lines:
			counter += 1
			woerter = line.split(" - ")
			if counter >= 100:
				print(f"{counter}. {woerter[1]}	 {woerter[0]}\n")
			else:
				print(f"{counter}.	{woerter[1]}	{woerter[0]}\n")

	elif mode == 3:
		choice = input("Datei importieren oder ein neues erstellen? (i/n) > ")
		if choice == "i":
			file = input("Dateispeicherort > ")
			sess.login()
			langs = input("Welche Sprachen sind in der Datei enthalten? (z.B. Deutsch, Französisch, Englisch) > ")
			sess.upload(file, langs)
			sess.logout()
		elif choice == "n":
			file = input("Dateispeicherort > ")
			langs = input("Welche Sprachen sind in der Datei enthalten? (z.B. Deutsch, Französisch, Englisch) > ")
			sess.login()
			with open(file, 'a', encoding="utf-8") as f:
				while True:
					voci_1 = input("Wort auf der Sprache 1 > ")
					voci_2 = input("Wort auf der Sprache 2 > ")
					if voci_1 == "exit" or voci_2 == "exit":
						sess.upload(file, langs)
						break
					else:
						f.write(f"{voci_1} - {voci_2}\n")
						continue
			sess.logout()
	voci_file.close()


# Function to create a new User Account
def create_user(cursor, db):
	username = input("Enter your desired username: ")
	first_name = input("Enter your first name: ")
	last_name = input("Enter your last name: ")
	password = input("Enter your password (Please make it strong?): ")
	cursor.execute()
	db.commit()
	return "Successfully created a new User Account! :3"


# Function to log in
def login(username, password, cursor):
	cursor.execute()
	data = cursor.fetchone()
	if data is None:
		return False
	else:
		return True


# Main method
def main():
	vals = get_cursor.get_cursor()
	cursor = vals[0]
	db = vals[1]
	choice_1 = input("Wollen Sie sich anmelden oder registrieren? (l/s) ")
	if choice_1 == "l":
		username = input("Nutzername: ")
		password = getpass.getpass(prompt="Passwort: ")
		auth = login(username, password, cursor)
		if auth:
			print("Erfolgreich angemeldet! :3")
			run()
		else:
			print("Falscher Benutzername oder Passwort!")
			exit()
	elif choice_1 == "s":
		create_user(cursor, db)
	else:
		print("Invalid Input!")
		exit()


if __name__ == '__main__':
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("Das Programm wurde beendet. Auf Wiedersehen!")
	except Exception as error:
		print(f"Ein Fehler ist aufgetreten: {error}")
