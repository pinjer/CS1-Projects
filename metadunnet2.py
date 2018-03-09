#!/usr/bin/env python

##This metadunnet2 game has come up to Nicholas' mind, once again.
##He has a simple plan of what for you to do.
##Done in 2010

# This game is for careful use only, not 'splash-type' use.
# Remember not to fool around too much.
# You must remember not to fall into the lake without a device, such as a life preserver.
# You are not a good swimmer!


# The section set has this for each section (numbered):
#     Name of section
#     Boolean (whether user has already been there)*
#     Description of section
# *This is needed so that we automatically describe at the right times.
# (Notice repetitive sections do not matter because they have different room numbers.

import random  # For the questions

section_descr = [
    [
        'Dead end', False,  # 0
        '''You are at the dead end of a dirt road.  The road goes to the east, and in a
        distance you see a crosswalk.  The plants around you are shining rose bushes,
        and they are bright-dark green.'''
    ],
    [
        'E/W dirt road', False,  # 1
        '''You are on the continuation of a dirt road.  There are more bushes on the sides
        of you.  The road continues east and west.'''
    ],
    [
        'Crosswalk', False,  # 2
        '''You are on a crosswalk of three passages, one to the north, one to the east,
        and one to the south.  The ground here seems very soft.  You can also go back
        west.'''
    ],
    [
        'N/S road', False,  # 3
        '''You are on a north-south road.'''
    ],
    [
        "Rabbit's area", False,  # 4
        '''You are at the end of the road.  A path leads north.  Surprisingly, the bushes
        do not touch each other to the south.'''
    ],
    [
        'N/S road', False,  # 5
        '''You are on a north-south road.'''
    ],
    [
        'Building front', False,  # 6
        '''You are at the front of a large building to the north.  The bushes here do not
        touch the building at all.  You can also go back south.'''
    ],
    [
        'Building hallway', False,  # 7
        '''You are in the hallway of a building.  There are rooms to the east and west,
        and the hallway continues north.  The exit is to the south.'''
    ],
    [
        'Living room', False,  # 8
        '''You are in a living room.  It seems like a lot of stuff has been removed, due
        to moving situations.  All that there is left is a sofa on the ground here.
        The exit is to the west.  There is nothing here for you to lie down on.'''
    ],
    [
        'Art room', False,  # 9
        '''You are in an art room.  There are many decorations on the walls here.  There
        seems to be a paint bucket attached to the ground here, and a drawing easel in
        front of you.  The exit is to the east.'''
    ],
    [
        'N end of N/S hallway', False,  # 10
        '''You are at the end of a hallway.  You can go back south, and there is a
        door to the east.'''
    ],
    [
        'Arcade room', False,  # 11
        '''You are in a room which looks typically like a video arcade.  This room is full
        of broken lights and machines, which have apparently broke due to an earthquake
        a year ago.  There is a hole in the floor here, which you would probably fit
        in.  The exit is to the west.'''
    ],
    [
        'Soft area', False,  # 12
        '''You have reached a soft area.  It is pitch dark in here, and the ground here
        feels like a matress.  There is light through a path to the east.'''
    ],
    [
        'W end of E/W tunnel passage', False,  # 13
        '''You are at the end of a tunnel passage.  The lights here are shining brightly.
        The passage goes to the east.  There is an opening to the west.'''
    ],
    [
        'E/W tunnel passage', False,  # 14
        '''You are in the middle of the tunnel passage that goes east and west.'''
    ],
    [
        'E end of E/W tunnel passage', False,  # 15
        '''You are at the east end of the tunnel passage.  Stairs lead up and down from
        here.  You can also go back west.'''
    ],
    [
        'Up-down staircase', False,  # 16
        '''You are in an up-down stairway.  You can see the center of the staircase down
        below you.'''
    ],
    [
        'Top of staircase.', False,  # 17
        '''You are at the top of the staircase.  There is a path to the east and a ladder
        leading up to a room above.  You can also go back down the stairs.'''
    ],
    [
        'E end of E/W hallway', False,  # 18
        '''You are at the east end of a hallway.  There is a large hole in the floor
        here.  You can also go back west.'''
    ],
    [
        'W end of long E/W hallway', False,  # 19
        '''You are at the west end of a long E/W hallway.  The hallway goes east.'''
    ],
    [
        '2/3 west', False,  # 20
        '''You are 2/3 west of the long hallway.  There is a box here with a thin slit on
        it.'''
    ],
    [
        '2/3 east', False,  # 21
        '''You are 2/3 east of the long hallway.  There is a path to the south.'''
    ],
    [
        'N/S hallway', False,  # 22
        '''You are in a hallway which continues north and south.  There is a sports bin on
        the ground here.'''
    ],
    [
        'S end of N/S hallway', False,  # 23
        '''You are at the south end of a hallway.  There is a fruit cart here.'''
    ],
    [
        'E end of long E/W hallway', False,  # 24
        '''You are at the east end of a long hallway.  A path leads to the north.'''
    ],
    [
        'Math-solve corner', False,  # 25
        '''You are outside a math-solving center to the west, and there is a path to the
        south.'''
    ],
    [
        'Math-arena east', False,  # 26
        '''You are at the east side of an arena in which you have to solve tricky math
        problems to get by.  A path goes to the east.'''
    ],
    [
        'Math-arena west', False,  # 27
        '''You are at the west side of the arena.  A path goes to the west.'''
    ],
    [
        'Art show council', False,  # 28
        '''You have reached an art show council.  There are a countless amount of
        paintings on the walls.  On the wall you can see a handle with a spring on it.
        The exit is to the east.'''
    ],
    [
        'Up-down staircase', False,  # 29
        '''You are in an up-down stairway.  You can see the center of the staircase up
        above you.'''
    ],
    [
        'Bottom of staircase.', False,  # 30
        '''You are at the bottom of the staircase.  There is a path to the west.  You can
        also go back up the stairs.'''
    ],
    [
        'Breeze area', False,  # 31
        '''You are in a breeze area.  There is nothing here except for a slider on the
        wall.  The exit is to the east.'''
    ],
    [
        'Lakefront West', False,  # 32
        '''You are at the west side of a lake.  The water here seems very deep.  You can
        also go back west.  You notice that the bushes stop at the water here.'''
    ],
    [
        'Lakefront East', False,  # 33
        '''You are at the east side of the lake.  There is a path to the east.'''
    ],
    [
        'Finale Entrance', False,  # 34
        '''You are at the entrance of a finale center to the east.  You can also go back
        west.'''
    ],
    [
        "N Finale's room", False,  # 35
        '''You are in a finale's room in the north end of a hallway.'''
    ],
    [
        'Question room 1', False,  # 36
        '''You have reached a question room.  You must answer a question properly in order
        to get by.  Use the 'answer' command to answer the question.'''
    ],
    [
        'Finale N/S Hallway', False,  # 37
        '''You are in a north-south hallway.'''
    ],
    [
        'Question room 2', False,  # 38
        '''You are in a second question room.'''
    ],
    [
        'Finale N/S Hallway', False,  # 39
        '''You are in a north-south hallway.'''
    ],
    [
        'Question room 3', False,  # 40
        '''You are in a third question room.'''
    ],
    [
        "S Finale's room", False,  # 41
        '''You are in a finale's room in the south end of a hallway.'''
    ],
    [
        'Rocky boulder room', False,  # 42
        '''You have gone very high.  This room is filled with many rocks.  There is a
        ladder leading down a hole in the floor.'''
    ]
]

