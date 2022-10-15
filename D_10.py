import pyjokes


def tell_some_jokes():
    return pyjokes.get_joke()


print(tell_some_jokes())
