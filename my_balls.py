import pygame
from random import randint


class Ball:

    def __init__(self, x, y, dx, dy, radius, r, dr, g, dg, b, db, surface):
        """ x, y are a coords of centr of the circle.
            x >= 0 and x <= :WINDOW_WIDTH
            y >= 0 and y <= :WINDOW_HEIGHT
            if bouth dx and dy are 0, we'll give them come value manually,
            cause
            if we don't we'll get a stuck ball
            radius > 0 and radius < min(WINDOW_WIDTH, WINDOW_HEIGHT)
            r, g ,b are a color components (r, g, b)
            dr, db, dg - are steps to change color component
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
        self.dr = dr
        self.g = g
        self.dg = dg
        self.b = b
        self.db = db
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

    def check_collision(self, ball):
        return False


def change_color_component(color_component, d_color_component):
    if 10 + d_color_component < color_component + d_color_component < (
                                                    245 - d_color_component):
        color_component += d_color_component
    else:
        d_color_component *= -1
        color_component += d_color_component
    return color_component, d_color_component


def main():
    """ lowe_r and upper_r is a color part r in RGB model random range, should
        be between 1 and 254
    """
    lower = 6
    upper = 249
    dr = 4
    dg = 4
    db = 4
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
                          randint(lower, upper), dr,
                          randint(lower, upper), dg,
                          randint(lower, upper), db, surface))
    while run:
        clock.tick(45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            any_ball_clicked = False
            for ball in balls:
                if ball.is_clicked(*pygame.mouse.get_pos()):
                    ball.r, ball.dr = change_color_component(ball.r, ball.dr)
                    any_ball_clicked = True
            if not any_ball_clicked:
                r_fill, dr_fill = change_color_component(r_fill, dr_fill)
                ball.color = (ball.r, ball.g, ball.b)

        if pygame.mouse.get_pressed(num_buttons=3)[2]:
            any_ball_clicked = False
            for ball in balls:
                if ball.is_clicked(*pygame.mouse.get_pos()):
                        ball.g, ball.dg = change_color_component(ball.g,
                                                                 ball.dg)
                        any_ball_clicked = True
            if not any_ball_clicked:
                g_fill, dg_fill = change_color_component(g_fill, dg_fill)
                ball.color = (ball.r, ball.g, ball.b)

        if pygame.mouse.get_pressed(num_buttons=3)[1]:
            any_ball_clicked = False
            for ball in balls:
                if ball.is_clicked(*pygame.mouse.get_pos()):
                    ball.b, ball.db = change_color_component(ball.b, ball.db)
                    any_ball_clicked = True
            if not any_ball_clicked:
                b_fill, db_fill = change_color_component(b_fill, db_fill)
                ball.color = (ball.r, ball.g, ball.b)

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
