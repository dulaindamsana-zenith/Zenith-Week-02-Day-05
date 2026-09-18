import random as encryptor

def aes_encrypt(value):
        letters = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        symbols = [
                '+', '-', '*', '/', '//', '%', '**',
                '=', '+=', '-=', '*=', '/=',
                '==', '!=', '>', '<', '>=', '<=',
                '&', '|', '^', '~', '<<', '>>',
                '(', ')', '[', ']', '{', '}',
                ',', ':', '.', ';', '@', '->',
        ]

        all_chars = letters + [str(num) for num in numbers] + symbols

        result = ""

        for aes_generator in range(len(str(value))):
                result += encryptor.choice(all_chars)

        return result

def rsa_encrypt(value):
    prime_p = 89
    prime_q = 82

    modulus_n = prime_p * prime_q
    totient_phi = (prime_p - 1) * (prime_q - 1)

    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    public_exponent_e = 2
    while public_exponent_e < totient_phi:
        if find_gcd(public_exponent_e, totient_phi) == 1:
            break
        public_exponent_e += 1

    if isinstance(value, str):
        encrypted_blocks = []
        for character in value:
            character_as_number = ord(character)
            encrypted_character = pow(character_as_number, public_exponent_e, modulus_n)
            encrypted_blocks.append(str(encrypted_character))
        return "-".join(encrypted_blocks)
        
    else:
        return pow(value, public_exponent_e, modulus_n)

def utf_8_encrypt(text):
    byte_array = text.encode('utf-8')
    bit_list = []

    for b in byte_array:
        binary_code = bin(b)[2:]
        while len(binary_code) < 8:
            binary_code = "0" + binary_code

        inverted_bits = ""
        for bit in binary_code:
            if bit == "0":
                inverted_bits += "1"
            else:
                inverted_bits += "0"
        bit_list.append(inverted_bits)
    return " ".join(bit_list)