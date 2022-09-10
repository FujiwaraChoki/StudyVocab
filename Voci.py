import random

mode = input("Enter Test mode? (y/n): ")
voci_file = open("Voci.txt", "r", encoding="utf-8")
lines = voci_file.readlines()
langs = ["Deutsch", "Französisch"]
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


# Main method
def main():
	if mode == "y":
		for line in lines:
			language = random.choice(langs)
			woerter = line.split(" - ")
			wort = ""
			if language == "Deutsch":
				answer = input(f"Übersetze das Wort {woerter[1]} in die Sprache Französisch: ")
				check_answer(answer, woerter[0])
			else:
				answer = input(f"Übersetze das Wort '{woerter[0]}' in die Sprache Deutsch: ")
				check_answer(answer, woerter[1])
	else:
		counter = 0
		for line in lines:
			counter += 1
			woerter = line.split(" - ")
			if counter >= 100:
				print(f"{counter}. {woerter[1]}	 {woerter[0]}\n")
			else:
				print(f"{counter}.	{woerter[1]}	{woerter[0]}\n")

	vociFile.close()


if __name__ == '__main__':
	try:
		while True:
			main()
	except KeyboardInterrupt:
		print("Das Programm wurde beendet. Auf Wiedersehen!")
