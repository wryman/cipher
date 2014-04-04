#  File: Cipher.py

#  Description:  Use a transposition cipher to encode/decode input.txt

#  Student Name:  William Ryman

#  Student UT EID:  wrr368

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created:4/3/14

#  Date Last Modified:4/3/14


option=input("Do you want to encrypt or decrypt? (E/D):")
even_str=''
odd_str=''
encrypted_str=''
decrypted=''
#Having problems with even lengthed strings
if option =='E' or option=='e':
	infile=open('input.txt','r')
	file_content=infile.read()
	infile.close()
	for i in range (0,len(file_content),2):
		encrypted_str=odd_str+even_str
	outfile=open('output.txt','w')
	outfile.write(encrypted_str)
	outfile.close()
	print(encrypted_str)

elif option=='D' or option=='d':
	infile=open('input.txt','r')
	file_content=infile.read()
	infile.close()
	for i in range(0,len(file_content)//2,1):
			even_str+=file_content[len(file_content)//2+i]
			odd_str+=file_content[i]
			decrypted+=even_str[i]+odd_str[i]
	print(decrypted)

else:
	print('Wrong input. Bye.')
outfile=open('output.txt','r')
outcontent=outfile.read()
outfile.close()