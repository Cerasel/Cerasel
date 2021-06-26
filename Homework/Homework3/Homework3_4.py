# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    r1, r2 = text.split(' ', maxsplit=1)
    r2 = r2
    r1 = r1.upper()
    r2r = ''
    for letter in r2:
        if letter.islower():
            r2r += letter
        else :
           r2r =''
    return(r1,r2)
    # <your code here>


print(process_text('1234567a Text to te5t'))