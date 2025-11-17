from string import ascii_lowercase as alphabet, ascii_uppercase as alphabet2    

def caesar_cryptage(sentence:str, offset:int=1) -> str:
    final_caesar = " "
    for character in sentence :
        if character in alphabet:
            step_one = (ord(character) - ord('a') + offset) % 26 + ord('a')
            step_two = chr(step_one)
            final_caesar += step_two
        elif character in alphabet2:
            step_one = (ord(character) - ord('A') + offset) % 26 + ord('A')
            step_two = chr(step_one)
            final_caesar += step_two
        else:
            final_caesar += character
    print(final_caesar)

def caesar_decryptage(sentence:str, offset:int=1) -> str:
    final_caesar = " "
    for character in sentence :
        if character in alphabet or character in alphabet2:
            if character in alphabet: 
                step_one = (ord(character) - ord('a') - offset) % 26 + ord('a')
                step_two = chr(step_one)
                final_caesar += step_two
            elif character in alphabet2:
                step_one = (ord(character) - ord('A') - offset) % 26 + ord('A')
                step_two = chr(step_one)
                final_caesar += step_two
            else:
                final_caesar += character
    print(final_caesar)

caesar_cryptage('Je suis en cours Python a l\'EPSI', 8)
caesar_decryptage('TXAZCELYE', 1)