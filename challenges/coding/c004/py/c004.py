from collections import Counter


def get_captain_room(room_list: list[int]) -> int:
    count_item = Counter(room_list)

    for room, count in count_item.items():
        if count == 1:
            return room

    return 0


if __name__ == '__main__':
    # Read Input
    k_input = input()
    room_input = input()
    data = room_input.split()

    # n groups
    n = int(k_input)

    # Define a list of rooms
    rooms = list(map(int, data[1:]))

    # Get captain room
    print(get_captain_room(rooms))
