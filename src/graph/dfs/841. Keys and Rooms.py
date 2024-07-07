class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        roomsOpen = {0}

        while keys:
            key = keys.pop()
            roomsOpen.add(key)
            newKeys = rooms[key]

            while newKeys:
                newKey = newKeys.pop()

                if newKey not in roomsOpen and newKey not in keys:
                    keys.add(newKey)

        return len(roomsOpen) == len(rooms)