#-------------------------------------------------------------------------------
# Name:      Exercise 1
#
# Author:    David Viljoen
#
# Date:      13-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

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

import running_totals
reload(running_totals)

def main():
    """main()"""
    test_running_total()
    strange_sum_function()

def test_running_total():
    expected = 6
    iterations = 3
    actual = running_totals.running_total(iterations)
    compare_expected_and_actual(iterations, expected, actual)

def strange_sum_function():
    expected = 6.4166
    arg = 4
    actual = running_totals.strange_sum_function(arg)
    compare_expected_and_actual(arg, expected, actual)

def test_compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()