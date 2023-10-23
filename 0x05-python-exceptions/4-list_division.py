#!/usr/bin/pytho3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for p in range(list_length):
        try:
            div = my_list_1[p] / my_list_2[p]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            n_list.append(div)
    return n_list
