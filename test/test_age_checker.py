from lib.age_checker import *
from datetime import datetime
import pytest
# '''
# Checks if a correct format
# returns True
# '''
# def test_check_format_correct():
#     result = is_old_enough("1990-01-01")
#     assert result == True

# '''
# Checks if an incorrect format
# returns False
# '''
# def test_check_format_incorrect():
#     result = is_old_enough("199001-01")
#     assert result == False

# '''
# Checks if an empty string
# returns False
# '''
# def test_check_format_empty():
#     result = is_old_enough("")
#     assert result == False

# 
'''
Given a person is younger
than 16 (10) return denied 
message
'''
def test_person_younger_than_16():
    result = is_old_enough("2008-04-26")
    assert result == "You are not over 16, access denied."
'''
Given a person is older
than 16 (10) return granted 
message
'''

def test_person_older_than_16():
    result = is_old_enough("2008-04-25")
    assert result == "You are over 16, access granted."
