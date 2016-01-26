from Common import *

width = 1280
height = 720
size = width, height
pygame.init()

class Instructions:
    def run(self):
        screen = pygame.display.set_mode(size)
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    exit()
            mouse = pygame.mouse.get_pos()

            pygame.Surface.fill(WHITE)

            # Display some text
            textColor = BLUE
            font = pygame.font.Font(None, 36)
            text = font.render("Hello There", 1, (10, 10, 10))
            textSurf, textRect = text_objects(text, largeText,textColor)
            textRect.center = (screen.Center)
            screen.blit(textSurf, textRect)