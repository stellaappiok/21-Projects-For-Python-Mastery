import pygame
import random
import time
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Reaction Trainer")

BACKGROUND_COLOR = (0, 25, 40)

HEADER_HEIGHT = 50
EDGE_PADDING = 30

SPAWN_INTERVAL = 400
SPAWN_EVENT = pygame.USEREVENT + 1

MAX_MISSES = 3

FONT = pygame.font.SysFont("arial", 24)


class Bubble:
    MAX_RADIUS = 30
    ANIMATION_SPEED = 0.2

    OUTER_COLOR = "red"
    INNER_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.growing = True

    def animate(self):
        if self.radius >= self.MAX_RADIUS:
            self.growing = False

        if self.growing:
            self.radius += self.ANIMATION_SPEED
        else:
            self.radius -= self.ANIMATION_SPEED

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self.OUTER_COLOR,
            (self.x, self.y),
            int(self.radius)
        )

        pygame.draw.circle(
            surface,
            self.INNER_COLOR,
            (self.x, self.y),
            int(self.radius * 0.8)
        )

        pygame.draw.circle(
            surface,
            self.OUTER_COLOR,
            (self.x, self.y),
            int(self.radius * 0.6)
        )

        pygame.draw.circle(
            surface,
            self.INNER_COLOR,
            (self.x, self.y),
            int(self.radius * 0.4)
        )

    def is_clicked(self, mouse_x, mouse_y):
        distance = math.hypot(
            mouse_x - self.x,
            mouse_y - self.y
        )

        return distance <= self.radius


def center_x(surface):
    return SCREEN_WIDTH / 2 - surface.get_width() / 2


def format_time(seconds_passed):
    minutes = int(seconds_passed // 60)
    seconds = int(seconds_passed % 60)
    tenths = int((seconds_passed * 10) % 10)

    return f"{minutes:02}:{seconds:02}.{tenths}"


def draw_header(screen, elapsed, hits, misses):
    pygame.draw.rect(
        screen,
        "grey",
        (0, 0, SCREEN_WIDTH, HEADER_HEIGHT)
    )

    speed = round(hits / elapsed, 1) if elapsed > 0 else 0

    labels = [
        FONT.render(f"Time: {format_time(elapsed)}", True, "black"),
        FONT.render(f"Speed: {speed} t/s", True, "black"),
        FONT.render(f"Hits: {hits}", True, "black"),
        FONT.render(f"Lives: {MAX_MISSES - misses}", True, "black")
    ]

    screen.blit(labels[0], (10, 10))
    screen.blit(labels[1], (220, 10))
    screen.blit(labels[2], (450, 10))
    screen.blit(labels[3], (650, 10))


def draw_game(screen, bubbles):
    screen.fill(BACKGROUND_COLOR)

    for bubble in bubbles:
        bubble.draw(screen)


def show_results(screen, elapsed, hits, clicks):
    screen.fill(BACKGROUND_COLOR)

    speed = round(hits / elapsed, 1) if elapsed > 0 else 0
    accuracy = round((hits / clicks) * 100, 1) if clicks > 0 else 0

    results = [
        FONT.render(f"Time: {format_time(elapsed)}", True, "white"),
        FONT.render(f"Speed: {speed} t/s", True, "white"),
        FONT.render(f"Hits: {hits}", True, "white"),
        FONT.render(f"Accuracy: {accuracy}%", True, "white")
    ]

    positions = [100, 200, 300, 400]

    for label, y in zip(results, positions):
        screen.blit(label, (center_x(label), y))

    pygame.display.update()

    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                pygame.quit()
                quit()


def main():
    clock = pygame.time.Clock()

    bubbles = []

    hits = 0
    clicks = 0
    misses = 0

    start_time = time.time()

    pygame.time.set_timer(
        SPAWN_EVENT,
        SPAWN_INTERVAL
    )

    running = True

    while running:
        clock.tick(60)

        current_click = False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        elapsed = time.time() - start_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == SPAWN_EVENT:

                x = random.randint(
                    EDGE_PADDING,
                    SCREEN_WIDTH - EDGE_PADDING
                )

                y = random.randint(
                    HEADER_HEIGHT + EDGE_PADDING,
                    SCREEN_HEIGHT - EDGE_PADDING
                )

                bubbles.append(Bubble(x, y))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_click = True
                clicks += 1

        for bubble in bubbles[:]:

            bubble.animate()

            if bubble.radius <= 0:
                bubbles.remove(bubble)
                misses += 1
                continue

            if current_click and bubble.is_clicked(mouse_x, mouse_y):
                bubbles.remove(bubble)
                hits += 1

        if misses >= MAX_MISSES:
            show_results(
                WINDOW,
                elapsed,
                hits,
                clicks
            )

        draw_game(WINDOW, bubbles)
        draw_header(WINDOW, elapsed, hits, misses)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
