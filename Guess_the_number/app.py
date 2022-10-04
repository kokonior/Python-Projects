from turtle import pos
import pygame
import random
from pygame import K_BACKSPACE, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pyparsing import White

pygame.init()

#declaring the height and width of our window
width = 800
height = 450

#having some colors ready to use
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

#initializing the window
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("GUESS WHAT?")
font = pygame.font.Font('./WigendaTypewrite.ttf', 24)

Playing = True
guess_text = ''
timer = pygame.time.Clock()
fps = 60
typing = False
decisioning = False
solution = random.randint(1, 100)
print(solution)

def decision(inp):
    inp = int(inp)

    pygame.draw.rect(screen, black, [0, 0, width, height])
    screen.fill(black)

    close = pygame.draw.rect(screen, grey, [700, 370, 40, 40], 0, 5)
    close_text = font.render('X', True, black)
    screen.blit(close_text, (710, 375))
    
    if solution == inp:
        text = font.render("You win !!!", True, white)
        screen.blit(text, (width/2, height/2))
    else:
        text = font.render("You lose !!!", True, white)
        screen.blit(text, (width/2, height/2))

    return

def draw_text_inp(guess_text, typing):
    pygame.draw.rect(screen, black, [0, 0, (width), (height)])
    menuText = font.render('Guess the number(1-100)', True, white)
    screen.blit(menuText, (230, 110))

    if typing:
        pygame.draw.rect(screen, grey, [260, 180, 250, 50], 0, 5)

    entry_rect = pygame.draw.rect(screen, grey, [260, 180, 250, 50], 5, 5)
    entry_text = font.render(f'{guess_text}', True, black)
    screen.blit(entry_text, (270, 180))

    return entry_rect


while Playing:
    
    textbox = draw_text_inp(guess_text, typing)
    guessButton = pygame.draw.rect(
        screen, grey, [330, 260, 100, 30], 0, 5)
    guessButtonText = font.render('Guess', True, black)
    screen.blit(guessButtonText, (340, 260))

    close = pygame.draw.rect(screen, grey, [700, 370, 40, 40], 0, 5)
    close_text = font.render('X', True, black)
    screen.blit(close_text, (710, 375))

    if decisioning:
        decision(guess_text)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False
        if event.type == pygame.TEXTINPUT and typing:
            guess_text += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(guess_text) > 0 and typing:
                guess_text = guess_text[:-1]
        if event.type == pygame.MOUSEBUTTONUP:
            if textbox.collidepoint(event.pos):
                typing = True
                guess_text = ''
            if guessButton.collidepoint(event.pos):
                decisioning = True
            if close.collidepoint(event.pos):
                pygame.quit()
        
    pygame.display.flip()
pygame.quit()