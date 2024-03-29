import pygame


pygame.init()
pygame.mixer.init()


razryvnaya1 = "images/cheri cheri lady speed up.mp3"
razryvnaya2 = "images/Ғазизхан Шекербеков - Көріктім (Sped Up).mp3"
razryvnaya3 = "images/Ерболат Кудайбергенов - Мен қазақпын [Мәтін  Текст  Lyrics].mp3"

musiclist = [razryvnaya1, razryvnaya2, razryvnaya3]
current_music_index = 0


pygame.mixer.music.load(musiclist[current_music_index])
pygame.mixer.music.play()

screen = pygame.display.set_mode((929, 913))
mem = pygame.image.load('images/mem.png')


run = True
pause = False

while run:
    screen.blit(mem, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
              
                current_music_index = (current_music_index + 1) % len(musiclist)
                pygame.mixer.music.load(musiclist[current_music_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                
                current_music_index = (current_music_index - 1) % len(musiclist)
                pygame.mixer.music.load(musiclist[current_music_index])
                pygame.mixer.music.play()

    pygame.display.flip()


pygame.quit()
