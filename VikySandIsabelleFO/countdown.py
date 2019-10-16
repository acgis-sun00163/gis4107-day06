#-------------------------------------------------------------------------------
# Name:    countdown.py
#
# Author:    David Viljoen
#
# Date:      13-10-2019
#
# CreatedBy: Isabelle and Chengjiaqi Sun
#-------------------------------------------------------------------------------

def get_countdown_as_text_using_for(start_value):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0
    """
    string = ''
    start_value = range (start_value, -1, -1)
    for number in start_value:
        string += str(number) + ' '
    return string[:-1]



def get_countdown_as_text_using_while(start_value):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0
    """
    string = str(start_value) + ' '
    while start_value > 0:
        start_value = start_value -1
        string += str(start_value) + ' '
    return string [:-1]

? 2019 GitHub, Inc.