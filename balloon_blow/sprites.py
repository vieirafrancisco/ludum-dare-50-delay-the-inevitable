import pygame

from balloon_blow.settings import BLACK, HEIGHT, WHITE, WIDTH

BALLOON_MAX_RADIUS = 200
BALLOON_FILL_RATE = 10
BALLOON_INITIAL_SIZE = 50


class Balloon(pygame.sprite.Sprite):
    def __init__(self, game):
        groups = [game.all_sprites]
        super().__init__(groups)
        self.game = game
        self.image = pygame.Surface((400, 400))
        pygame.draw.circle(self.image, WHITE, (200, 200), BALLOON_INITIAL_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.size = BALLOON_INITIAL_SIZE
        self.fill_time = 0

    def draw(self, surface):
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, WHITE, (200, 200), self.size)
        surface.blit(self.image, self.rect)

    def update(self):
        # back to initial / TODO: game over
        if self.size >= BALLOON_MAX_RADIUS:
            self.size = BALLOON_INITIAL_SIZE

        # fill balloon
        if hasattr(self.game, "dt"):
            self.fill_time += self.game.dt
            if self.fill_time >= 2:
                self.size += BALLOON_FILL_RATE
                self.fill_time = 0
