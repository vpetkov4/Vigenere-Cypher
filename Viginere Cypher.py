
"""The Vigenere cypher is a generalization
 of the Caesar cypher. It is based on a multiple letter keyword, while the
 Caesar cypher is based on a single letter keyword.
 The Vigenere cypher was created in the middle of the 16th century
 and remained unbroken until the middle of the 19th century.
 
 This file implements the Vigenere cypher as a class.
 It also defines a method to encrypt text from a file
 and to save the encrypted message into a file.
 Finally, it implements a simple interface that allows
 the user to choose to
 1): open a file and decrypt a message, 
 2): to encrypt their own message,
 3): to save the current thread into a file.

 You can open a text file containing multiple messages
 encrypted with different keys.
 
 To recognize a keyword it must be encoded by a string like
 Key: "keyword"
 The methods will clean the text from non alphabetic characters
 """

"""Define the Viginere class"""

class Vigenere(object):


    def __init__(self,plain_text="",key=""):
        self.plain_text=plain_text.upper()
        self.key=key.upper()
        self.key_len=len(key)
        self.text_len=len(plain_text)


    #The encryption method
    def encrypt(self):
        self.cryptext=""
        i=0
        
        while(i<self.text_len-self.text_len%self.key_len):
            for j in range(self.key_len):
                    char=(ord(self.plain_text[i])+ord(self.key[j]))%26
                    char+=ord('A')
                    self.cryptext+=chr(char)
                    i+=1  
        
        j=0
        
        while(i<self.text_len):
            char=(ord(self.plain_text[i])+ord(self.key[j]))%26
            char+=ord('A')
            self.cryptext+=chr(char)
            i+=1
            j+=1
            
        return self
    
    
    #The decryption method
    def decrypt(self):
        self.decryptext=""
        i=0
        
        while(i<self.text_len-self.text_len%self.key_len):
            for j in range(self.key_len):
                    char=(ord(self.cryptext[i])-ord(self.key[j])+26)%26
                    char+=ord('A')
                    self.decryptext+=chr(char)
                    i+=1
                    
        j=0
        
        while(i<self.text_len):
            char=(ord(self.cryptext[i])-ord(self.key[j])+26)%26
            char+=ord('A')
            self.decryptext+=chr(char)
            i+=1
            j+=1
            
        return self

"""Define a function that handles opening and writing to a file
"""

def viginere_from_file(filename):
    bad_char=[" ",",",".","'","!","?",":",";","\n",'"',
              "*", "&", "^", "%", "$", "#", "@", "~","/"]

    file=open(filename+".txt",'r')
    L=file.readlines()
    key=""
    
    #Create two lists with the encrypted and decrypted messages
    crypt_text_=[]
    decrypt_text_=[]
    for line in L:
        #Check if this line gives a key
        is_key=line[0:4]
        if is_key=="Key:":
            key=line[3:]
            for i in bad_char:
                key=key.replace(i,"")
            
            crypt_text_.append("\n")
            crypt_text_.append(line)
            
            
            decrypt_text_.append("\n")
            decrypt_text_.append(line)
            
            
        else:
            
            text=line
            
            
            for i in bad_char:
                text=text.replace(i,"")
            
            vig=Vigenere(text,key)
            vig.encrypt()
            vig.decrypt()
            
            crypt_text_.append(vig.cryptext)
            
            decrypt_text_.append(vig.decryptext)
            
            
            write_to_file(filename+"-crypt",crypt_text_,decrypt_text_)
            
    file.close()


"""Write in the new file function"""
def write_to_file(filename,crypt_text_,decrypt_text_):
    file2=open(filename+".txt",'w')
    file2.writelines("This is the encrypted text:\n\n")
            
    for cryp_text in crypt_text_:
        file2.writelines(cryp_text)
        file2.writelines("\n")
       
    file2.writelines("\n\n")
    file2.writelines("-"*100)
    
    file2.writelines("\n\nThis is the decrypted text:\n\n")
    for decrypt_text in decrypt_text_:
        file2.writelines(decrypt_text)
        file2.writelines("\n")
    file2.close()



bad_char=[" ",",",".","'","!","?",":",";","\n",'"',
          "*", "&", "^", "%", "$", "#", "@", "~","/"]

"""Create a live thread, if we want to safe it later in a file"""
crypt_text_=[]
decrypt_text_=[]


print("Would you like to open a file?:")
command=input("> ").lower()
if command=="yes":
    command= input("filename> ")
    viginere_from_file(command)


print("Would you like to encrypt a message?: ")
command=input("> ").lower()
while(command=="yes"):
    
    key=input("Key: ")
    text=input("Message: ")
            
    for i in bad_char:
        text=text.replace(i,"")
        key=key.replace(i,"")
                
    crypt_text_.append("\n")
    crypt_text_.append("Key: "+key.upper())
    
            
    decrypt_text_.append("\n")
    decrypt_text_.append("Key: "+key.upper())
    
    
    k=Vigenere(text,key)
    k.encrypt()
    k.decrypt()
    print(k.cryptext)
    print(k.decryptext)
    crypt_text_.append(k.cryptext)
    decrypt_text_.append(k.decryptext)
    
    print("Would you like to encrypt another message?: ")
    command=input("> ").lower()

if len(crypt_text_)>0:            
    print("Would you like to save the current thread into a file?:")
    
    command=input("> ").lower()
    if command=="yes":
        print("Please choose the filename:")
        filename=input("> ").lower()
        write_to_file(filename,crypt_text_,decrypt_text_)
                






"""
try:
    L=["Key: Tom\n", "Hello world!\n", "Try this at least once!\n"]
    
    test_source_file=open("Vigenere_source_test.txt","w")
    test_source_file.writelines(L)
    test_source_file.close()
except Exception as e:
    print("Test file is already created.",e)"""