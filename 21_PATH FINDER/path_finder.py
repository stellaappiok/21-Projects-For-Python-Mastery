import curses
from curses import wrapper
from collections import deque
import time

GRID = [
    ["#", "S", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "E", "#"]
]


def locate(symbol):
    for r, row in enumerate(GRID):
        for c, cell in enumerate(row):
            if cell == symbol:
                return r, c
    return None


def adjacent_cells(r, c):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(GRID) and 0 <= nc < len(GRID[0]):
            valid.append((nr, nc))

    return valid


def draw(screen, route):
    wall_color = curses.color_pair(1)
    path_color = curses.color_pair(2)

    route = set(route)

    for r, row in enumerate(GRID):
        for c, value in enumerate(row):
            if (r, c) in route:
                screen.addstr(r, c * 2, "*", path_color)
            else:
                screen.addstr(r, c * 2, value, wall_color)


def bfs(screen):
    start = locate("S")
    finish = "E"

    frontier = deque([(start, [start])])
    explored = {start}

    while frontier:
        current, trail = frontier.popleft()
        r, c = current

        screen.clear()
        draw(screen, trail)
        screen.refresh()
        time.sleep(0.15)

        if GRID[r][c] == finish:
            return trail

        for nxt in adjacent_cells(r, c):
            nr, nc = nxt

            if nxt in explored:
                continue

            if GRID[nr][nc] == "#":
                continue

            explored.add(nxt)
            frontier.append((nxt, trail + [nxt]))

    return None


def main(screen):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    bfs(screen)
    screen.getch()


wrapper(main)