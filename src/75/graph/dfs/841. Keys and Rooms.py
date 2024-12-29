from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        keys = deque(rooms[0])
        visited_rooms = [0] * len(rooms)
        visited_rooms[0] = 1

        while keys:
            key = keys.popleft()

            if not visited_rooms[key]:
                visited_rooms[key] = 1
                keys.extend(rooms[key])

        return all(visited_rooms)
