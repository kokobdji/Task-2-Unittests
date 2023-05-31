class Error(Exception):
    pass


def reverse_str(text: str) -> str:
    if not isinstance(text, str):
        raise Error('Give me str please')
    row = text.split(' ')
    reversed_list = []
    for word in row:
        list_ = [el for el in word if el.isalpha()]
        result = [list_.pop() if el.isalpha() else el for el in word]
        reversed_list.append(''.join(result))
    return ' '.join(reversed_list)


def array_diff(a, b):
    c = []
    for num in a:
        if not num in b:
           c.append(num)
    print(c)


array_diff([1,2,2], [1])
