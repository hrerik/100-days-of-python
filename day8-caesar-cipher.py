alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

playing = True # While true will keep playing the game

def within_range(index): # Function that stops error "Index out of range" when calling "alphabet.index()"
    while index >= 26:
        index -= 26
    while index < 0:
        index += 26
    return index

def caesar(_direction, _text, _shift):
    
    printed_text = ""
    _shift = within_range(_shift) # Eliminates unnecessary computations

    if _direction == "encode":
        for letter in _text:
            if letter in alphabet:
                i = within_range(alphabet.index(letter) + _shift)
                printed_text += alphabet[i]
            else:
                printed_text += letter
        print(printed_text)
        
    elif _direction == "decode":
        for letter in _text:
            if letter in alphabet:
                i = within_range(alphabet.index(letter) - _shift)
                printed_text += alphabet[i]
            else:
                printed_text += letter
        print(printed_text)
        
    else:
        print("Invalid operation.")
        
while playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(direction, text, shift)
    
    # Checks for user's answer to keep playing
    inp = input('Would you like to try again? Type "yes" to continue:\n')
    if inp.lower() != "yes":
        playing = False
