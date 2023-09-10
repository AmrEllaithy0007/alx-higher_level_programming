#!/usr/bin/python3
def print_Reversed_list_integer(my_list=[]):
    if my_list:
        for item in my_list[::-1]:
            print("{:d}".format(item))
