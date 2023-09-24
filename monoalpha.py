monoalphabetic_dict = {
    "a": "c",
    "b": "d",
    "c": "e",
    "d": "f",
    "e": "g",
    "f": "h",
    "g": "i",
    "h": "j",
    "i": "k",
    "j": "l",
    "k": "m",
    "l": "n",
    "m": "o",
    "n": "p",
    "o": "q",
    "p": "r",
    "q": "s",
    "r": "t",
    "s": "u",
    "t": "v",
    "u": "w",
    "v": "x",
    "w": "y",
    "x": "z",
    "y": "a",
    "z": "b"
}

def m_alpha_cip(plaintext):
    cipher = ""
    for letter in plaintext:
        cipher += monoalphabetic_dict[letter]
    print("ciphertext: ",cipher)
    
message = str(input("Enter plaintext: "))
m_alpha_cip(message)