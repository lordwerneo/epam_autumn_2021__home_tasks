"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`.
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    filtered_indexes, result = [], []
    for value in indexes:
        if filtered_indexes and isinstance(value, int) and value > filtered_indexes[-1]:
            filtered_indexes.append(value)
        elif not filtered_indexes and value > 0:
            filtered_indexes.append(value)
    start = 0
    for end in filtered_indexes:
        result.append(string[start:end])
        start = end
    if start < len(string):
        result.append(string[start:])
    return result

