import random
import time
import string

def gen():

	length = input("How many characters would you like your password to be(6-10)")

	a = random.choice(string.ascii_lowercase)
	b = random.choice(string.ascii_lowercase)
	c = random.choice(string.ascii_lowercase)
	d = random.choice(string.ascii_lowercase)
	e = random.choice(string.ascii_lowercase)
	f = random.choice(string.ascii_lowercase)
	g = random.choice(string.ascii_lowercase)
	h = random.choice(string.ascii_lowercase)
	i = random.choice(string.ascii_lowercase)
	j = random.choice(string.ascii_uppercase)
	k = random.randint(1,9)
	l = random.randint(1,9)
	m = random.randint(1,9)
	n = random.choice(string.ascii_uppercase)

	a2 = str(a)
	b2 = str(b)
	c2 = str(c)
	d2 = str(d)
	e2 = str(e)
	f2 = str(f)
	g2 = str(g)
	h2 = str(h)
	i2 = str(i)
	j2 = str(j)
	k2 = str(k)
	l2 = str(l)
	m2 = str(m)
	n2 = str(n)

	print("Generating...")
	time.sleep(random.randint(1,3))


	if length == " 6":
		print("Your password is " + j2 + a2 + b2 + c2 + k2 + l2)

	if length == " 7":
		print("Your password is " + j2 + a2 + b2 + c2 + k2 + l2 + e2)

	if length == " 8":
		print("Your password is " + j2 + a2 + b2 + c2 + k2 + l2 + e2 + i2)

	if length == " 9":
		print("Your password is " + j2 + a2 + b2 + c2 + k2 + l2 + e2 + i2 + m2)

	if length == " 10":
		print("Your password is " + j2 + a2 + b2 + c2 + k2 + l2 + e2 + i2 + m2 + n2)

	again = input("Want to generate another password?")

	if again in [" Yes", " yes", " Y", " y"]:
		gen()
	else:
		print("Ok come back soon")

yesNo = input("Type yes to generate a password")

if yesNo in [" Yes", " yes", " Y", " y"]:
	print("Perfect")
else:
	print("Ok come back soon")
	exit()

password = input("Please enter the password you were given")

if password in [" Hackz1", " hackz1"]:
	print("Password accepted")
	gen()
else:
	print("Password denied")
	exit();
