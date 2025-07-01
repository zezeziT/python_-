#
def shout(text):
    return text.upper() + '!!!'

def whisper(text):
    return text.lower() + '...'


if __name__ == '__main__':
    a='Hello ze'
    b = shout(a)  # return 返回值会赋给b  但是本身a不会变
    print(a)
    print(b)

