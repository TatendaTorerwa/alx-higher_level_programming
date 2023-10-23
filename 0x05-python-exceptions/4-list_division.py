#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i] if i < len(my_list_1) else 0
            element2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check for non-integer or non-float elements
            if not isinstance(element1, (int, float)) or not isinstance(element2, (int, float)):
                print("wrong type")
                result.append(0)
            elif element2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(element1 / element2)
        except IndexError:
            print("out of range")
            result.append(0)
        except Exception as e:
            print("An unexpected error occurred:", e)
            result.append(0)
        finally:
            continue

    return result
