#Input: 150 5
#putput: 10010110 227 10011000 231 10011010


alphabet = "150 5"
l=[]
k = alphabet.split()
# print(bin(7)[2:])
# print(oct(6)[2:])
j=int(k[0])
for i in range(int(k[1])):
  if i%2==0:
    print(bin(j)[2:],end=" ")
 
  else:
    print(oct(j)[2:],end=" ")
  j=j+1
