#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    this is a lockbox code
    """

    if not boxes:
        return False
    
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box
    
    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key < n and key not in visited:
                    stack.append(key)
    
    return len(visited) == n
