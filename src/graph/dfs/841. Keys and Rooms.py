from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        rooms_opened = [0]
        keys = rooms[0]

        while keys:
            key = keys.pop()
            if key not in rooms_opened:
                rooms_opened.append(key)
                for k in rooms[key]:
                    if k not in rooms_opened:
                        keys.append(k)

        return len(rooms_opened) == len(rooms)
