## de oude substitute functie:
def old_substitute(string):
    result = ''
    for char in string:
        if char == 'A':
            char = 'T'
        elif char == 'T':
            char = 'A'
        elif char == 'G':
            char = 'C'
        elif char == 'C':
            char = 'G'
        result += char
    return result

# nieuwe functie:
def substitute(string, d):
    """Substitutes characters in a string based on a dictionary d"""
    result = ''
    for char in string:
         #print(f"key: {char}")
         #print(f"value {d[char]}")
         #if char in d:
         #    result = result + d[char]
         #else: result = result + '_'
         result = result + d.get(char, '_')
    return result

sub_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
original = 'AXGT&$#AGCGTCCTTAGTTACAGGATGGCXTTAT'
#expected = 'TCATCGCAGGAATCAATGTCCTACCGAATA'
result = substitute(string=original, d=sub_dict)
print(result)