section = 0

# Now for the dungeon map telling us which directions take us to which sections.
# Any number 0-42 represents a new room, 255 special, and -1 always unable.

dir_north = 0
dir_south = 1
dir_east = 2
dir_west = 3
dir_up = 4
dir_down = 5

dungeon_map = [
    # nort sout east west up   down
    [-1, -1, 1, -1, -1, -1],  # 0
    [-1, -1, 2, 0, -1, -1],  # 1
    [5, 3, 32, 1, -1, -1],  # 2
    [2, 4, -1, -1, -1, -1],  # 3
    [3, 255, -1, -1, -1, -1],  # 4
    [6, 2, -1, -1, -1, -1],  # 5
    [255, 5, -1, -1, -1, -1],  # 6
    [10, 6, 8, 9, -1, -1],  # 7
    [-1, -1, -1, 7, -1, -1],  # 8
    [-1, -1, 7, -1, -1, -1],  # 9
    [-1, 7, 255, -1, -1, -1],  # 10
    [-1, -1, -1, 10, -1, 12],  # 11
    [-1, -1, 13, -1, -1, -1],  # 12
    [-1, -1, 14, 12, -1, -1],  # 13
    [-1, -1, 15, 13, -1, -1],  # 14
    [-1, -1, -1, 14, 16, 29],  # 15
    [-1, -1, -1, -1, 17, 15],  # 16
    [-1, -1, 18, -1, 42, 16],  # 17
    [-1, -1, -1, 17, -1, 255],  # 18
    [-1, -1, 20, -1, -1, -1],  # 19
    [-1, -1, 21, 19, -1, -1],  # 20
    [-1, 22, 24, 20, -1, -1],  # 21
    [21, 23, -1, -1, -1, -1],  # 22
    [22, -1, -1, -1, -1, -1],  # 23
    [25, -1, -1, 21, -1, -1],  # 24
    [-1, 24, -1, 26, -1, -1],  # 25
    [-1, -1, 25, 255, -1, -1],  # 26
    [-1, -1, 255, 28, -1, -1],  # 27
    [-1, -1, 27, -1, -1, -1],  # 28
    [-1, -1, -1, -1, 15, 30],  # 29
    [-1, -1, -1, 31, 29, -1],  # 30
    [-1, -1, 30, -1, -1, -1],  # 31
    [-1, -1, 255, 2, -1, -1],  # 32
    [-1, -1, 34, 255, -1, -1],  # 33
    [-1, -1, 255, 33, -1, -1],  # 34
    [-1, 255, -1, -1, -1, -1],  # 35
    [-1, -1, -1, -1, -1, -1],  # 36
    [36, 38, -1, -1, -1, -1],  # 37
    [-1, -1, -1, -1, -1, -1],  # 38
    [38, 40, -1, -1, -1, -1],  # 39
    [-1, -1, -1, -1, -1, -1],  # 40
    [255, -1, -1, -1, -1, -1],  # 41
    [-1, -1, -1, -1, -1, 17]  # 42
    # nort sout east west up   down
]

# Takable items

tk_shovel = [0, 'shovel']
tk_sword = [1, 'sword']
tk_brush = [2, 'paintbrush']
tk_paintbrush = [2, 'paintbrush']
tk_carrot = [3, 'carrot']
tk_credit = [4, 'credit']
tk_card = [4, 'credit']
tk_key = [5, 'key']
tk_statue = [6, 'statue']
tk_unicorn = [6, 'statue']
tk_racket = [7, 'racket']
tk_orange = [8, 'orange']
tk_pear = [9, 'pear']
tk_apple = [10, 'apple']
tk_calc = [11, 'calculator']
tk_calculator = [11, 'calculator']
tk_scientific = [11, 'calculator']
tk_ti = [11, 'calculator']
tk_texas = [11, 'calculator']
tk_ball = [12, 'ball']
tk_life = [13, 'life']
tk_preserver = [13, 'life']

# This is how they're explained to be in the room.

takable = [
    ['There is a shovel here.', 'A shovel'],  # 0
    ['There is a sword nearby.', 'A sword'],  # 1
    ['There is a paintbrush here.', 'A paintbrush'],  # 2
    ['There is a carrot here.', 'A carrot'],  # 3
    ['There is a credit card here.', 'A credit card'],  # 4
    ['There is a shiny brass key here.', 'A brass key'],  # 5
    ['There is a statue of a unicorn here.', 'A unicorn statue'],  # 6
    ['There is a tennis racket here.', 'A tennis racket'],  # 7
    ['There is an orange here.', 'An orange'],  # 8
    ['There is a pear here.', 'A pear'],  # 9
    ['There is an apple here.', 'An apple'],  # 10
    ['There is a scientific calculator here.', 'A scientific calculator'],  # 11
    ['There is a soft tennis ball here.', 'A tennis ball'],  # 12
    ['There is a life preserver here.', 'A life preserver']  # 13
]

# Descriptions of takable items.

takable_look = [
    'It is a normal shovel with a price tag attached to it reading $24.99.',
    'The sword was featured in World War II.',
    None,
    'It looks like a thin one.  Smells funny.',
    "The credit card has 'Nicholas McConnell' written neatly on it.",
    None,
    'You observe that the unicorn has one horn and no base for it to stand still.',
    'It has the letter T on it.',
    None,
    None,
    None,
    'It is a special calculator from the TI company.',
    None,
    'It says I. I. Wales.'
]

# Non-takable items

ntk_bush = [0, 'bushes']
ntk_bushes = [0, 'bushes']
ntk_easel = [1, 'easel']
ntk_slider = [2, 'slider']
ntk_hare = [3, 'rabbit']
ntk_rabbit = [3, 'rabbit']
ntk_dragon = [4, 'dragon']
ntk_sofa = [5, 'sofa']
ntk_couch = [5, 'sofa']
ntk_boulder = [6, 'boulder']
ntk_rock = [6, 'boulder']
ntk_handle = [7, 'handle']
ntk_spring = [7, 'handle']
ntk_lake = [8, 'water']
ntk_water = [8, 'water']
ntk_bucket = [9, 'bucket']
ntk_paintbucket = [9, 'bucket']
ntk_paint = [9, 'bucket']
ntk_ladder = [10, 'ladder']
ntk_box = [11, 'box']
ntk_slit = [11, 'box']
ntk_machine = [12, 'machines']
ntk_machines = [12, 'machines']
ntk_bin = [13, 'bin']
ntk_sportbin = [13, 'bin']
ntk_sportsbin = [13, 'bin']
ntk_cart = [14, 'cart']
ntk_fruitcart = [14, 'cart']
ntk_rose = [15, 'roses']
ntk_roses = [15, 'roses']

# This is how they're explained to be in the room.

nontakable = [
    None,  # 0
    None,  # 1
    None,  # 2
    'There is a rabbit here.',  # 3
    'There is a ferocious dragon here!',  # 4
    None,  # 5
    'There is a large boulder here.',  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    None,  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None  # 15
]

# Descriptions of nontakable items.

