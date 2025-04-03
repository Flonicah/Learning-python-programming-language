#building a basic translatoer in python
# define a translat function in girraffe language

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            # checking if it is upper or lower case
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
                
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))
