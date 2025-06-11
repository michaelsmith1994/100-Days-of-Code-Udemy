
import random

#Random will need a seed to prevent the characters from being scrambled every run. 
# To make this consistant but seucre I have decided to make the seed the same as the shift key. 
all_possible_Chars = list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58)) + list(range(32, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

def character_list_builder(shift):
    random.seed(shift)
    random.shuffle(all_possible_Chars)



def message_cipher(shift, text):
    character_list_builder(abs(int(shift)))
    shift = int(shift)
    message_list = list(text)

    for i, character in enumerate(message_list):
        ascii_val = ord(character)
        if ascii_val in all_possible_Chars:
            idx = all_possible_Chars.index(ascii_val)
            new_idx = (idx + shift) % len(all_possible_Chars)
            message_list[i] = chr(all_possible_Chars[new_idx])
        else:
            return("Character not found in table: "+ character)

    return ''.join(message_list)