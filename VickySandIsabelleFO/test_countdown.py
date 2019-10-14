#-------------------------------------------------------------------------------
# Name:    test_example.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import countdown
reload(countdown)

def main():
    """main()"""
    test_get_countdown_using_for()
    test_get_countdown_using_while()

def test_get_countdown_using_for():
    print "test_get_countdown_using_for"
    expected = '10 9 8 7 6 5 4 3 2 1 0'
    start_value = 10
    actual = countdown.get_countdown_as_text_using_for(start_value)
    compare_expected_and_actual('', expected, actual)

    expected = '3 2 1 0'
    start_value = 3
    actual = countdown.get_countdown_as_text_using_for(start_value)
    compare_expected_and_actual(start_value, expected, actual)

def test_get_countdown_using_while():
    print "\ntest_get_countdown_using_while"
    expected = '10 9 8 7 6 5 4 3 2 1 0'
    start_value = 10
    actual = countdown.get_countdown_as_text_using_while(start_value)
    compare_expected_and_actual('', expected, actual)

    expected = '3 2 1 0'
    start_value = 3
    actual = countdown.get_countdown_as_text_using_while(start_value)
    compare_expected_and_actual(start_value, expected, actual)


def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
