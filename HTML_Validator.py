#!/bin/python3
import re


def validate_html(html):
    '''
    This function performs a limited version of
    html validation by checking whether every
    opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to
    # generate a list of html tags without any extra text;
    # then process these html tags using the
    # balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from
    # class will be that you will have to keep track of not just
    # the 3 types of parentheses,
    # but arbitrary text located between the html tags
    if html == '':
        return True
    text = _extract_tags(html)
    print(text)
    if len(text) == 0:
        return False
    checked = []
    for i, char in enumerate(text):
        if list(char)[1] != "/":
            checked.append(char)
        else:
            if len(checked) == 0:
                return False
            print(list(checked[-1])[1:])
            print(list(char)[2:])
            if list(checked[-1])[1:] == list(char)[2:]:
                checked.pop()
            else:
                return False
    return len(checked) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly by the user are prefixed
    with an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    x = re.findall("<([^\s>]+)",  html)
    return list(map((lambda word: "<" + word + ">"), x))
