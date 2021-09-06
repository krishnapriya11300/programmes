




 # list of numbers
biggest= [1, 2, 3, 4]
  
  
# printing the maximum element
print("Largest element is:", max(biggest))


 


# list of numbers
biggest2= [1, 2, 3, 4]


mx=max(biggest2[0],biggest2[1])
secondmax=min(biggest2[0],biggest2[1])
n =len(biggest2)
for i in range(2,n):
    if biggest2[i]>mx:
        secondmax=mx
        mx=biggest2[i]
    elif biggest2[i]>secondmax and \
        mx != biggest2[i]:
        secondmax=biggest2[i]
 #printing the maximum element
print("Largest number is:", max(biggest2))


print("Second Largest number is : ",\
      str(secondmax))





def biggestn(list1, N):
    final_list = []
  
    for i in range(0, N): 
        max1 = 0
          
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j];
                  
        list1.remove(max1);
        final_list.append(max1)
          
    print(final_list)
# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
  
# Calling the function
biggestn(list1, N)










import string
  
alphabet = set(string.ascii_lowercase)
  
def pangram(string):
    return set(string.lower()) >= alphabet
      
string = "The quick brown fox jumps over the lazy dog"
if(pangram(string) == True):
    print("True")
else:
    print("False")







def countCurrency(amount):
     
    notes = [2000, 500, 200, 100,
               50, 20, 10, 5, 1]
                
    noteCounter = [0, 0, 0, 0, 0,
                     0, 0, 0, 0]
     
    print ("Currency Count -> ")
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i ," : ", j)
 
# Driver code
amount = 868
countCurrency(amount)




fname = input("Enter file name: ")
try:
   fh = open(fname)
except:
    print(' file is extremely large so it cannot be read:error')
    quit()
    
text=fh.read()
res=text.upper()
print(res.rstrip())

