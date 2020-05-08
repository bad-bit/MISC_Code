# CTF - Houseplant 
# Year - 2020
# Category - Reverse Engineering
# Author - badbit
# Twitter - badbit0



import base64
import codecs

def main():

	key = "nyameowpurrpurrnyanyapurrpurrnyanya"
	key_decoded = codecs.decode(key, "rot-13")

	print(key_decoded)

	result = "'=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR"
	unwow = (result)[::-1]
	un_d = codecs.decode(unwow, "rot-13")
	print("This is un_d  "+un_d)
	un_c = str(un_d)
	un_c = base64.b64decode(un_c, altchars=None)
	print(un_c)
	
	result_final = un_c.decode()
	print(result_final)

	a = zip(key_decoded, result_final)

	for i, j in a:
		
		xord = ord(i) ^ ord(j)
		print(chr(xord), end= "")


if __name__ == '__main__':
	main()

