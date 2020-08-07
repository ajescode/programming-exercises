def solution(x):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    encrypt_key = dict(zip(alphabet, alphabet[::-1]))
    decrypted_string = ''

    for letter in x:
        if letter in alphabet:
            letter = encrypt_key.get(letter)
        decrypted_string += letter
    return decrypted_string
