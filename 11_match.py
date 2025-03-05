# MATCH STATEMENT

http_status = 200

if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status == 501:
    print("Server Error")
else:
    print("Unknown")

"""
A match statement compares a value to several different conditions until one is met.
"""

match http_status:
    case 200 | 201: # or operator
        print("Success")
    case 400:
        print("Bad request")
    case 500 | 501:
        print("Server Error")
    case _: # default
        print("Unknown")
    
# Combining
# You can combine several conditions by using the or operator in the conditional statement.
'''
    case 200 | 201: 
'''

# The default is essentially the final outcome if nothing is found in the case checks it's 
# the equivalent to the else in the if blocks
'''
    case _:
        print("Unknown")
'''
