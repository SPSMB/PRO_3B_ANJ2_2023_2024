import pygame
import sys

pygame.init()

width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

white = (255, 255, 255)
black = (0,0,0)
ball_color = (228, 252, 13)
paddle_color = (34,255,0)

paddle_width = 9
paddle_height = 100
paddle_speed = 6
player1_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

ball_radius = 15
ball_speed_x = 5
ball_speed_y = 5
ball = pygame.Rect(width // 2 - ball_radius // 2, height // 2 - ball_radius // 2, ball_radius, ball_radius)

player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

collision_sound = pygame.mixer.Sound("collision.wav")
goal_sound = pygame.mixer.Sound("goal.wav")

def update():
    global ball_speed_x, ball_speed_y, player1_score, player2_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
        collision_sound.play()
    
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1
        collision_sound.play()
    
    if ball.left <= 0:
        #player 2 dal gol
        goal_sound.play()
        player2_score +=1
        reset_ball()
    elif ball.right >= width:
        #player 1 dal gol
        goal_sound.play()
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (width // 2, height // 2)
    ball_speed_x *= -1
    ball_speed_y *= -1

def draw():
    win.fill(black)
    pygame.draw.rect(win, white, (width//2 - 5, 0, 5, height))
    pygame.draw.rect(win, paddle_color, player1_paddle)
    pygame.draw.rect(win, paddle_color, player2_paddle)
    pygame.draw.ellipse(win, ball_color, ball)
    score_text = font.render(f"{player1_score} : {player2_score}", True, white)
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_paddle.top > 0:
            player1_paddle.y -= paddle_speed
        if keys[pygame.K_s] and player1_paddle.bottom < height:
            player1_paddle.y += paddle_speed
        if keys[pygame.K_UP] and player2_paddle.top > 0:
            player2_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2_paddle.bottom < height:
            player2_paddle.y += paddle_speed
        update()
        draw()
        clock.tick(60)

if __name__ == "__main__":
    main()