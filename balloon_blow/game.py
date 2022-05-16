import pygame

from balloon_blow.settings import FPS, WIDTH, HEIGHT, BLACK
from balloon_blow.sprites import Balloon


class Game:
    def __init__(self) -> None:
        self.window = None
        self.is_running = False
        self.clock = pygame.time.Clock()

    def start(self) -> None:
        pygame.init()
        pygame.font.init()

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

        # set title
        pygame.display.set_caption("Balloon Blow")

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.balloon = Balloon(self)

    def cleanup(self) -> None:
        pygame.font.quit()
        pygame.quit()

    def execute(self) -> None:
        self.start()
        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.window.fill(BLACK)
            self.render()
            self.update()
            pygame.display.flip()
            self.dt = self.clock.tick(FPS) / 1000
        self.cleanup()

    def handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self.is_running = False

    def render(self) -> None:
        for sprite in self.all_sprites.sprites():
            sprite.draw(self.window)

    def update(self) -> None:
        self.balloon.update()
