#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is
        a list of keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return (False)

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return (all(visited))
