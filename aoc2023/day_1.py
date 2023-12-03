def main():
    str_digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five" : 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    sum_of_digits = 0
    
    with open('input_1.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        print(line)
        
        # -----------------------------

        # find a first digit in the line (from left to right)
        found_first_digit_idx_ = None
        for idx, digit in enumerate(line):
            if digit.isdigit():
                found_first_digit_idx_ = idx
                break

        # find a first digit, where the digit is a word (from left to right)
        found_first_digit_idx = None
        len_of_found_first_digit = 0
        for i in range(len(line)):
            tmp_s_1st = ""
            for j in range(i, len(line)):
                tmp_s_1st += line[j]
                if tmp_s_1st in str_digit_map:
                    found_first_digit_idx = i
                    len_of_found_first_digit = len(tmp_s_1st)
                    break
            if found_first_digit_idx is not None:
                break

        left_to_right_found_value = None
        if found_first_digit_idx_ is not None and found_first_digit_idx is not None:
            if found_first_digit_idx_ < found_first_digit_idx:
                left_to_right_found_value = line[found_first_digit_idx_]
            elif found_first_digit_idx < found_first_digit_idx_:
                left_to_right_found_value = line[slice(found_first_digit_idx, found_first_digit_idx + len_of_found_first_digit)]
                left_to_right_found_value = str_digit_map[left_to_right_found_value]
        elif found_first_digit_idx_ is not None and found_first_digit_idx is None:
            left_to_right_found_value = line[found_first_digit_idx_]
        elif found_first_digit_idx_ is None and found_first_digit_idx is not None:
            left_to_right_found_value = line[slice(found_first_digit_idx, found_first_digit_idx + len_of_found_first_digit)]
            left_to_right_found_value = str_digit_map[left_to_right_found_value]

        # -----------------------------

        found_last_digit_idx_ = None
        for idx, digit in enumerate(reversed(line)):
            if digit.isdigit():
                found_last_digit_idx_ = idx
                break

        found_last_digit_idx = None
        len_of_found_last_digit = 0
        for i in range(len(line)):
            tmp_s_2nd = ""
            for j in range(i, len(line)):
                tmp_s_2nd += line[::-1][j]
                if tmp_s_2nd[::-1] in str_digit_map:
                    found_last_digit_idx = i
                    len_of_found_last_digit = len(tmp_s_2nd)
                    break
            if found_last_digit_idx is not None:
                break

        right_to_left_found_value = None
        if found_last_digit_idx_ is not None and found_last_digit_idx is not None:
            if found_last_digit_idx_ < found_last_digit_idx:
                right_to_left_found_value = line[::-1][found_last_digit_idx_]
            elif found_last_digit_idx < found_last_digit_idx_:
                right_to_left_found_value = line[::-1][slice(found_last_digit_idx, found_last_digit_idx + len_of_found_last_digit)]
                right_to_left_found_value = str_digit_map[right_to_left_found_value[::-1]]
        elif found_last_digit_idx_ is not None and found_last_digit_idx is None:
            right_to_left_found_value = line[::-1][found_last_digit_idx_]
        elif found_last_digit_idx_ is None and found_last_digit_idx is not None:
            right_to_left_found_value = line[::-1][slice(found_last_digit_idx, found_last_digit_idx + len_of_found_last_digit)]
            right_to_left_found_value = str_digit_map[right_to_left_found_value[::-1]]

        print(">>", left_to_right_found_value, right_to_left_found_value)
        sum_of_digits += int(f"{left_to_right_found_value}{right_to_left_found_value}")
        print(">>", sum_of_digits)

        print("======================")
    return sum_of_digits


if __name__ == '__main__':
    main()
