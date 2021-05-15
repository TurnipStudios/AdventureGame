base_room = {'0': '   ', '1': '   ', '2': '   ', '3': '   ', '4': '   ',
             '5': '   ', '6': '   ', '7': '   ', '8': '   ', '9': '   ',
             '10': '   ', '11': '   ', '12': '   ', '13': '   ', '14': '   ',
             '15': '   ', '16': '   ', '17': '   ', '18': '   ', '19': '   ',
             '20': '   ', '21': '   ', '22': '   ', '23': '   ', '24': '   '}

start_room = base_room.copy()
end_room = base_room.copy()
current_room = start_room


def draw_inside(room):
    if room == start_room:
        start_room['24'] = '/H\\'
    elif room == end_room:
        end_room['24'] = ' H '


def draw_room(room):
    draw_inside(room)
    print("-----------------")
    print("|" + room['0'] + room['1'] + room['2'] + room['3'] + room['4'] + "|")
    print("|" + room['5'] + room['6'] + room['7'] + room['8'] + room['9'] + "|")
    print("|" + room['10'] + room['11'] + room['12'] + room['13'] + room['14'] + "|")
    print("|" + room['15'] + room['16'] + room['17'] + room['18'] + room['19'] + "|")
    print("|" + room['20'] + room['21'] + room['22'] + room['23'] + room['24'] + "|")
    print("-----------------")


def player_position():
    return list(current_room.keys())[list(current_room.values()).index(' O ')]


def spawn_player(position):
    player = " O "
    current_room['{0}'.format(position)] = player


def update_player(position):
    player = " O "
    current_room['{0}'.format(player_position())] = "   "
    current_room['{0}'.format(position)] = player


def handle_commands():
    command = input("> ")
    command = command.lower()
    if command == "help":
        print("Commands:")
        print("left, right, up, down")
    elif command == "left":
        update_player(int(player_position()) - 1)
    elif command == "right":
        update_player(int(player_position()) + 1)
    elif command == "up":
        update_player(int(player_position()) - 5)
    elif command == "down":
        update_player(int(player_position()) + 5)
    else:
        print("Invalid command!")


def main():
    print("Welcome to Adventure!")
    print("This game is controlled using commands,")
    print("For a list of all commands, enter \"help\"")
    start_room_logic()


def init(position):
    spawn_point = position
    spawn_player(spawn_point)


def start_room_logic():
    global current_room
    current_room = start_room
    print("You are now in the start room!")
    init(12)
    while True:
        if int(player_position()) == 24:
            end_room_logic()
        draw_room(current_room)
        handle_commands()


def end_room_logic():
    global current_room
    current_room = end_room
    print("You are now in the end room!")
    init(23)
    while True:
        if int(player_position()) == 24:
            start_room_logic()
        draw_room(current_room)
        handle_commands()


main()
