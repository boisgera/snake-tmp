import pyxel

pyxel.init(30, 30, fps=18)


class Snake:
    def __init__(self, _geometry, _head, _direction):
        self.geometry = _geometry
        self.head = self.geometry[-1]
        self.direction = _direction
        self.newhead = [
            self.head[0] + self.direction[0],
            self.head[1] + self.direction[1],
        ]

    def len(self):
        return len(self.geometry)


ORDI = Snake([[2, 9], [3, 9], [4, 9]], [], [1, 0])


rocks = []

for x in range(30):
    for y in range(30):
        if (x + y) % 5 == 0 and (x - y) % 11 == 0:
            rocks.append([x, y])


def spawn_fruit():
    global fruit
    while True:
        fruit = [pyxel.rndi(0, 29), pyxel.rndi(0, 29)]
        if (fruit not in rocks) and (fruit not in ORDI.geometry):
            break


spawn_fruit()


def chng_dir():
    tirage = pyxel.rndi(0, 1)

    if (ORDI.direction == [1, 0]) or (ORDI.direction == [-1, 0]):
        if ORDI.head[0] <= 14:
            ORDI.direction = [0, 1]
        else:
            ORDI.direction = [0, -1]

    if (ORDI.direction == [0, 1]) or (ORDI.direction == [0, -1]):
        if ORDI.head[0] <= 14:
            ORDI.direction = [1, 0]
        else:
            ORDI.direction = [-1, 0]


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    print(f"{ORDI.head} head avant")

    ORDI.newhead = [ORDI.head[0] + ORDI.direction[0], ORDI.head[1] + ORDI.direction[1]]

    print(f"{ORDI.newhead} newhead avant")
    print(f"{ORDI.direction} direction avant")

    # guidage sur x
    if (ORDI.head[0] - fruit[0] < 0) and ORDI.direction != [-1, 0]:
        ORDI.direction = [1, 0]
    elif (ORDI.head[0] - fruit[0] > 0) and ORDI.direction != [1, 0]:
        ORDI.direction = [-1, 0]

    if ORDI.newhead in rocks and (
        ORDI.direction == [1, 0] or ORDI.direction == [-1, 0]
    ):
        if ORDI.head[0] <= 14:
            ORDI.direction = [0, 1]

        else:
            ORDI.direction = [0, -1]

    # guidage sur y (peut être là le pb, pcq on peut pu toucher aux x une fois qu'on y est)
    else:
        if (ORDI.head[1] - fruit[1] < 0) and ORDI.direction != [0, -1]:
            ORDI.direction = [0, 1]
        elif (ORDI.head[1] - fruit[1] > 0) and ORDI.direction != [0, 1]:
            ORDI.direction = [0, -1]

    print(f"{ORDI.direction} direction")
    print(f"{ORDI.newhead} newhead")

    ORDI.newhead = [ORDI.head[0] + ORDI.direction[0], ORDI.head[1] + ORDI.direction[1]]

    print(f"{ORDI.newhead} newhead après")
    print(f"{ORDI.head} head après")

    if (
        (ORDI.newhead in rocks)
        or ORDI.newhead[0] < 0
        or ORDI.newhead[0] > 29
        or ORDI.newhead[1] < 0
        or ORDI.newhead[1] > 29
    ):
        chng_dir()

    elif ORDI.newhead == fruit:
        ORDI.geometry = ORDI.geometry + [ORDI.newhead]
        spawn_fruit()

    else:
        ORDI.geometry = ORDI.geometry[1:] + [ORDI.newhead]


#    print(f"{ORDI.head} head avant")
#    print(f"{ORDI.newhead} newhead avant")
#    print(f"{ORDI.direction} direction avant")

#    ORDI.head = ORDI.newhead

#    print(ORDI.head)
#    print(f"{ORDI.newhead} newhead")
#    print(f"{ORDI.direction} direction")


def draw():
    pyxel.cls(9)
    for x, y in rocks:
        pyxel.pset(x, y, 0)
    pyxel.pset(fruit[0], fruit[1], 4)
    for x, y in ORDI.geometry[:-1]:
        pyxel.pset(x, y, 14)
    ORDI.head = ORDI.geometry[-1]
    pyxel.pset(ORDI.head[0], ORDI.head[1], 15)


pyxel.run(update, draw)
