def greetings(name):
    """
    Returns a simple greting message, given your name.
    """
    message = "Hi there! -- " + name
    return message


if __name__ == '__main__':
    name = "Clare"
    print(greetings(name))
