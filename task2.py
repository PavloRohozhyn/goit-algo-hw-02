from collections import deque

def palindrome(data):
    """ processor """

    # do lowercase
    data = ''.join(data.lower().split())
    # add data to enqueu (doble)
    char_deque = deque(data)
    # check chars
    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False
    return True


def main():
    """ Main funciton """
    # text
    texts = [
        'data',
        'datad',
        'dataData',
        'dataDataD'
    ]
    for t in texts:
        print(palindrome(t))

if __name__ == "__main__":
    main()
