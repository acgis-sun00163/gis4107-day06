#-------------------------------------------------------------------------------
# Name:    continue_break_examples.py
#
# Author:    David Viljoen
#
# Date:      13-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

def main():
    """main()"""

def continue_break_example(max_loop_value, continue_value, break_value):
    """Demonstrate continue and break in for loop
    """
    for i in range(max_loop_value + 1):
        if i == continue_value: continue
        if i == break_value: break
        print i
    else:
        print "No break"

def reformat_text(text, max_dash_count):
    """Given text that contains dashes, ignore dashes up to max_dash_count
    and return all text up to max_dash_count.  The returned text does not
    include the dashes.  For example, given text = 'a-b-c', and
    max_dash_count of 1, the function would return 'a'  If text contains
    no dashes, text will be returned.
    """


    i= max_dash_count
    n = text.replace ('-','')
    return n[:i]


def strip_python_comments (python_statement):
    strippable = python_statement.strip('#')
    if strippable == '':
        return None
    else:
        return strippable

