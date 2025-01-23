import pygame
import sys
import time

CELL_SIZE = 60
MARGIN = 5
SLEEP_TIME = 0.5

COLOR_BG = (30, 30, 30)
COLOR_RED = (200, 50, 50)
COLOR_GREEN = (50, 200, 50)
COLOR_ACTIVE = (255, 215, 0)
COLOR_NEIGHBOR = (80, 160, 255)
COLOR_MIN = (255, 255, 0)
COLOR_SQUARE = (255, 128, 0)
COLOR_TEXT = (0, 0, 0)


def distinct_octal(x):
    digits_appear = [False] * 8
    while x:
        x, d = divmod(x, 8)
        if digits_appear[d]:  # Jeśli cyfra już wystąpiła
            return False
        digits_appear[d] = True  # Zaznacz cyfrę jako używaną
    return True


def main(T):
    pygame.init()
    n = len(T)
    WIDTH = n * CELL_SIZE + (n + 1) * MARGIN
    HEIGHT = n * CELL_SIZE + (n + 1) * MARGIN
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("github.com/kamilGie/ASRT-WDI")

    B = [[distinct_octal(T[i][j]) for j in range(n)] for i in range(n)]
    D = [[0] * n for _ in range(n)]
    max_side = 0

    def draw_square_outline(r, c, side, color, width=3):
        """rysuje kwadrat jak znajdzie"""
        x = c * CELL_SIZE + (c + 1) * MARGIN
        y = r * CELL_SIZE + (r + 1) * MARGIN
        w_px = side * CELL_SIZE + (side - 1) * MARGIN
        h_px = side * CELL_SIZE + (side - 1) * MARGIN
        pygame.draw.rect(screen, color, (x, y, w_px, h_px), width)

    def draw_grid_dp(
        active=None, neighbors=None, min_neighbor=None, highlight_square=None
    ):
        if neighbors is None:
            neighbors = []

        screen.fill(COLOR_BG)
        font = pygame.font.SysFont(None, 28)

        # rysuje pola czerwone i zielone
        for r in range(n):
            for c in range(n):
                x = c * CELL_SIZE + (c + 1) * MARGIN
                y = r * CELL_SIZE + (r + 1) * MARGIN
                color = COLOR_GREEN if B[r][c] else COLOR_RED
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

                if D[r][c] > 0:
                    text = font.render(str(D[r][c]), True, COLOR_TEXT)
                    rect = text.get_rect(
                        center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                    )
                    screen.blit(text, rect)

        # podswietlanie sasiadow
        for rr, cc in neighbors:
            if 0 <= rr < n and 0 <= cc < n:
                x = cc * CELL_SIZE + (cc + 1) * MARGIN
                y = rr * CELL_SIZE + (rr + 1) * MARGIN
                pygame.draw.rect(
                    screen, COLOR_NEIGHBOR, (x, y, CELL_SIZE, CELL_SIZE), width=4
                )

        # sasiad z min

        if min_neighbor and active and active[0] > 0 and active[1] > 1:
            (mr, mc) = min_neighbor
            xx = mc * CELL_SIZE + (mc + 1) * MARGIN
            yy = mr * CELL_SIZE + (mr + 1) * MARGIN
            pygame.draw.rect(screen, COLOR_MIN, (xx, yy, CELL_SIZE, CELL_SIZE), width=4)

        # aktywna komorka
        if active:
            (ar, ac) = active
            x = ac * CELL_SIZE + (ac + 1) * MARGIN
            y = ar * CELL_SIZE + (ar + 1) * MARGIN
            pygame.draw.rect(
                screen, COLOR_ACTIVE, (x, y, CELL_SIZE, CELL_SIZE), width=5
            )

        #  znaleziony kwadrat
        if highlight_square:
            (sq_i, sq_j, sq_side) = highlight_square
            draw_square_outline(sq_i, sq_j, sq_side, COLOR_SQUARE, width=4)

        pygame.display.flip()

    for i in range(n):
        for j in range(n):
            # Obsługa zdarzeń (zamknięcie okna)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if B[i][j]:
                top_val = D[i - 1][j] if i > 0 else float("inf")
                left_val = D[i][j - 1] if j > 0 else float("inf")
                diag_val = D[i - 1][j - 1] if (i > 0 and j > 0) else float("inf")

                neighbors = []
                if i > 0:
                    neighbors.append((i - 1, j))
                if j > 0:
                    neighbors.append((i, j - 1))
                if i > 0 and j > 0:
                    neighbors.append((i - 1, j - 1))

                draw_grid_dp(
                    active=(i, j),
                    neighbors=neighbors,
                    min_neighbor=None,
                    highlight_square=None,
                )
                time.sleep(SLEEP_TIME)

                min_val = min(top_val, left_val, diag_val)
                min_neighbor = None
                if min_val == top_val:
                    min_neighbor = (i - 1, j)
                if min_val == left_val:
                    min_neighbor = (i, j - 1)
                if min_val == diag_val:
                    min_neighbor = (i - 1, j - 1)

                draw_grid_dp(
                    active=(i, j),
                    neighbors=neighbors,
                    min_neighbor=min_neighbor,
                    highlight_square=None,
                )
                time.sleep(SLEEP_TIME)

                if i == 0 or j == 0:
                    D[i][j] = 1
                else:
                    D[i][j] = 1 + min_val
                max_side = max(max_side, D[i][j])

                highlight = None
                if D[i][j] > 1:
                    side = D[i][j]
                    top_i = i - side + 1
                    left_j = j - side + 1
                    highlight = (top_i, left_j, side)

                draw_grid_dp(
                    active=(i, j),
                    neighbors=neighbors,
                    min_neighbor=min_neighbor,
                    highlight_square=highlight,
                )
                time.sleep(SLEEP_TIME)

            else:
                draw_grid_dp(active=(i, j))
                time.sleep(SLEEP_TIME * 0.1)

    time.sleep(1)
    return max_side


if __name__ == "__main__":
    # Mozna zmienac tablice na inne
    T = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    main(T)

    T = [[1, 1, 1], [1, 9, 1], [1, 1, 1]]
    main(T)

    T = [[1, 1, 1], [1, 1, 9], [1, 1, 1]]
    main(T)

    T = [
        [7, 9, 5, 8, 9],
        [64, 9, 8, 1, 66],
        [32, 2, 4, 6, 9],
        [8, 24, 33, 1, 9],
        [77, 8, 5, 12, 64],
    ]
    main(T)
