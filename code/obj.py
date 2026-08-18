from config import *

class GROUND(pygame.sprite.Sprite):
    def __init__(self, group, x: int | float, y: int | float) -> None:
        super().__init__(group)
        self.image = pygame.Surface((ground_w, ground_h))
        self.image.fill("Brown")
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, dt):
        pass


class BIRD(pygame.sprite.Sprite):
    def __init__(self, group, x: int | float, y: int | float) -> None:
        super().__init__(group)
        self.image = pygame.Surface((bird_w, bird_h))
        self.image.fill("Yellow")
        self.rect = self.image.get_rect(topleft = (x, y))

        self.player_gravity = 0

    def set_gravity(self, dt: int | float) -> None:
        self.player_gravity += fall
        self.rect.y += self.player_gravity * dt

    def move(self, dt: int | float) -> None:
        key = pygame.key.get_pressed()

        if (self.rect.top <= 0):
            self.rect.top = 0
        else:
            if (key[pygame.K_SPACE]):
                self.player_gravity = gravity * jump


    def update(self, dt: int | float) -> None:
        self.set_gravity(dt)
        self.move(dt)


class PIPE(pygame.sprite.Sprite):
    def __init__(self, group, pipe_h: int | float, y: int | float) -> None:
        super().__init__(group)
        self.image = pygame.Surface((pipe_w, pipe_h))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft = (WIDTH, y))
        self.speed = pipe_speed 

    def move(self, dt: int | float) -> None:
        self.rect.x -= self.speed * dt

    def update(self, dt: int | float) -> None:
        if self.rect.right < 0:
            self.kill()
        self.move(dt)
        
