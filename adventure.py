base_room = {'0': '   ', '1': '   ', '2': '   ', '3': '   ', '4': '   ',
             '5': '   ', '6': '   ', '7': '   ', '8': '   ', '9': '   ',
             '10': '   ', '11': '   ', '12': '   ', '13': '   ', '14': '   ',
             '15': '   ', '16': '   ', '17': '   ', '18': '   ', '19': '   ',
             '20': '   ', '21': '   ', '22': '   ', '23': '   ', '24': '   '}

base_room_keys = list(base_room)
# I know this is ugly, couldn't come up with a better solution
room_up = (
    base_room_keys[0], base_room_keys[1], base_room_keys[2], base_room_keys[3], base_room_keys[4], base_room_keys[5],
    base_room_keys[6], base_room_keys[7], base_room_keys[8], base_room_keys[9])
room_down = (
    base_room_keys[15], base_room_keys[16], base_room_keys[17], base_room_keys[18], base_room_keys[19],
    base_room_keys[20],
    base_room_keys[21], base_room_keys[22], base_room_keys[23], base_room_keys[24])
room_left = (
    base_room_keys[0], base_room_keys[1], base_room_keys[5], base_room_keys[6], base_room_keys[10],
    base_room_keys[11],
    base_room_keys[15], base_room_keys[16], base_room_keys[20], base_room_keys[21])
room_right = (
    base_room_keys[3], base_room_keys[4], base_room_keys[8], base_room_keys[9], base_room_keys[13],
    base_room_keys[14],
    base_room_keys[18], base_room_keys[19], base_room_keys[23], base_room_keys[24])
edge_up = (base_room_keys[0], base_room_keys[1], base_room_keys[2], base_room_keys[3], base_room_keys[4])
edge_down = (base_room_keys[20], base_room_keys[21], base_room_keys[22], base_room_keys[23], base_room_keys[24])
edge_left = (base_room_keys[0], base_room_keys[5], base_room_keys[10], base_room_keys[15], base_room_keys[20])
edge_right = (base_room_keys[4], base_room_keys[9], base_room_keys[14], base_room_keys[19], base_room_keys[24])
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


def goblin_position():
    return list(current_room.keys())[list(current_room.values()).index(' @ ')]


def spawn_player(position):
    player = " O "
    current_room['{0}'.format(position)] = player


def spawn_goblin(position):
    goblin = " @ "
    current_room['{0}'.format(position)] = goblin


def player_direction():
    if player_position() in room_up:
        return "up"
    elif player_position() in room_down:
        return "down"
    elif player_position() in room_left:
        return "left"
    elif player_position() in room_right:
        return "right"


def update_player(position):
    player = " O "
    current_room['{0}'.format(player_position())] = "   "
    current_room['{0}'.format(position)] = player


def update_goblin(position):
    goblin = " @ "
    current_room['{0}'.format(goblin_position())] = "   "
    current_room['{0}'.format(position)] = goblin


def is_player_colliding():
    if player_position() in edge_up:
        return "up"
    if player_position() in edge_down:
        return "down"
    if player_position() in edge_left:
        return "left"
    if player_position() in edge_right:
        return "right"


def is_goblin_colliding():
    if goblin_position() in edge_up:
        return "up"
    if goblin_position() in edge_down:
        return "down"
    if goblin_position() in edge_left:
        return "left"
    if goblin_position() in edge_right:
        return "right"


def handle_commands():
    command = input("> ")
    command = command.lower()
    if command == "help":
        print("Commands:")
        print("left, right, up, down")
    elif (command == "left" or command == "a") and is_player_colliding() != "left":
        update_player(int(player_position()) - 1)
    elif (command == "right" or command == "d") and is_player_colliding() != "right":
        update_player(int(player_position()) + 1)
    elif (command == "up" or command == "w") and is_player_colliding() != "up":
        update_player(int(player_position()) - 5)
    elif (command == "down" or command == "s") and is_player_colliding() != "down":
        update_player(int(player_position()) + 5)
    else:
        print("Invalid command!")


def goblin_ai():
    if player_direction() == "up" and is_goblin_colliding() != "up":
        update_goblin(int(goblin_position()) - 5)
    if player_direction() == "down" and is_goblin_colliding() != "down":
        update_goblin(int(goblin_position()) + 5)
    if player_direction() == "left" and is_goblin_colliding() != "left":
        update_goblin(int(goblin_position()) - 1)
    if player_direction() == "right" and is_goblin_colliding() != "right":
        update_goblin(int(goblin_position()) + 1)


def main():
    print("Welcome to Adventure!")
    print("This game is controlled using commands,")
    print("For a list of all commands, enter \"help\"")
    start_room_logic()


def init(position):
    spawn_point = position
    spawn_player(spawn_point)
    spawn_goblin(2)


def start_room_logic():
    global current_room
    current_room = start_room
    print("You are now in the start room!")
    init(22)
    while True:
        if int(player_position()) == 24:
            end_room_logic()
        draw_room(current_room)
        handle_commands()
        goblin_ai()


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
