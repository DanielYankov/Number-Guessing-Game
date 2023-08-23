import pygame
from button import Button
from NumberGuessingGameClass import NumberGuessingGame

# game settings and initializing
pygame.init()
scale = 0.75
FPS = 30
pygame.display.set_caption('Number Guessing Game')
clock = pygame.time.Clock()
trigger = pygame.USEREVENT + 1
pygame.time.set_timer(trigger, 700)

# setting initial variables
screen_width = 500 * scale
screen_height = 800 * scale
background_color = (255, 255, 200)
text_color = (107, 71, 50)
screen = pygame.display.set_mode((screen_width, screen_height))
game = NumberGuessingGame()
dificulty_selected = False
guess_button_clicked = False
enter_clicked = False
game_over = False
change_frame = False
show_scale = True
user_input = ''
label_text = ''
final_text = ''
frame = 0
guessed_numbers = []

# available keys to write the number
number_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9 ]

# setting fonts for the game
font20 = pygame.font.SysFont('impact', round(20 * scale))
font40 = pygame.font.SysFont('impact', round(40 * scale))
font80 = pygame.font.SysFont('impact', round(80 * scale))
fonts = [font20, font40, font80]

# initializing buttons
easy_button_image = pygame.image.load('img\Easy_button.png').convert_alpha()
easy_button_hover_image = pygame.image.load('img\Easy_button_hover.png').convert_alpha()
easy_button = Button(15  * scale, 400 * scale, easy_button_image, easy_button_hover_image, scale)

medium_button_image = pygame.image.load('img\Medium_button.png').convert_alpha()
medium_button_hover_image = pygame.image.load('img\Medium_button_hover.png').convert_alpha()
medium_button = Button(175 * scale, 400 * scale, medium_button_image, medium_button_hover_image, scale)

hard_button_image = pygame.image.load('img\Hard_button.png').convert_alpha()
hard_button_hover_image = pygame.image.load('img\Hard_button_hover.png').convert_alpha()
hard_button = Button(335 * scale, 400 * scale, hard_button_image, hard_button_hover_image, scale)

guess_button_image = pygame.image.load('img\Guess_button.png').convert_alpha()
guess_button_hover_image = pygame.image.load('img\Guess_button_hover.png').convert_alpha()
guess_button = Button(175 * scale, 400 * scale, guess_button_image, guess_button_hover_image, scale)

play_again_button_image = pygame.image.load('img\Play_again_button.png').convert_alpha()
play_again_button_hover_image = pygame.image.load('img\Play_again_button_hover.png').convert_alpha()
play_again_button = Button(40 * scale, 500 * scale, play_again_button_image, play_again_button_hover_image,  scale)

exit_button_image = pygame.image.load('img\Exit_button.png').convert_alpha()
exit_button_hover_image = pygame.image.load('img\Exit_button_hover.png').convert_alpha()
exit_button = Button(300 * scale, 500 * scale, exit_button_image, exit_button_hover_image,  scale)

refactor_up_button_image = pygame.image.load('img\Refactor_up_button.png').convert_alpha()
refactor_up_button_hover_image = pygame.image.load('img\Refactor_up_button_hover.png').convert_alpha()
refactor_up_button = Button(20 * scale, 80 * scale, refactor_up_button_image, refactor_up_button_hover_image, scale)

refactor_down_button_image = pygame.image.load('img\Refactor_down_button.png').convert_alpha()
refactor_down_button_hover_image = pygame.image.load('img\Refactor_down_button_hover.png').convert_alpha()
refactor_down_button = Button(120 * scale, 80 * scale, refactor_down_button_image, refactor_down_button_hover_image, scale)

buttons = [easy_button, medium_button, hard_button, guess_button, play_again_button, exit_button, refactor_up_button, refactor_down_button]

#define function for creating text on the screen
def draw_text(text, font, text_color, x, y, centered = False):
    textSurface = font.render(text, True, text_color)
    textRect = textSurface.get_rect()
    if centered:
        textRect.center = (screen_width / 2, y * scale)
        screen.blit(textSurface, textRect)
    else:
        screen.blit(textSurface, (x * scale, y * scale))

# functions for drawing elements on the screen

def draw_board():
    screen.fill(background_color)

def draw_attempts():
    draw_text(f'Attempts left: {game.attemptsLeft}', fonts[1], text_color, 230, 20)

def draw_scale_game():
    draw_text(f'Scale game', fonts[1], text_color, 20, 20)

def draw_type_your_guess(frame):
    if frame < 2:
        text = 'type your guess.  '
    elif frame == 2:
        text = 'type your guess.. '
    elif frame == 3:
        text = 'type your guess...'

    draw_text(text, fonts[1], text_color, 20, 220, centered=True)

