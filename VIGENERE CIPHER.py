# NIce Question Given On Facebook group by TA-Mr.NITISH MITTAL
"""
HTML-CSS Love - Practice Question
This practice question has been created by Nitish Mittal (Teaching Assistant) for course MITx 6.00.1x Summer 2015 on edX.
This is in reference to week 6 course material.
Hello Python Lovers,

Here we are back with a very interesting problem for you. This is very related to Week 6 Problem Set 
and it is essential that you cover Week 6 Material before attempting this interesting problem. 
You all must attempt this to have a very clear approach towards algorithms and their implementation. 

You have implemented Caesar Cipher for Week 6. Here you have to implement Vigenere Cipher,
an improved Cipher. Essential information regarding Vigenere Cipher is given at the end of this text below. 
Just for the basic information, it uses a string as a key instead of the integer value for the purpose of encryption. 
So here’s the problem statement in which you have to use Vigenere Cipher.
(a-z are considered to be indexed from 0-25 for the key)

HTML and CSS are in deep love. Caveat! There’s always a villain in the story.
PHP also loves CSS and doesn’t want HTML and CSS to be together. PHP always tries to intrude in their private space and 
read their messages. HTML and CSS go to their mutual friend Python and ask for help. 
Python being the smartest, writes a class named “PHPGoAway” for its friends. 
It explains them its working. It says that this class can be called by either of them by sending a message “Python Buddy” only
as an argument to the object being created. Once the object is created, the string key can be set by using the method “setKey”
with the key as the argument. Both of them will use this object with the help of their friend Python.

Whenever any one of them wishes to send a message, it needs to call a method “forLove” of the class with 
the message string as the argument. This method returns back the encrypted message. Whenever any one of them receives a message
eeds to call a method “fromLove” of the class with the encrypted message string as the argument. 
This method returns back the decrypted message. Remember that the key was set initially itself.
So this key will be used for both the purposes. The key can also be changed later by calling “setKey” function again. 
Python warned HTML and CSS to use only lower space ascii characters for the message and also not to use any punctuations. 
However the spaces remain intact.

Help Python in writing code for its friends HTML and CSS. This might sound difficult at the first sight, 
but please read about Vigenere Cipher and this problem thoroughly. Please provide the code for the class along with all
the methods as described above in the form below.

For typical values, consider this scenario. Suppose the key used is ‘yophp’. 
HTML sends the message “i love you” to CSS. Provide the encrypted result of the method “forLove” for this message. 
This is R1. For the same object with the same key, consider sometime HTML received a message from CSS 
which was “rvt mtczxuvq ogl bshjha”. Provide the actual message sent by calling the method “fromLove” for this encrypted
message. This is R2.
We hope you enjoy this! Also please don’t forget to provide your feedback :)

Good Luck!

Nitish Mittal
Teaching Assistant


VIGENERE CIPHER
(Source: Wikipedia)

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, 
in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. 
The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square, or Vigenère table. 
It consists of the alphabet written out 26 times in different rows, each alphabet shifted cyclically to the left compared 
to the previous alphabet, corresponding to the 26 possible Caesar ciphers. At different points in the encryption process, 
the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.

For example, suppose that the plaintext to be encrypted is:

ATTACKATDAWN
The person sending the message chooses a keyword and repeats it until it matches the length of the plaintext, 
for example, the keyword "LEMON":

LEMONLEMONLE
Each row starts with a key letter. The remainder of the row holds the letters A to Z (in shifted order). 
Although there are 26 key rows shown, you will only use as many keys (different alphabets) as there are unique 
letters in the key string, here just 5 keys, {L, E, M, O, N}. For successive letters of the message, we are going to 
take successive letters of the key string, and encipher each message letter using its corresponding key row. 
Choose the next letter of the key, go along that row to find the column heading that matches the message character; 
the letter at the intersection of [key-row, msg-col] is the enciphered letter.

For example, the first letter of the plaintext, A, is paired with L, the first letter of the key. 
So use row L and column A of the Vigenère square, namely L. Similarly, for the second letter of the plaintext, 
the second letter of the key is used; the letter at row E and column T is X. The rest of the plaintext is enciphered in 
a similar fashion:

Plaintext:	ATTACKATDAWN
Key:	LEMONLEMONLE
Ciphertext:	LXFOPVEFRNHR
Decryption is performed by going to the row in the table corresponding to the key,
finding the position of the ciphertext letter in this row, and then using the column's label as the plaintext.
For example, in row L (from LEMON), the ciphertext L appears in column A, which is the first plaintext letter. 
Next we go to row E (from LEMON), locate the ciphertext X which is found in column T, thus T is the second plaintext letter.

"""




