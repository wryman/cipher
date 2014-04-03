#  File: Cipher.py

#  Description:  Use a transposition cipher to encode/decode input

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
if option =='E' or option=='e':
	infile=open('input.txt','r')
	file_content=infile.read()
	infile.close()
	for i in range (0,len(file_content),2):
		even_str+=file_content[i]
		odd_str+=file_content[i+1]
	encrypted_str=odd_str+even_str
	outfile=open('output.txt','w')
	outfile.write(encrypted_str)
	outfile.close()
elif option=='D' or option=='d':
	infile=open('input.txt','r')
	file_content=infile.read()
	infile.close()
	for i in range(0,len(file_content),2):
		decrypted+=file_content[len(even)]
	print (decrypted)
else:
	print('Wrong input. Bye.')
outfile=open('output.txt','r')
outcontent=outfile.read()
outfile.close
print(outcontent)