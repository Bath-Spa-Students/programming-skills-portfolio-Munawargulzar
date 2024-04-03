def make_shirt (size= 'large', message= 'I love python'):
    """ summarize the shirt that was made"""
    print("\nI made a " + size + "t-shirt")
    print('It printed "'+ message + '"on the front')

    make_shirt()
    make_shirt(size='large')
    make_shirt('medium', 'python is cool')