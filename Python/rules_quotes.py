# Single Quotes ' and Double Quotes ":
# Single quotes (') and double quotes (") are used interchangeably to define string literals.
# You can use one type of quote inside a string defined with the other type without any issues.'''
# For example:
single_quoted = 'This is a single-quoted string.'
double_quoted = "This is a double-quoted string."
mixed_quotes = "You can also use 'single quotes' or \"double quotes\" inside strings."

# Triple Single Quotes ''' and Triple Double Quotes """:
# You can use one type of triple quote inside a strng defined with the other type without any issues.
# For example:
multi_line = '''This is a multi-line
               string using triple single quotes.'''

another_multi_line = """This is a multi-line
                      string using triple double quotes."""

mixed_quotes = '''You can use "double quotes"
                 or 'single quotes' inside triple-quoted strings.'''

# Escaping Quotes Inside Strings:
# If you want to include the same type of quote inside a string that is used to define the string, you need to escape it using a backslash (\).
single_inside_double = "He said, \"Hello!\""
double_inside_single = 'She exclaimed, \'Wow!\''