#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     HTML-CSS LOve Vingere Cipher Using Class
#
# Author:      harsh
#
# Created:     23/07/2015
# Copyright:   (c) harsh 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------




class PHPGoAway(object):
   def __init__(self,message ):
      self.message = message
      if self.message != "Python Buddy":
        raise AttributeError("This object has no attributes to this Class")

   def setKey(self,key):
    self.key = key
    return key

   def ForLove(self,text):
    self.text = text
    key = self.key.lower()

    def shift(letter):
     har1 = buildCoder1()
     return har1[letter]

    def applyCoder(letter, coder):
     return coder[letter]

    def buildCoder(s):
     har = {}
     import string
     sum = 0
     for x in string.lowercase:
        if ord(x) <  ord('z')- s+1 :
            har[x] = chr(ord(x) + s)
        else:
            har[x] =  chr(ord('a') + sum)
            sum = sum +1
     return har

    def buildCoder1():
     har = {}
     import string
     sum = 0
     for x in string.lowercase:
        har[x] = sum
        sum = sum +1
     return har


    def applycoderall(text,key):
     import string
     text = text.lower()
     a = len(text)/len(key)
     if len(text) % len(key) != 0:
        test = (key*(a+1))[:len(text)]
     else:
        test = key*a
     a1 = ''
     b = 0
     for x in range(len(text)):
      a = x
      if text[x] in string.lowercase:
        a1 = a1 + applyCoder(text[a],buildCoder(shift(test[b])))
        b = b +1
      else:
        a1 = a1 + text[a]
     return  a1.upper()
    return applycoderall(text,key)

   def FromLove(self,text):
    self.text = text
    text1 = text.replace(" ",'')
    key = self.key.lower()

    def applyCoder(letter, coder):
     return coder[letter]

    def buildCoder1():
     har = {}
     import string
     sum = 0
     for x in string.lowercase:
        har[x] = sum
        sum = sum +1
     return har


    def shift(letter):
     har1 = buildCoder1()
     return har1[letter]


    def buildCoder(s):
     har = {}
     import string
     sum = 0
     for x in string.lowercase:
        if ord(x) <  ord('z')- s+1 :
            har[x] = chr(ord(x) + s)
        else:
            har[x] =  chr(ord('a') + sum)
            sum = sum +1
     return har

    def applycoderallD(text,key):
     import string
     text = text.lower()
     a = len(text)/len(key)
     if len(text) % len(key) != 0:
        test = (key*(a+1))[:len(text)]
     else:
        test = key*a
     a1 = ''
     b = 0
     for x in range(len(text)):
      a = x
      if text[x] in string.lowercase:
        a1 = a1 + applyCoder(text[a],buildCoder(26-shift(test[b])))
        b = b +1
      else:
        a1 = a1 + text[a]
     return a1.upper()
    return applycoderallD(text,key)


pythonBuddy = PHPGoAway("Python Buddy")
pythonBuddy.setKey("yophp")
print pythonBuddy.ForLove("I Love you")  #R1
print pythonBuddy.FromLove("rvt mtczxuvq ogl bshjha") #R2









