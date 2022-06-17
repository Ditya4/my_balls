import pygame
from random import randint


class Ball:

    def __init__(self, x, y, dx, dy, radius, r, g, b, surface):
        """ x, y are a coords of centr of the circle.
            x >= 0 and x <= :WINDOW_WIDTH
            y >= 0 and y <= :WINDOW_HEIGHT
            if bouth dx and dy are 0, we'll give them come value manually,
            cause
            if we don't we'll get a stuck ball
            radius > 0 and radius < min(WINDOW_WIDTH, WINDOW_HEIGHT)
            r, g ,b are a color components (r, g, b)
        """
        if dx == dy == 0:
            dx = randint(1, 5)
            dy = randint(1, 5)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b
        self.surface = surface

    def move(self):
        global WINDOW_WIDTH, WINDOW_HEIGHT
        if 0 < self.x + self.dx < WINDOW_WIDTH:
            self.x += self.dx
        else:
            self.dx *= -1
        if 0 < self.y + self.dy < WINDOW_HEIGHT:
            self.y += self.dy
        else:
            self.dy *= -1

    def show(self):
        pygame.draw.circle(self.surface, (self.r, self.g, self.b),
                           (self.x, self.y), self.radius)

    def is_clicked(self, x, y):
        if self.x - self.radius <= x <= self.x + self.radius:
            if self.y - self.radius <= y <= self.y + self.radius:
                return True
        return False


def main():
    """ lowe_r and upper_r is a color part r in RGB model random range, should
        be between 1 and 254
    """
    lower_r = 6
    upper_r = 249
    dr = 4
    g_fill = 245
    dg_fill = 2
    b_fill = 245
    db_fill = 2
    r_fill = 245
    dr_fill = 2
    run = True
    balls = []
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("My balls")
    for number in range(BALL_COUNT):
        balls.append(Ball(randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS),
                          randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS),
                          randint(-3, 3), randint(-3, 3), BALL_RADIUS,
                          randint(lower_r, upper_r), randint(lower_r, upper_r),
                          randint(lower_r, upper_r), surface))
    while run:
        clock.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            for ball in balls:
                if ball.is_clicked(*pygame.mouse.get_pos()):
                    if 5 <= ball.r <= 248:
                        ball.r += dr
                    else:
                        dr *= -1
                        ball.r += dr
                    ball.color = (ball.r, ball.g, ball.b)
                else:
                    if db_fill + 10 < b_fill + db_fill < 248 - db_fill:
                        b_fill += db_fill
                    else:
                        db_fill *= -1
                        b_fill += db_fill
        if pygame.mouse.get_pressed(num_buttons=3)[2]:
            for ball in balls:
                if ball.is_clicked(*pygame.mouse.get_pos()):
                    if 5 <= ball.r <= 250:
                        ball.r -= dr
                    else:
                        dr *= -1
                        ball.r -= dr
                    ball.color = (ball.r, ball.g, ball.b)
                else:
                    if dg_fill < g_fill + dg_fill < 255 - dg_fill:
                        g_fill += dg_fill
                    else:
                        dg_fill *= -1
                        g_fill += dg_fill
        if pygame.mouse.get_pressed(num_buttons=3)[1]:
            if dr_fill + 10 < r_fill + dr_fill < 249 - dr_fill:
                r_fill += dr_fill
            else:
                dr_fill *= -1
                r_fill += dr_fill
        surface.fill((r_fill, g_fill, b_fill,))
        for ball in balls:
            ball.move()
            ball.show()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 500
    BALL_COUNT = 5
    BALL_RADIUS = 30
    main()
