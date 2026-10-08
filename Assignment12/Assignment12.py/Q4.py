str=input('enter a string:')

first_char=str[0]
last_char=str[-1]
middle_chars=str[1:-1]

new_str=last_char+middle_chars+first_char

print(f"string after exchanging first and last character:{new_str}")