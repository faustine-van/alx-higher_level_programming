#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """fct : function execute function safely
       *args: any parameters are used to pass any arguments or keyword
       arguments that need to be passed to the function.
    """
    try:
        return fct(*args)
    except Exception as e:
        messageError = "Exception: " + str(e)
        print(messageError, file=sys.stderr)
        return None
