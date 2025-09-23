from morse_mapping import morse_code_mapping

reverse_morse_code_mapping = {v: k for k, v in morse_code_mapping.items()}

print(
    "The length of a dot(.) is 1 unit.\n"
    "A dash(-) is 3 units.\n"
    "The space between pats of the same letter is 1 unit.\n"
    "The space between letters is 3 units which is represented here by |.\n"
    "The space between words is 7 units which is represented here by \\.\n"
)


def main():
    q = input("Code or decode?: ")
    entry = input("Enter Your text here: ")

    if q.lower() == 'code':
        print(convert_to_code(entry))
    elif q.lower() == 'decode':
        print(convert_to_text(entry))
    else:
        print("Invalid response")


def convert_to_code(word):
    morse_code = ''
    for letter in word.upper():
        try:
            morse_code += f"{morse_code_mapping[letter]}|"
            # where | is the 3 unit space between letters
        except KeyError:
            if letter != ' ':
                morse_code += f"{letter.lower()}|"
            else:
                morse_code += "\\"  # for 7 unit spaces in between words
    return morse_code


def convert_to_text(morse_code):
    code_char = ''
    plain_text = ''
    if not morse_code:
        return ""
    if "|" not in morse_code and "\\" not in morse_code:
        try:
            return reverse_morse_code_mapping[morse_code]
        except KeyError:
            return "Invalid Morse code"
    else:
        position_of_pipe, position_of_slash = check_for(morse_code, "|"), check_for(morse_code, "\\")
        if position_of_pipe is not None and position_of_slash is not None:
            slice_pos = min(position_of_slash, position_of_pipe)
        elif position_of_pipe is None:
            slice_pos = position_of_slash
        elif position_of_slash is None:
            slice_pos = position_of_pipe
        else:
            slice_pos = None
        try:
            if slice_pos == position_of_slash:
                plain_text += f"{convert_to_text(morse_code[:slice_pos])} "
            else:
                plain_text += f"{convert_to_text(morse_code[:slice_pos])}"
            morse_code = morse_code[(slice_pos+1):]
            plain_text += convert_to_text(morse_code)
        except IndexError:
            return

    return plain_text.lower()

def check_for(string, char):
    try:
        index_of_character = string.index(char)
        return index_of_character
    except ValueError:
        return None


# .--|.|\.-..|---|...-|.|\.....|
# print(convert_to_text(".--|.|\.-..|---|...-|.|\.....|"))
# print(f"'{text}' in morse code is {convert_to_code(text)}")

if __name__ == "__main__":
    main()
