import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  cipher_text = ""
  for i in range(len(text)):
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if text[i] in alphabet:
      index = alphabet.index(text[i])
      if direction == "encode":
        cipher_text += alphabet[index+shift]
      else:
        cipher_text += alphabet[index-shift]
    else:
      cipher_text += text[i]

  print(f"The {direction}d text is {cipher_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 25
  caesar(text, shift, direction)
  decision = input("Type 'Yes' if you want to go again. Otherwise type no\n").lower()
  if decision == "no":
    break