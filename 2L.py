def Cadena_a_binario(s):
    return ' '.join(format(ord(char), '08b') for char in s)