nontakable_look = [
    'The bushes have lots of roses in them.',
    'It is a normal painting easel with thin sheets of paper.',
    'The slider points to a breeze scale which has long since faded away.',
    'It looks like a hare to me.',
    'It is very willing to burn your face.',
    None,
    'It is just a boulder.  It cannot be moved.',
    None,
    None,
    'It is a paint bucket attached to the ground, and it seems to have red paint.',
    'The ladder is permanently attached to the hole.',
    'It is a box with a very thin slit and the following in sloppy writing:\n' +
    '    TO ADD 5 CREDITS, PUT CREDIT CARD HERE',
    'The machines looked like they once had fun games.',
    None,
    None,
    None
]

# Places things are

inventory = []

items = [
    ['dragon', 'bushes', 'roses'],  # 0
    ['sword', 'bushes', 'roses'],  # 1
    ['bushes', 'roses'],  # 2
    ['carrot', 'bushes', 'roses'],  # 3
    ['rabbit', 'bushes', 'roses'],  # 4
    ['bushes', 'roses'],  # 5
    ['bushes', 'roses'],  # 6
    [],  # 7
    ['sofa', 'statue'],  # 8
    ['easel', 'bucket'],  # 9
    [],  # 10
    ['machines'],  # 11
    [],  # 12
    [],  # 13
    [],  # 14
    [],  # 15
    [],  # 16
    ['ladder'],  # 17
    ['orange'],  # 18
    [],  # 19
    ['box'],  # 20
    ['pear', 'apple'],  # 21
    ['bin'],  # 22
    ['cart'],  # 23
    ['calculator'],  # 24
    [],  # 25
    [],  # 26
    [],  # 27
    ['handle'],  # 28
    [],  # 29
    [],  # 30
    ['slider'],  # 31
    ['water', 'bushes', 'roses'],  # 32
    ['water'],  # 33
    [],  # 34
    [],  # 35
    [],  # 36
    [],  # 37
    [],  # 38
    [],  # 39
    [],  # 40
    [],  # 41
    ['boulder', 'ladder']  # 42
]

diggables = [
    [],  # 0
    [],  # 1
    ['paintbrush'],  # 2
    [],  # 3
    [],  # 4
    [],  # 5
    [],  # 6
    [],  # 7
    [],  # 8
    [],  # 9
    [],  # 10
    [],  # 11
    [],  # 12
    [],  # 13
    [],  # 14
    [],  # 15
    [],  # 16
    [],  # 17
    [],  # 18
    [],  # 19
    [],  # 20
    [],  # 21
    [],  # 22
    [],  # 23
    [],  # 24
    [],  # 25
    [],  # 26
    [],  # 27
    [],  # 28
    [],  # 29
    [],  # 30
    [],  # 31
    [],  # 32
    [],  # 33
    [],  # 34
    [],  # 35
    [],  # 36
    [],  # 37
    [],  # 38
    [],  # 39
    [],  # 40
    [],  # 41
    ['racket']  # 42
]

saved = []

# Data.

dragon = 1
rabbit = 1
painted = 0
paint = 0
points = 0
finale = 0
credit = 5
finale_dir_take = ''  # Which way do you take to a question room?
breeze_level = 0

current_question_index = 0

questions = [
    ['What is the nearest whole dollar of the price of the shovel?', ['25', 'twenty-five']],
    ['Name either one of the two objects you found by digging.', ['brush', 'paintbrush', 'racket']],
    ['What is the last name on the credit card?', ['mcconnell']],
    ['What kind of a rabbit was hiding your credit card?', ['hare']],
    ['Name either one of the two objects you gave up items in for points.',
     ['bin', 'sportbin', 'sportsbin', 'cart', 'fruitcart']],
    ['What did you paint on the easel to get your key?', ['statue', 'unicorn']],
    ['How many horns does the unicorn statue have?', ['1', 'one']],
    ['What letter was on the racket?', ['t']],
    ['What color paint was in the paint bucket?', ['red']],
    ['What company made the calculator?', ['ti', 't', 'i', 'texas', 'instruments']],
    ['How many credits did the box add to the credit card?', ['5', 'five']]
]


# Now for functions.

def special_sections():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##This is a special variable condition about a section.
    ##For example, the painting room has something special.
    if section == 9:  # Art room
        if painted == 0:
            print \
                    """There is writing on the wall here telling you that you must paint a picture of
                    a unicorn on the easel."""
        else:
            print
            'The writing on the wall here tells you that you were great.'
    if section == 31:  # Breeze area
        if breeze_level == 0:
            print
            'It is normal room breeze in here.'
        elif breeze_level == 1:
            print
            'It is quite refreshing in here.'
        elif breeze_level == 2:
            print
            'It is coolingly windy in here.'
        elif breeze_level == 3:
            print
            'It is strongly windy in here.'
        elif breeze_level == 4:
            print
            'You are dead now.'
        else:
            print
            None
    if section == 36 or section == 38 or section == 40:  # Question rooms
        print
        'Your question is:'
        print
        questions[current_question_index][0]


def explain_long():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##Describe the current section and everything in it.
    print
    section_descr[section][0]
    print
    section_descr[section][2]
    special_sections()
    for i in items[section]:
        try:
            f = eval('lambda : ntk_%s[0]' % i)
            f = f()
            if isinstance(nontakable[f], str):
                print
                nontakable[f]
        except Exception, takable_item:
            f = eval('lambda : tk_%s[0]' % i)
            f = f()
            print
            takable[f][0]


def explain_short():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##Similar to last, but do not describe completely.
    print
    section_descr[section][0]
    special_sections()
    for i in items[section]:
        try:
            f = eval('lambda : ntk_%s[0]' % i)
            f = f()
            if isinstance(nontakable[f], str):
                print
                nontakable[f]
        except Exception, takable_item:
            f = eval('lambda : tk_%s[0]' % i)
            f = f()
            print
            takable[f][0]


def die():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    print
    '\nYou are dead.'
    show_points()
    for i in xrange(25):
        raw_input()
    explain_short()


def inven():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##List every item in the player's inventory.
    print
    'You currently have:'
    for i in inventory:
        f = eval('lambda : tk_%s[0]' % i)
        f = f()
        print
        takable[f][1]


def show_points():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if not bool(finale):
        print
        'You have scored %d out of a possible 50 points.' % points
    else:
        print
        'You have scored %d finale points out of a possible 50.' % points
        if points == 50:
            print
            '\n\nCongratulations!  You have won.'


