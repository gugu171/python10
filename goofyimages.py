import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('mi is ading imag and bickrond imgie')
background_image = pygame.transform.scale(
    pygame.image.load('goofybackground.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
goofyimage = pygame.transform.scale(
    pygame.image.load('goofycartoon.png').convert_alpha(), (200,200))
goofyrect = goofyimage.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render('HALLO WURLD', True,
                                         pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(goofyimage, (0,0))
        display_surface.blit(goofyimage, goofyrect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
        