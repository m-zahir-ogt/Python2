# implementation Cesar Encryption

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



geld =500
mostafa = 167
Glep = 166
olga = 166

restgeld = geld %3 #in this case it is 2
teilbareGeld = geld - restgeld  #in this case  498
mostaf = teilbareGeld/3
print("mostafa tasche:" +str(mostafa))


cites = ["köln", "Düseldorf", "Berlin", "paris", "Turin"]

#this function do encryption
def encrypt()->str:
    klarText = input("\nplease enter Text to be encrypted:")
    key = input("please enter encryption Key:")
    return "it is encrypted from  " + klarText + "and Key:" + key
 
def decode()->str:
    cypherText = input("\nplease enter Text to be DECRYPTED!!:")
    key = input("please enter DECRYPTION KEY!!:")
    return "it is DECRYPTED  from  " + cypherText + "and Key:" + key
 
 
def main():
    result =""
    print("hello , i am cesar enc and dec app!")
    userChoice = input("if you want decrypt press d oder encrypt press e:")
 
    if(userChoice == "e"):
        result = encrypt()
    elif userChoice == "d":
        result = decode()
    else:
        result = "you must enter only e or d"
 
    print(result)
 
if __name__ == "__main__":
    main()


