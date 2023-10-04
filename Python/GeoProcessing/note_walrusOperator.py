# Allows us to combine expressions and assignments
# EXAMPLE 1:
if __name__ == '__main__':
    text = 'This is a very long sentence.'

    # Regular Way:
    # words = text.split()
    #info = {
    #    "words": words
    #}
    info = { 
        'words': (words := text.split()),
        'characters': (chars := len("".join(words))),
        'avg_char_per_word': round(chars / len(words), 2)
    }    
    
    print(info)
    
# EXAMPLE 2: use a variable if it exists
name = 'Mario'
empty_name = ''

# expression works if value on right of walrus is true
if temp_name := empty_name or name:
        print(temp_name)
        print('Executed')  