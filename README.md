# Vigenere-Cypher
Implements the Vigenere Cypher from scratch

The Vigenere cypher is a generalization
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
