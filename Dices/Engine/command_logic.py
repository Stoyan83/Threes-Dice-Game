def command(line):
    while True:
        try:

            current_line = input(line).upper().strip()
            if current_line != "R" and current_line != "D" and current_line != "ROLL" and current_line != "DONE":
                raise ValueError
            break

        except ValueError:
            print("Invalid command please try again")

    return current_line


def remove_smallest(numbers):
    new_nums = []
    if len(numbers) == 0:
        return numbers
    if 3 in numbers:
        for number in numbers[:len(numbers)]:
            if number == 3:
                numbers.remove(number)
                new_nums.append(number)
                break
    else:
        for number in numbers[:len(numbers)]:
            if number == min(numbers):
                numbers.remove(number)
                new_nums.append(number)
                break
    return numbers, new_nums