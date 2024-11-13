# https://python.plainenglish.io/five-python-wrappers-that-can-reduce-your-code-by-half-af775feb1d5

import time as t
import sys

def check_imported_versions(caller_globals):
    # Get all imported modules from the caller's global namespace
    for name, module in caller_globals.items():
        # Only check for module objects
        if isinstance(module, type(sys)):
            # Check for both __version__ and version attributes
            version = getattr(module, '__version__', None) or getattr(module, 'version', None)
            if version:
                print(f"{name} (module: {module.__name__}) Version: {version}")
            else:
                print(f"{name} (module: {module.__name__}) does not have a version attribute.")


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = t.time()
        result = func(*args, **kwargs)
        end_time = t.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds...")
        return result
    return wrapper

def sep() -> None:
    return print('----------------------------------------------------------------------------------------------------------------')