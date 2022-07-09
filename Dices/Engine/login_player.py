def player(line):
    while True:
        try:

            current_line = input(line).upper()
            if not current_line.isalpha() or len(current_line) < 3:
                raise ValueError
            break

        except ValueError:
            print(
'''PLEASE ENTER A VALID NAME:
Username may only contain uppercase and lowercase letters
and may have 3 or more letters.
''')

    return current_line