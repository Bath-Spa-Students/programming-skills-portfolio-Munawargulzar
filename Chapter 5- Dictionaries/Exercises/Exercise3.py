glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    # Add the following five terms to the glossary
    'for loop': 'A way to repeatedly execute a block of code while iterating over a sequence of items.',
    'function': 'A block of code that can be called and executed multiple times with different inputs.',
    'return': 'A statement that ends the execution of a function and specifies the value to be returned to the caller.',
    'scope': 'The region of a program in which a variable can be accessed.',
    'module': 'A file containing Python definitions and statements.'
}

# Print each term and its definition
for term, definition in glossary.items():
    print(f"\n{term.title()}: {definition}")