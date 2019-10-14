#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     08-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    """main()"""

def running_total(iterations):
    """Return the sum of numbers from 1 to intertions inclusively
    """
    x = range (iterations, 0, -1)
    for number in x:
        integer = 1
        integer += number
    return sum(x)

def strange_sum_function (number):
    x = range (number, 0, -1)
    y = range (1, number+1, 1)

    list = []
    for z in range (number):
        w = float (x[z]) / float (y[z])
        list.append(w)
    return sum(list)






