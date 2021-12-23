import random
import string

while True:
    text=str(input("enter a text="))

    def split(text):
        return [char for char in text]

    a= split(text)

    alphabet= list(string.ascii_lowercase)

    x1 = random.choice(alphabet)
    x2 = random.choice(alphabet)
    x3 = random.choice(alphabet)
    x4 = random.choice(alphabet)


    a.pop(0)
    a.insert(0,x1)
    a.pop(1)
    a.insert(1,x2)
    a.pop(2)
    a.insert(2,x3)
    a.pop(3)
    a.insert(3,x4)

    def listToString(a): 
        
        str1 = " "  
        return (str1.join(a))
            
    print("Encoded= {}".format(listToString(a)))



     