def draw_choose_dificulty():
    draw_text("Choose Dificulty:", fonts[1], text_color, 110, 300, centered=True)

def draw_user_input():
    draw_text(user_input, fonts[2], text_color, 180, 300, centered=True)

def draw_final_lable(text):
    draw_text(text, fonts[2], text_color, 180, 300, centered=True)

def draw_label(text):
    draw_text(text, fonts[1], text_color, 1, 150, centered=True)

def draw_guessed_numbers():
    draw_text('Guessed numbers:', fonts[1], text_color, 1, 550, centered=True)
    text = ', '.join(guessed_numbers)
    draw_text(text, fonts[1], text_color, 1, 600, centered=True)

# functions for reloading fonts, buttons and game screen after rescaling
def reload_buttons(buttons: Button):
    for button in buttons:
        image = button.original_image
        image_hover = button.original_image_hover
        width = image.get_width()
        height = image.get_height()
        button.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        button.image_hover = pygame.transform.scale(image_hover, (int(width * scale), int(height * scale)))
        button.rect = button.image.get_rect()
        button.rect.topleft = (button.original_x * scale, button.original_y * scale)

def reload_fonts(scale):
    font20 = pygame.font.SysFont('impact', round(20 * scale))
    font40 = pygame.font.SysFont('impact', round(40 * scale))
    font80 = pygame.font.SysFont('impact', round(80 * scale))
    fonts = [font20, font40, font80]
    return fonts




# game loop
run = True
while run:
    # draw background color
    draw_board()

    # drawing dificulty select screen
    if dificulty_selected == False:
        draw_choose_dificulty()
        if easy_button.draw(screen):
            game.choose_dificulty(1)
            dificulty_selected = True
        elif medium_button.draw(screen):
            game.choose_dificulty(2)
            dificulty_selected = True
        elif hard_button.draw(screen):
            game.choose_dificulty(3)
            dificulty_selected = True

        # functionality for rescaling screen
        if show_scale:
            draw_scale_game()
            if refactor_up_button.draw(screen):
                scale += 0.05
                reload_buttons(buttons)
                fonts = reload_fonts(scale)
                screen_width = 500 * scale
                screen_height = 800 * scale
                screen = pygame.display.set_mode((screen_width, screen_height))
            if refactor_down_button.draw(screen):
                scale -= 0.05
                if scale <= 0.05:
                    scale = 0.05
                reload_buttons(buttons)
                fonts = reload_fonts(scale)
                screen_width = 500 * scale
                screen_height = 800 * scale
                screen = pygame.display.set_mode((screen_width, screen_height))

    # drawing the game window
    else:
        draw_user_input()
        draw_label(label_text)
        draw_final_lable(final_text)

        # functionality for the game over screen
        if game_over:
            # reseting variables for playing again
            if play_again_button.draw(screen):
                game = NumberGuessingGame()
                dificulty_selected = False
                guess_button_clicked = False
                enter_clicked = False
                game_over = False
                user_input = ''
                label_text = ''
                final_text = ''
                guessed_numbers = []
                show_scale = False
            # exiting game button
            if exit_button.draw(screen):
                run = False
        # game window
        else:
            draw_type_your_guess(frame)
            draw_attempts()
            draw_guessed_numbers()
            if (guess_button.draw(screen) or enter_clicked) and user_input != '':
                label_text = game.make_guess(int(user_input))
                guessed_numbers.append(user_input)
                if label_text == '':
                    game_over = True
                    final_text = 'Game Over!'
                    label_text = f'The number was: {game.numberToGuess}'
                elif label_text == 'correct':
                    game_over = True
                    final_text = 'You Win!'
                    label_text = ''
                user_input = ''
            enter_clicked = False
            # trigger event for the animated lable "type your guess"
            if change_frame:
                frame += 1
                if frame > 3:
                    frame = 1
                change_frame = False

    # event handler
    for event in pygame.event.get():

        # quiting game when top right cross is pressed
        if event.type == pygame.QUIT:
            run = False

        #functionality for typing number on the screen
        if event.type == pygame.KEYDOWN and game_over == False:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[0:-1]
            elif event.key == pygame.K_RETURN:
                enter_clicked = True
            elif event.key in number_keys:
                user_input += event.unicode
                user_input_int = int(user_input)
                # limiting the user to only type numbers below 100
                if user_input_int > 100:
                    user_input_int = user_input_int // 10
                user_input = str(user_input_int)
        # catching the event for the animated "type your guess" lable
        if event.type == trigger:
            change_frame = True

    # setting game fps and updating display
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()