#-------------------------------------------------------------------------------
# Name:    test_continue_break_examples.py
#
# Purpose: Test continue_break_examples module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import continue_break_examples as cbe
reload(cbe)

def main():
    """main()"""
    test_continue_break_example()
    test_reformat_text()
    test_reformat_text2()
    test_strip_python_comments ()

def test_continue_break_example():
    print "\ntest_continue_break_example()"
    max_loop_value = 4
    continue_value = 2
    break_value = 5
    cbe.continue_break_example(max_loop_value, continue_value, break_value)

def test_reformat_text():
    print '\ntest_reformat_text()'
    expected = 'abc'
    text = 'a-b-c-d'
    max_dash_count = 3
    actual = cbe.reformat_text(text, max_dash_count)
    compare_expected_and_actual(expected, actual, text, max_dash_count)

def test_reformat_text2():#    print '\ntest_reformat_text()'
    text = 'a-b-c-d-e-f-g-h-i-j-k-l'
    max_dash_count = 7
    actual = cbe.reformat_text(text, max_dash_count)
    compare_expected_and_actual(expected, actual, text, max_dash_count)

def compare_expected_and_actual(expected, actual, *args):
    print 'args are (text, max_dash_count)'
    if expected == actual:
        print 'PASSED:  For args =', args
    else:
        fmt = 'FAILED: For args = {}\nExpected: {}\nActual:   {}'
        print fmt.format(args, expected, actual)

def test_strip_python_comments():
    expected = '3'
    python_statement = 6#
    actual =cbe.strip_python_comments (python_statement)
    compare_expected_and_actual (expected, actual, python_statement)

if __name__ == '__main__':
    main()
