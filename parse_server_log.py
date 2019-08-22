import os
import re
import base64

def main():

	stripped = []
	#count = 0

	file = open('server_log.txt', 'r')
	log = file.read()


	reg = re.findall(r'QVND.*HTTP/', log)
	#print(reg)

	for i in reg:
		
		stripped.append(i.strip("%3D HTTP/"))
		#stripped.append(i.strip("%3D"))
		#print(stripped)

	for x in stripped:
		
		#print(type(x))
		#print(x)
		print(base64.b64decode(x + '=' * (-len(x) % 4)))
		print("\n")
		print("-------------------")
		print("\n")
		#count = count + 1

	#print(count)


	#print(decoded)



if __name__ == '__main__':
	main()
