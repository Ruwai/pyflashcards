cards_python = """\
QUESTION
How could this code be improved?

>>> ls = [1,2,3]
>>> for i in range(ls):
>>>     print(i, ls[i])

ANSWER
>>> for i, item in enumerate(ls):
>>>     print(i, item)

TAGS
python, effective python


QUESTION
How could this code be improved?

>>> ls = [1,2,3]
>>> if len(ls) != 0:
>>>     do_something()

ANSWER
Empty strings and lists implicitly evaluate to False.

>>> if ls:
>>>     do_something()

TAGS
python, item 2, effective python


QUESTION
What's wrong here?

>>> ls = [[0] * 3] * 3
>>> print(ls)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> ls[0][1] = 2
>>> print(ls)
>>> [[0, 2, 0], [0, 2, 0], [0, 2, 0]]

ANSWER
Lists don't contain objects - they contain references to objects.

>>> ls_row = [0] * 3
>>> ls = [ls_row.copy() for _ in range(3)]
>>> ls[0][1] = 2
>>> print(ls)
[[0, 2, 0], [0, 0, 0], [0, 0, 0]]

TAGS
python, item 2, effective python
"""
