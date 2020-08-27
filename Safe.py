from random import randint

password = ""

def set_password():
	pasw = randint(0, 9999)

	for i in range(0, 4 - len(str(pasw))):
		pasw = "0" + str(pasw)

	return str(pasw)

def main():
	global password
	password = str(set_password())

	if enter_password() == True:
		print("Поздравляю, у тебя получилось взломать программу! Ты крутой праграммист!")
		while True:
			pass

def enter_password():
	while True:
		inp = str(input("Введите пароль: "))
		if inp == password:
			return True

main()