def examine(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if not isinstance(nontakable_look[f[0]], str):
                print
                'I see nothing special about that.'
            else:
                print
                nontakable_look[f[0]]
        else:
            print
            "I don't see that here."
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0 or inventory.count(f[1]) > 0:
                if not isinstance(takable_look[f[0]], str):
                    print
                    'I see nothing special about that.'
                else:
                    print
                    takable_look[f[0]]
            else:
                print
                "I don't see that here."
        except Exception, not_object:
            print
            "I don't know what that is."


def take(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if obj == 'all':
        ##Take all items in section.
        ##Do not take the non-takable items.
        success = 0
        first_items_section = list(items[section])
        for i in first_items_section:
            try:
                f = eval('lambda : tk_%s' % i)
                f = f()
                print
                '%s: Taken.  ' % takable[f[0]][1]
                items[section].remove(f[1])
                inventory.append(f[1])
                success = 1
            except Exception, nontakable:
                pass
        if success == 0:
            print
            'Nothing to take.'
        if finale == 1:
            TT = 0
            if items[41].count('pear') > 0:
                TT += 10
            if items[41].count('apple') > 0:
                TT += 10
            if items[41].count('orange') > 0:
                TT += 10
            if items[41].count('ball') > 0:
                TT += 10
            if items[41].count('racket') > 0:
                TT += 10
            points = TT
    else:
        try:  ##Try non-take items first.
            f = eval('lambda : ntk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0:
                print
                'You cannot take that.'
            else:
                print
                'I do not see that here.'
        except Exception, not_nontakable:
            try:  ##Now try takable items.
                f = eval('lambda : tk_%s' % obj)
                f = f()
                if items[section].count(f[1]) > 0:
                    print
                    'Taken.  '
                    items[section].remove(f[1])
                    inventory.append(f[1])
                    if finale == 1:
                        TT = 0
                        if items[41].count('pear') > 0:
                            TT += 10
                        if items[41].count('apple') > 0:
                            TT += 10
                        if items[41].count('orange') > 0:
                            TT += 10
                        if items[41].count('ball') > 0:
                            TT += 10
                        if items[41].count('racket') > 0:
                            TT += 10
                        points = TT
                else:
                    print
                    'I do not see that here.'
            except Exception, not_object:
                print
                "I don't know what that is."


##Now do a drop and a check.

def drop_check():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if rabbit == 1 and items[4].count('carrot') > 0:
        print \
                '''The rabbit takes the carrot and hops away with it.  He left something on the
                ground.'''
        rabbit = 0
        items[4].remove('rabbit')
        items[4].remove('carrot')
        items[4].append('credit')
    if finale == 1:
        TT = 0
        if items[41].count('pear') > 0:
            TT += 10
        if items[41].count('apple') > 0:
            TT += 10
        if items[41].count('orange') > 0:
            TT += 10
        if items[41].count('ball') > 0:
            TT += 10
        if items[41].count('racket') > 0:
            TT += 10
        points = TT


def drop(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        print
        "You don't have that."
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if inventory.count(f[1]) > 0:
                print
                'Done.'
                inventory.remove(f[1])
                items[section].append(f[1])
                drop_check()
            else:
                print
                "You don't have that."
        except Exception, not_object:
            print
            "I don't know what that is."


def eat(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        print
        "You don't have that."
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if inventory.count(f[1]) > 0:
                if f[1] == 'orange' or f[1] == 'apple' or f[1] == 'pear':
                    print
                    'That tasted fine.'
                    inventory.remove(f[1])
                elif f[1] == 'carrot':
                    print
                    'That tasted unusual.'
                    inventory.remove(f[1])
                else:
                    print
                    'You shove %s down your throat, and start to choke.' % takable[f[0]][1].lower()
                    die()
            else:
                print
                "You don't have that."
        except Exception, not_object:
            print
            "I don't know what that is."


def lick(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        print
        "You don't have that."
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if inventory.count(f[1]) > 0:
                if f[1] == 'orange' or f[1] == 'apple' or f[1] == 'pear':
                    print
                    'You get a fine taste on your tongue.'
                elif f[1] == 'carrot':
                    print
                    'You get a confusing taste on your tongue.'
                else:
                    print
                    'You spread your tongue on %s and cut it on a sharp edge.' % takable[f[0]][1].lower()
                    print
                    'You start whining.'
                    die()
            else:
                print
                "You don't have that."
        except Exception, not_object:
            print
            "I don't know what that is."


def quaff(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if f[1] == 'water':
                print \
                        '''You manage to drink one sip of the water, but spit it out.  You notice that the
                        water is very salty.'''
            else:
                print
                "You can't drink that!"
        else:
            print
            "I don't see that here."
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0 or inventory.count(f[1]) > 0:
                print
                "You can't drink that!"
            else:
                print
                "I don't see that here."
        except Exception, not_object:
            print
            "I don't know what that is."


def shake(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##If shaking will do anything, put here.
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if f[1] == 'dragon':
                print
                'As you go up and shake the dragon, he burns your head with fire.'
                die()
            elif f[1] == 'rabbit':
                print
                'The rabbit gets very upset and tears your skin off with his teeth.'
                die()
            else:
                print
                'You cannot shake that.'
        else:
            print
            'I do not see that here.'
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if inventory.count(f[1]) > 0:
                print
                'Shaking %s seems to have no effect.' % takable[f[0]][1].lower()
            else:
                print
                "You don't have that."
        except Exception, not_object:
            print
            "I don't know what that is."


def breeze_set():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##For example, when the room is blowing very strong wind,
    ##the statue will fall apart and uncover a tennis ball,
    ##and the orange will be smashed onto the wall.
    if section == 31 and breeze_level == 3 and (inventory.count('statue') > 0 or items[section].count('statue') > 0):
        print \
                '''You notice the layers of wax on the unicorn statue ripping off, until they
                completely fall apart.  The wax must have uncovered a small tennis ball!'''
        if inventory.count('statue') > 0:
            inventory.remove('statue')
            inventory.append('ball')
        else:
            items[section].remove('statue')
            items[section].append('ball')
    if section == 31 and breeze_level == 3 and (inventory.count('orange') > 0 or items[section].count('orange') > 0):
        print \
                '''You notice the skin on the orange ripping off.  After it rips off, the orange
                gets smashed onto the wall, and pours down like juice.'''
        if inventory.count('orange') > 0:
            inventory.remove('orange')
        else:
            items[section].remove('orange')


def explain_if_new():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if not section_descr[section][1]:  # If not already been to
        explain_long()
        section_descr[section][1] = True
    else:
        explain_short()


def solve():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if section != 26 and section != 27:
        print
        'I see no problems to solve!'
    else:
        if inventory.count('calculator') == 0:
            print \
                    '''You try to pass the math arena, but you then get used to the fact that you
                    haven't really learned that complicated math.'''
        else:
            print
            'As you pass the arena, your calculator solves the problems correctly.\n'
            if section == 26:
                section = 27
            else:
                section = 26
            explain_if_new()


def swim():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if section != 32 and section != 33:
        print
        'I see no water!'
    else:
        if inventory.count('life') == 0:
            print \
                    '''You dive in the water and at first notice it is quite cold.  But then you
                    realize that you get used to the fact that you aren't really a good swimmer.'''
            die()
        else:
            if section == 32:
                section = 33
            else:
                section = 32
            explain_if_new()


def sleep():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if section != 12:  # Soft area
        print
        "You try to go to sleep while standing up here, but can't seem to do it."
    else:
        print \
                '''As soon as you start to doze off you begin dreaming.  You picture many
                explorers walking through a tunnel, looking for places to put in their items.
                Then you see yourself as one of these explorers.  While no one is looking, you
                leave the group and enter a cave.  You see yourself pulling up a cart, putting
                some supply of fruits in it, and then pushing the cart away from you again.
                After this, you immediately wake up.'''


def answer(ans):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if section != 36 and section != 38 and section != 40:
        print
        'I do not believe anyone asked you anything.'
    else:
        if questions[current_question_index][1].count(ans) > 0:
            print
            'Correct.'
            questions.remove(questions[current_question_index])
            if questions == []:
                questions.append(["No more questions, just do 'answer finale'.", ['finale']])
            current_question_index = 0
            if finale_dir_take == 'north':
                section -= 1
            else:
                section += 1
            explain_if_new()
        else:
            print
            'That answer is incorrect.'


def kill(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if inventory.count('sword') == 0:
        print
        'You have nothing you can use to kill things.'
    else:
        try:  ##Try non-take items first.
            f = eval('lambda : ntk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0:
                if f[1] == 'dragon':
                    print
                    'The dragon is killed and rolls over the bushes.  He uncovered something.'
                    dragon = 0
                    items[section].remove('dragon')
                    items[section].append('shovel')
                elif f[1] == 'rabbit':
                    print
                    'The rabbit is killed and rolls away.'
                    rabbit = 0
                    items[section].remove('rabbit')
                else:
                    print
                    'You cannot kill that.'
            else:
                print
                'I do not see that here.'
        except Exception, not_nontakable:
            try:  ##Now try takable items.
                f = eval('lambda : tk_%s' % obj)
                f = f()
                if items[section].count(f[1]) > 0:
                    print
                    'You cannot kill that.'
                else:
                    print
                    'I do not see that here.'
            except Exception, not_object:
                print
                "I don't know what that is."


def feed(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if f[1] == 'dragon':
                if inventory.count('carrot') > 0:
                    print
                    'You try to.  The dragon is generous enough and does not want to eat the carrot.'
                else:
                    print
                    'You have nothing with which to feed it.'
            elif f[1] == 'rabbit':
                if inventory.count('carrot') > 0:
                    drop('carrot')
                else:
                    print
                    'You have nothing with which to feed it.'
            else:
                print
                'You cannot feed that.'
        else:
            print
            'I do not see that here.'
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0:
                print
                'You cannot feed that.'
            else:
                print
                'I do not see that here.'
        except Exception, not_object:
            print
            "I don't know what that is."


def dig():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##If you have your shovel you can dig.  But do you find anything?
    if inventory.count('shovel') == 0:
        print
        'You have nothing you can use to dig.'
    else:
        if diggables[section] == []:
            print
            'Digging here reveals nothing.'
        else:
            print
            'I think you found something.'
            items[section] = items[section] + diggables[section]
            diggables[section] = []


def put(obj1, obj2):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##Put one object in another.
    try:
        f = eval('lambda : ntk_%s' % obj1)
        f = f()
        print
        "You don't have that."
    except Exception, not_nontakable:
        try:
            f = eval('lambda : tk_%s' % obj1)
            f = f()
            if inventory.count(f[1]) == 0:
                print
                "You don't have that."
            else:
                try:
                    f2 = eval('lambda : ntk_%s' % obj2)
                    f2 = f2()
                    if items[section].count(f2[1]) == 0:
                        print
                        'That indirect object is not here.'
                    else:
                        if f2[1] == 'bucket' and f[1] == 'paintbrush':  ##Put paint on the paintbrush
                            print
                            'Done.  Your paintbrush now has paint on it.'
                            paint = 1
                        elif f2[1] == 'box':  ##Put the credit card in the credit card box
                            if f[1] != 'credit':
                                print
                                "You can't put that in the credit card box!"
                            else:
                                print \
                                        '''As you drop in the credit card, the card begins to halt.  Finally, it
                                        disappears in a SWOOOOSH!  The credit card seems to have flown!'''
                                credit += 5
                                inventory.remove('credit')
                                items[9].append('credit')  # Move this to the art room
                        elif f2[1] == 'cart':  ##Put a fruit in the fruitcart
                            print
                            'You hear it zoom off into the distance.'
                            if f[1] == 'apple' or f[1] == 'orange' or f[1] == 'pear':
                                points += 10
                                show_points()
                            inventory.remove(f[1])
                            items[35].append(f[1])  # Add the items to the north end of the finale hallway
                        elif f2[1] == 'bin':  ##Put a sports use in the sports bin
                            print
                            'You hear it fall down into the deep hole and then slide off to the side.'
                            if f[1] == 'ball' or f[1] == 'racket':
                                points += 10
                                show_points()
                            inventory.remove(f[1])
                            items[35].append(f[1])
                        elif f2[1] == 'water':  ##Put something in lake
                            if f[1] == 'life':
                                print
                                'You hear it plop on the water and float to the other side.'
                                inventory.remove(f[1])
                                if section == 32:
                                    items[33].append('life')
                                else:
                                    items[32].append('life')
                            else:
                                print
                                'As you drop it in the water, you see it sink to the bottom.'
                                inventory.remove(f[1])
                        else:
                            if f[1] != f2[1]:
                                print \
                                        '''I don't know how to combine those objects.  Maybe you should just try dropping
                                        it.'''
                            else:
                                print
                                "You can't put anything in itself."
                except Exception, not_nontakable:
                    try:
                        f2 = eval('lambda : tk_%s' % obj2)
                        f2 = f2()
                        if inventory.count(f2[1]) == 0 and items[section].count(f2[1]) == 0:
                            print
                            'That indirect object is not here.'
                        else:
                            if f[1] != f2[1]:
                                print \
                                        '''I don't know how to combine those objects.  Maybe you should just try dropping
                                        it.'''
                            else:
                                print
                                "You can't put anything in itself."
                    except Exception, not_object:
                        print
                        "I don't know what that indirect object is."
        except Exception, not_object:
            print
            "I don't know what that object is."


def _paint(obj1, obj2):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##Paint with the paintbrush.
    if inventory.count('paintbrush') == 0:
        print
        'You have nothing you can use to paint.'
    else:
        try:
            f = eval('lambda : ntk_%s' % obj1)
            f = f()
            if inventory.count(f[1]) == 0 and items[section].count(f[1]) == 0:
                print
                "You don't seem to remember what that looks like."
            else:
                try:
                    f2 = eval('lambda : ntk_%s' % obj2)
                    f2 = f2()
                    if items[section].count(f2[1]) == 0:
                        print
                        'That indirect object is not here.'
                    else:
                        if f2[1] == 'easel':  ##Paint on easel
                            if paint == 0:
                                print
                                'You rub your paintbrush on the easel, but no paint is drawn.'
                            else:
                                print
                                'Done.'
                                paint = 0
                        else:
                            print
                            "You shouldn't paint on there."
                except Exception, not_nontakable:
                    try:
                        f2 = eval('lambda : tk_%s' % obj2)
                        f2 = f2()
                        if inventory.count(f2[1]) == 0 and items[section].count(f2[1]) == 0:
                            print
                            'That indirect object is not here.'
                        else:
                            print
                            "You shouldn't paint on there."
                    except Exception, not_object:
                        print
                        "I don't know what that indirect object is."
        except Exception, not_nontakable:
            try:
                f = eval('lambda : tk_%s' % obj1)
                f = f()
                if inventory.count(f[1]) == 0 and items[section].count(f[1]) == 0:
                    print
                    "You don't seem to remember what that looks like."
                else:
                    try:
                        f2 = eval('lambda : ntk_%s' % obj2)
                        f2 = f2()
                        if items[section].count(f2[1]) == 0:
                            print
                            'That indirect object is not here.'
                        else:
                            if f2[1] == 'easel':  ##Paint on easel
                                if paint == 0:
                                    print
                                    'You rub your paintbrush on the easel, but no paint is drawn.'
                                else:
                                    print
                                    'Done.'
                                    paint = 0
                                    if f[1] == 'statue' and painted == 0:
                                        print
                                        'The writing turns around and finds you amazing, dropping something here.'
                                        painted = 1
                                        items[section].append('key')
                            else:
                                print
                                "You shouldn't paint on there."
                    except Exception, not_nontakable:
                        try:
                            f2 = eval('lambda : tk_%s' % obj2)
                            f2 = f2()
                            if inventory.count(f2[1]) == 0 and items[section].count(f2[1]) == 0:
                                print
                                'That indirect object is not here.'
                            else:
                                print
                                "You shouldn't paint on there."
                        except Exception, not_object:
                            print
                            "I don't know what that indirect object is."
            except Exception, not_object:
                print
                "I don't know what that object is."


def special_move():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##This is a case where you cannot go that way unless certain conditions meet, etc.
    if section == 4:
        if items[section].count('rabbit') > 0:
            print \
                    '''The rabbit is hopping so annoyed that you would walk right into it.  He tells
                    you so by ripping the skin off your hands.'''
            die()
        else:
            print
            "You can't go that way."
    elif section == 6:
        if inventory.count('credit') == 0 or credit < 5:
            print
            "You don't have a credit card with enough credits to open this door."
        else:
            print
            'Your credit card has decreased from %d credits to %d.\n' % (credit, credit - 5)
            credit -= 5
            section = 7
            explain_if_new()
    elif section == 10:
        if inventory.count('key') == 0:
            print
            "You don't have a key that can open this door."
        else:
            section = 11
            explain_if_new()
    elif section == 18:
        if breeze_level == 3:
            print \
                    '''As you go down the hole, you notice some wind blowing from way down low.
                    Suddenly, the wind falls down in the hole, and blows you.  The wind blows you
                    back until you smash your head badly.  You bleed to death.'''
            die()
        else:
            section = 19
            explain_if_new()
    elif section == 26 or section == 27:
        solve()
    elif section == 32 or section == 33:
        swim()
    elif section == 34:
        if inventory.count('credit') == 0 or credit < 5:
            print
            "You don't have a credit card with enough credits to open this door."
        else:
            print
            'Your credit card has decreased from %d credits to %d.\n' % (credit, credit - 5)
            print \
                    '''Once you enter this room, you hear a noise.  You feel yourself falling 20 feet
                    underground, and a lot of stone blocks the view of the windows.

                    Welcome to finale.  Thank you for volunteering in the game.
                    '''
            section = 35
            points = 0
            finale = 1
            explain_if_new()
    elif section == 35:
        section = 36
        current_question_index = random.randrange(0, len(questions))
        explain_if_new()
        finale_dir_take = 'south'
    elif section == 41:
        section = 40
        current_question_index = random.randrange(0, len(questions))
        explain_if_new()
        finale_dir_take = 'north'


def move(direct):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    ##Use the dungeon map to go in the direction.
    ##I have to understand the directions that aren't the best.
    if direct == 'ne' or direct == 'nw' or direct == 'se' or direct == 'sw' or direct == 'northeast' or direct == 'northwest' or direct == 'southeast' or direct == 'southwest':
        print
        "You can't go that way."
    else:
        if direct == 'n':
            direct = 'north'
        if direct == 's':
            direct = 'south'
        if direct == 'e':
            direct = 'east'
        if direct == 'w':
            direct = 'west'
        if direct == 'u':
            direct = 'up'
        if direct == 'd':
            direct = 'down'
        try:
            f = eval('lambda : dir_%s' % direct)
            f = f()
            newroom = dungeon_map[section][f]
            if newroom == -1:
                print
                "You can't go that way."
            elif newroom == 255:
                special_move()
            else:
                section = newroom
                if section == 36 or section == 38 or section == 40:
                    current_question_index = random.randrange(0, len(questions))
                explain_if_new()
            breeze_set()
        except Exception, not_a_direction:
            print
            'I do not understand where you want me to go.'


def slide(obj, direction):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if f[1] == 'slider':
                if direction == 'left':
                    breeze_level -= 1
                    if breeze_level < 0:
                        print
                        'The slider will not go further in that direction.'
                        breeze_level = 0
                    elif breeze_level == 0:
                        print
                        'The room has returned to normal room breeze.'
                    elif breeze_level == 1:
                        print
                        'It is now quite refreshing in here.  Your hair is being blown.'
                    elif breeze_level == 2:
                        print
                        'It is pretty windy.  It is still cooling you off.'
                    elif breeze_level == 3:
                        print
                        'It is now very windy.  There is something very strong about this.'
                    elif breeze_level == 4:
                        print
                        'As the slider clicks into place, you immediately get smashed onto the wall.'
                        die()
                    else:
                        print
                        None
                    breeze_set()
                elif direction == 'right':
                    breeze_level += 1
                    if breeze_level == 1:
                        print
                        'It is now quite refreshing in here.  Your hair is being blown.'
                    elif breeze_level == 2:
                        print
                        'It is pretty windy.  It is still cooling you off.'
                    elif breeze_level == 3:
                        print
                        'It is now very windy.  There is something very strong about this.'
                    elif breeze_level == 4:
                        print
                        'As the slider clicks into place, you immediately get smashed onto the wall.'
                        die()
                    else:
                        print
                        None
                    breeze_set()
                else:
                    print
                    'You must indicate right or left.'
            else:
                print
                "You can't slide that!"
        else:
            print
            'I do not see that here.'
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0:
                print
                "You can't slide that!"
            else:
                print
                'I do not see that here.'
        except Exception, not_object:
            print
            "I don't know what that is."


def pull(obj):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    try:  ##Try non-take items first.
        f = eval('lambda : ntk_%s' % obj)
        f = f()
        if items[section].count(f[1]) > 0:
            if f[1] == 'handle':
                print \
                        '''As the handle clicks into place, and you release it, everything starts to get
                        blurry.  You begin to collapse for a moment, and then straighten yourself up.

                        Case closed.'''
                items[section] = items[section] + inventory
                inventory = []
                if points == 50:
                    items[9].append('life')
                section = 9  # Art room
                explain_short()
            else:
                print
                "You can't pull that!"
        else:
            print
            'I do not see that here.'
    except Exception, not_nontakable:
        try:  ##Now try takable items.
            f = eval('lambda : tk_%s' % obj)
            f = f()
            if items[section].count(f[1]) > 0:
                print
                "You can't pull that!"
            else:
                print
                'I do not see that here.'
        except Exception, not_object:
            print
            "I don't know what that is."


def play():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    print
    'Resumed.\n'
    explain_short()


def end():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    print
    show_points()
    for i in xrange(25):
        raw_input()
    explain_short()


def _list():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    print
    'You currently have saved:'
    for i in saved:
        print
        i[0]


def save(name):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if [na[0] for na in saved].count(name) > 0:
        index = 0
        for i in xrange(0, len(saved)):
            if saved[i][0] == name:
                index = i
        saved.remove(saved[index])
    saved.append(
        [name, section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale,
         credit, finale_dir_take, breeze_level, current_question_index, questions])
    print
    'Saved.'


def restore(name):
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    if [na[0] for na in saved].count(name) > 0:
        index = 0
        for i in xrange(0, len(saved)):
            if saved[i][0] == name:
                index = i
        section_descr = list(saved[index][1])
        section = int(saved[index][2])
        inventory = list(saved[index][3])
        items = list(saved[index][4])
        diggables = list(saved[index][5])
        dragon = int(saved[index][6])
        rabbit = int(saved[index][7])
        painted = int(saved[index][8])
        paint = int(saved[index][9])
        points = int(saved[index][10])
        finale = int(saved[index][11])
        credit = int(saved[index][12])
        finale_dir_take = str(saved[index][13])
        breeze_level = int(saved[index][14])
        current_question_index = int(saved[index][15])
        questions = list(saved[index][16])
        print
        'Restored.\n'
        explain_short()
    else:
        print
        'That is not saved.'


def startover():
    global section_descr, section, inventory, items, diggables, dragon, rabbit, painted, paint, points, finale, credit, finale_dir_take, breeze_level, current_question_index, questions
    for i in xrange(0, len(section_descr)):
        section_descr[i][1] = False
    section = 0
    inventory = []
    items = [
        ['dragon', 'bushes', 'roses'],  # 0
        ['sword', 'bushes', 'roses'],  # 1
        ['bushes', 'roses'],  # 2
        ['carrot', 'bushes', 'roses'],  # 3
        ['rabbit', 'bushes', 'roses'],  # 4
        ['bushes', 'roses'],  # 5
        ['bushes', 'roses'],  # 6
        [],  # 7
        ['sofa', 'statue'],  # 8
        ['easel', 'bucket'],  # 9
        [],  # 10
        ['machines'],  # 11
        [],  # 12
        [],  # 13
        [],  # 14
        [],  # 15
        [],  # 16
        ['ladder'],  # 17
        ['orange'],  # 18
        [],  # 19
        ['box'],  # 20
        ['pear', 'apple'],  # 21
        ['bin'],  # 22
        ['cart'],  # 23
        ['calculator'],  # 24
        [],  # 25
        [],  # 26
        [],  # 27
        ['handle'],  # 28
        [],  # 29
        [],  # 30
        ['slider'],  # 31
        ['water', 'bushes', 'roses'],  # 32
        ['water'],  # 33
        [],  # 34
        [],  # 35
        [],  # 36
        [],  # 37
        [],  # 38
        [],  # 39
        [],  # 40
        [],  # 41
        ['boulder', 'ladder']  # 42
    ]
    diggables = [
        [],  # 0
        [],  # 1
        ['paintbrush'],  # 2
        [],  # 3
        [],  # 4
        [],  # 5
        [],  # 6
        [],  # 7
        [],  # 8
        [],  # 9
        [],  # 10
        [],  # 11
        [],  # 12
        [],  # 13
        [],  # 14
        [],  # 15
        [],  # 16
        [],  # 17
        [],  # 18
        [],  # 19
        [],  # 20
        [],  # 21
        [],  # 22
        [],  # 23
        [],  # 24
        [],  # 25
        [],  # 26
        [],  # 27
        [],  # 28
        [],  # 29
        [],  # 30
        [],  # 31
        [],  # 32
        [],  # 33
        [],  # 34
        [],  # 35
        [],  # 36
        [],  # 37
        [],  # 38
        [],  # 39
        [],  # 40
        [],  # 41
        ['racket']  # 42
    ]
    dragon = 1
    rabbit = 1
    painted = 0
    paint = 0
    points = 0
    finale = 0
    credit = 5
    finale_dir_take = []
    breeze_level = 0
    current_question_index = 0
    questions = [
        ['What is the nearest whole dollar of the price of the shovel?', ['25', 'twenty-five']],
        ['Name either one of the two objects you found by digging.', ['brush', 'paintbrush', 'racket']],
        ['What is the last name on the credit card?', ['mcconnell']],
        ['What kind of a rabbit was hiding your credit card?', ['hare']],
        ['Name either one of the two objects you gave up items in for points.',
         ['bin', 'sportbin', 'sportsbin', 'cart', 'fruitcart']],
        ['What did you paint on the easel to get your key?', ['statue', 'unicorn']],
        ['What letter was on the racket?', ['t']],
        ['What color paint was in the paint bucket?', ['red']],
        ['What company made the calculator?', ['ti', 't', 'i', 'texas', 'instruments']],
        ['How many credits did the box add to the credit card?', ['5', 'five']]
    ]
    print
    'Restarted.\n'
    explain_if_new()


helpfile = \
    '''Metadunnet[2] by Nicholas McConnell
    (c) 2010

    Tips:

    Use 'metax' for the following game control commands:
        play
        pause
        end
        list
        save
        restore
        startover
        score

    Best directions are north, south, east, west, up, down.  They can be
    abbreviated to n, s, e, w, u, d.

    You never earn any points until you give up your items.  Simply finding places
    to give them up is not good enough.  You need to be /brave/ and think /hard/ so
    you can find the right places to give up certain items.

    If you go down a hole without an aid, such as a ladder, you wouldn't be able to
    get back up again.

    If you have the credit card or key to open a door, you should not be explicit
    as to shaking the door open.  You can just walk in the direction of the door.

    This game should not be played by someone with too much fear of a dragon.  You
    should probably save this game for ages 6 and up.
    Note that this game can /especially/ be played by someone at age 12!

    Good luck!
    '''

##Now use the commands we just defined and start reading the user inputs.

explain_if_new()

while True:
    ##Now we ask for the reply and split it up into lowercase words.
    reply = raw_input(">").lower().split()
    if reply == []:
        pass
    else:
        if reply[0] == 'i':
            inven()
        elif reply[0] == 'inventory':
            inven()
        elif reply[0] == 'examine':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'x':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'look':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'l':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'read':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'describe':
            for i in xrange(len(reply) - 1):
                if reply[1] == 'at':
                    reply.remove('at')
            if len(reply) == 1:
                explain_long()
            else:
                examine(reply[1])
        elif reply[0] == 'get':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                take(reply[1])
        elif reply[0] == 'take':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                take(reply[1])
        elif reply[0] == 'drop':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                drop(reply[1])
        elif reply[0] == 'throw':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                drop(reply[1])
        elif reply[0] == 'toss':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                drop(reply[1])
        elif reply[0] == 'shake':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                shake(reply[1])
        elif reply[0] == 'wave':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                shake(reply[1])
        elif reply[0] == 'go':
            if len(reply) == 1:
                print
                'You must supply a direction.'
            else:
                move(reply[1])
        elif reply[0] == 'north' or reply[0] == 'south' or reply[0] == 'east' or reply[0] == 'west' or reply[
            0] == 'northeast' or \
                        reply[0] == 'northwest' or reply[0] == 'southeast' or reply[0] == 'southwest' or reply[
            0] == 'up' or reply[0] == 'down' or \
                        reply[0] == 'n' or reply[0] == 's' or reply[0] == 'e' or reply[0] == 'w' or reply[0] == 'ne' or \
                        reply[0] == 'nw' or reply[0] == 'se' or reply[0] == 'sw' or reply[0] == 'u' or reply[0] == 'd':
            move(reply[0])
        elif reply[0] == 'move':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                if len(reply) == 2:
                    slide(reply[1], 'DEFAULT')  # What?!
                else:
                    slide(reply[1], reply[2])
        elif reply[0] == 'slide':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                if len(reply) == 2:
                    slide(reply[1], 'DEFAULT')  # What?!
                else:
                    slide(reply[1], reply[2])
        elif reply[0] == 'pull':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                pull(reply[1])
        elif reply[0] == 'put':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                if len(reply) < 4:
                    try:
                        trial = eval('lambda: ntk_%s' % reply[1])
                        trial = trial()
                        print
                        "You don't have that."
                    except Exception, e1:
                        try:
                            trial = eval('lambda: tk_%s' % reply[1])
                            trial = trial()
                            if inventory.count(trial[1]) == 0:
                                print
                                "You don't have that."
                            else:
                                print
                                'You must supply an indirect object.'
                        except Exception, e2:
                            print
                            "I don't know what that object is."
                else:
                    put(reply[1], reply[3])
        elif reply[0] == 'insert':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                if len(reply) < 4:
                    try:
                        trial = eval('lambda: ntk_%s' % reply[1])
                        trial = trial()
                        print
                        "You don't have that."
                    except Exception, e1:
                        try:
                            trial = eval('lambda: tk_%s' % reply[1])
                            trial = trial()
                            if inventory.count(trial[1]) == 0:
                                print
                                "You don't have that."
                            else:
                                print
                                'You must supply an indirect object.'
                        except Exception, e2:
                            print
                            "I don't know what that object is."
                else:
                    put(reply[1], reply[3])
        elif reply[0] == 'paint':
            if inventory.count('paintbrush') == 0:
                print
                'You have nothing you can use to paint.'
            else:
                if len(reply) == 1:
                    print
                    'You must supply an object.'
                else:
                    if len(reply) < 4:
                        try:
                            trial = eval('lambda: ntk_%s' % reply[1])
                            trial = trial()
                            if inventory.count(trial[1]) == 0 and items[section].count(trial[1]) == 0:
                                print
                                "You don't seem to remember what that looks like."
                            else:
                                print
                                'You must supply an indirect object.'
                        except Exception, e1:
                            try:
                                trial = eval('lambda: tk_%s' % reply[1])
                                trial = trial()
                                if inventory.count(trial[1]) == 0 and items[section].count(trial[1]) == 0:
                                    print
                                    "You don't seem to remember what that looks like."
                                else:
                                    print
                                    'You must supply an indirect object.'
                            except Exception, e2:
                                print
                                "I don't know what that object is."
                    else:
                        _paint(reply[1], reply[3])
        elif reply[0] == 'draw':
            if inventory.count('paintbrush') == 0:
                print
                'You have nothing you can use to paint.'
            else:
                if len(reply) == 1:
                    print
                    'You must supply an object.'
                else:
                    if len(reply) < 4:
                        try:
                            trial = eval('lambda: ntk_%s' % reply[1])
                            trial = trial()
                            if inventory.count(trial[1]) == 0 and items[section].count(trial[1]) == 0:
                                print
                                "You don't seem to remember what that looks like."
                            else:
                                print
                                'You must supply an indirect object.'
                        except Exception, e1:
                            try:
                                trial = eval('lambda: tk_%s' % reply[1])
                                trial = trial()
                                if inventory.count(trial[1]) == 0 and items[section].count(trial[1]) == 0:
                                    print
                                    "You don't seem to remember what that looks like."
                                else:
                                    print
                                    'You must supply an indirect object.'
                            except Exception, e2:
                                print
                                "I don't know what that object is."
                    else:
                        _paint(reply[1], reply[3])
        elif reply[0] == 'eat':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                eat(reply[1])
        elif reply[0] == 'lick':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                lick(reply[1])
        elif reply[0] == 'sleep':
            sleep()
        elif reply[0] == 'lie':
            sleep()
        elif reply[0] == 'answer':
            if section != 36 and section != 38 and section != 40:
                print
                'I do not believe anyone asked you anything.'
            else:
                if len(reply) == 1:
                    print
                    'You must give the answer on the same line.'
                else:
                    answer(reply[1])
        elif reply[0] == 'kill':
            if len(reply) == 1:
                if inventory.count('sword') == 0:
                    print
                    'You have nothing you can use to kill things.'
                else:
                    print
                    'You must supply an object.'
            else:
                kill(reply[1])
        elif reply[0] == 'slay':
            if len(reply) == 1:
                if inventory.count('sword') == 0:
                    print
                    'You have nothing you can use to kill things.'
                else:
                    print
                    'You must supply an object.'
            else:
                kill(reply[1])
        elif reply[0] == 'attack':
            if len(reply) == 1:
                if inventory.count('sword') == 0:
                    print
                    'You have nothing you can use to kill things.'
                else:
                    print
                    'You must supply an object.'
            else:
                kill(reply[1])
        elif reply[0] == 'feed':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                feed(reply[1])
        elif reply[0] == 'dig':
            dig()
        elif reply[0] == 'swim':
            swim()
        elif reply[0] == 'solve':
            solve()
        elif reply[0] == 'quaff':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                quaff(reply[1])
        elif reply[0] == 'drink':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                quaff(reply[1])
        elif reply[0] == 'sip':
            if len(reply) == 1:
                print
                'You must supply an object.'
            else:
                quaff(reply[1])
        elif reply[0] == 'help':
            print
            helpfile
        elif reply[0] == 'metax':
            if len(reply) == 1:
                print
                'You must supply a game command.'
            else:
                if reply[1] == 'play':
                    print
                    'The game is currently being played.'
                elif reply[1] == 'pause':
                    print
                    "Paused.  Type 'metax play' to resume play."
                    while True:
                        pp = raw_input()
                        pp = pp.lower()
                        pp = pp.split()
                        if len(pp) > 0:
                            if pp[0] == 'metax':
                                if len(pp) == 1:
                                    print
                                    'You must supply a game command.'
                                else:
                                    if pp[1] == 'play':
                                        play()
                                        break
                                    elif pp[1] == 'pause':
                                        print
                                        'The game is currently paused.'
                                    elif pp[1] == 'end':
                                        end()
                                    elif pp[1] == 'list':
                                        _list()
                                    elif pp[1] == 'save':
                                        if len(pp) == 2:
                                            print
                                            'You must supply a name for the save.'
                                        else:
                                            save(pp[2])
                                    elif pp[1] == 'restore':
                                        if len(pp) == 2:
                                            print
                                            'You must supply a name to restore.'
                                        else:
                                            restore(pp[2])
                                            if saved.count(pp[2]) > 0:
                                                break
                                    elif pp[1] == 'startover':
                                        startover()
                                    elif pp[1] == 'score':
                                        show_points()
                                    else:
                                        print
                                        'That is no such game command.'
                elif reply[1] == 'end':
                    end()
                elif reply[1] == 'list':
                    _list()
                elif reply[1] == 'save':
                    if len(reply) == 2:
                        print
                        'You must supply a name for the save.'
                    else:
                        save(reply[2])
                elif reply[1] == 'restore':
                    if len(reply) == 2:
                        print
                        'You must supply a name to restore.'
                    else:
                        restore(reply[2])
                elif reply[1] == 'startover':
                    startover()
                elif reply[1] == 'score':
                    show_points()
                else:
                    print
                    'That is no such game command.'
        else:
            print
            "I don't understand that."
