from support import *
import time as t

print("**** A PYTHON BASED APP ****\n"+" *** BY Mohd Sufiyan Ansari\n"+"  ** Feedbacks are valuable\n"+"   * Enter Any Name (Containing Only English Alphabets and Spaces) and See The Turtle Drawing That Letter")
val=0

while(val!=1):
	val=1
	str_py=input("Enter A Name : ").upper()
	for i in str_py:
		if(ord(i)<65 or ord(i)>90) and ord(i)!=32:
			val=0
	if val==0:
		print('\nPlease Enter A Valid Name')

ff=int(input("Enter Font Size:\n 1 for 120\n 2 for 60\n 3 for 40\n"))
while(ff not in range(1,4)):
	ff=int(input("\nPlease Choose Correct Options.\nEnter Font Size:\n 1 for 120\n 2 for 60\n 3 for 40\n"))
	
pensize_var=int(input("Input pen thickness (2-6):"))
while(pensize_var not in range(2,7)):
	pensize_var=int(input("\nPlease Enter Between 2 and 6\nInput pen thickness (2-6):"))
	
print('Maximise The New Window')

name(pensize_var,ff)
l=0
for i in range(len(str_py)):
	if (i%(11*ff)==0 and i>0):
		l=l+1
	tab(120*(i%(11*ff))/ff-700,200+120-120/ff-(l*200)/ff)
	if i==0:
		t.sleep(1)
	if str_py[i]==' ':
		continue
	eval(str_py[i]+'()')   	
t.sleep(2)
