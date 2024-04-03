def make_shirt(size, message):
    """Summarize the shirt that was made"""
    print(f"\nI made a {size}t-shirt.")
    print(f'It printed "{message}" on the front.')

    make_shirt ('medium', 'Hello world')
    make_shirt (message= 'I am nice girl', size = 'small')
