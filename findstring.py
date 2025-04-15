import re

def ispresent(person):
    names = ['John', 'Jane', 'Doe']
    return person in names

def nodigit(person):
    return not person.isdigit()

def not_empty(person):
    return len(person) > 0

def no_special_chars(person):
    return bool(re.fullmatch(r'[A-Za-z]+', person))