from unidecode import unidecode
char1 = '罗'
char2 = '发'
char3 = '富'
ascii_code = unidecode(char1 + char2 + char3)
print(ascii_code)