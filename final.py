def binario_a_cadena(b):
    binary_values = b.split()
    ascii_characters = [chr(int(binary, 2)) for binary in binary_values]
    return ''.join(ascii_characters)
