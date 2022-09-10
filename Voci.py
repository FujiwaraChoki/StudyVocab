import random

mode = input("Enter Test mode? (y/n): ")
vociFile = open("Voci.txt", "r", encoding="utf-8")
lines = vociFile.readlines()
langs = ["Deutsch", "Französisch"]


def check_answer(answer, correct):
	if answer in correct and answer != "" and len(answer) > len(correct) - 4:
		print()
		print("Korrekt!")
		print()
	else:
		print()
		print("Falsch!")
		print("Korrekte Antwort: " + correct)
		print()


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
	for line in lines:
		woerter = line.split(" - ")
		print(f"""
	{woerter[0]}
	{woerter[1]}""")

	vociFile.close()
