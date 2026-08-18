from config import *

from obj import BIRD, GROUND, PIPE

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    running = True
    
    all_sprites = pygame.sprite.Group()
    player = pygame.sprite.Group()
    pipe = pygame.sprite.Group()
    collision_objs = pygame.sprite.Group()

    bird = BIRD((player, all_sprites), bird_x, bird_y)

    ground = GROUND((all_sprites, collision_objs), ground_x, ground_y)
 
    create_pipes((pipe, all_sprites, collision_objs), random.randint(pipe_min_h, pipe_max_h), 0)
    pipe_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(pipe_timer, pipe_time) 

    while (running):
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pipe_timer:
                create_pipes((pipe, all_sprites, collision_objs), random.randint(pipe_min_h, pipe_max_h), 0)
                #print("Create pipes")

        #draw
        screen.fill("#66CCCC")
        all_sprites.draw(screen)

        #update
        if pygame.sprite.spritecollide(bird, collision_objs, False):
            print("collide")
            running = False
        else:
            print("not collide")

        all_sprites.update(dt)

        pygame.display.update()
    
    pygame.quit()
    sys.exit()

def create_pipes(group, first_h: int | float, first_y: int | float):
    second_h = HEIGHT - pipe_gap - first_h
    second_y = HEIGHT - second_h
    pipe_1 = PIPE(group, first_h, first_y)
    pipe_2 = PIPE(group, second_h, second_y) 

if __name__ == "__main__":
    main()
