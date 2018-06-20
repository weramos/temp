"""
A welcome hello to the awesome Python class.
"""


def greeting(name=None):
    """
    Generate greeting, defaulting to smart aleck message if name not specified.
        - name: Name to use in greeting.
    """
    return "Surely, you have a name?" if name is None else f"Hello, {name}"
