import pygame

def menu(WIN, WIDTH, alg):
    pygame.init() 
    res = (WIDTH, WIDTH) 
    screen = pygame.display.set_mode(res) 
    color = (255,255,255) 
    color_light = (170,170,170) 
    color_dark = (100,100,100) 
    width = screen.get_width() 
    height = screen.get_height() 

    bigfont = pygame.font.SysFont('Corbel', 35)
    smallfont = pygame.font.SysFont('Corbel', 24)
    quit = bigfont.render('quit' , True , color)
    dfs_text = bigfont.render('Busca em Profundidade' , True , color)
    bfs_text = bigfont.render('Busca em Largura' , True , color)
    ucs_text = bigfont.render('Busca de Custo Uniforme' , True , color)
    gbfs_text = bigfont.render('Busca Gulosa pela Melhor Escolha' , True , color)
    a_star_text = bigfont.render('A*' , True , color)
    legenda1 = smallfont.render('M para voltar pro menu' , True , color)
    legenda2 = smallfont.render('C limpa o path' , True , color)
    legenda3 = smallfont.render('ESC limpa toda a tela' , True , color)
    legenda4 = smallfont.render('Botão esquerdo do Mouse coloca "começo"/"final"/"parede" nessa ordem' , True , color)
    legenda5 = smallfont.render('Botão direito do Mouse apaga blocos' , True , color)
    legenda6 = smallfont.render('SPACE começa o algoritmo' , True , color)

    while True: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 200 <= mouse[1] <= height/2 - 160: 
                    alg(WIN, WIDTH, "dfs")
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 150 <= mouse[1] <= height/2 - 110:
                    alg(WIN, WIDTH, "bfs")
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 100 <= mouse[1] <= height/2 - 60:
                    alg(WIN, WIDTH, "ucs")
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 50 <= mouse[1] <= height/2 - 10:
                    alg(WIN, WIDTH, "gbfs")
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 <= mouse[1] <= height/2 + 40:
                    alg(WIN, WIDTH, "a*")
                if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 + 50 <= mouse[1] <= height/2+90: 
                    pygame.quit()
                    
        screen.fill((60,25,60)) 
        
        mouse = pygame.mouse.get_pos()
        
        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 200 <= mouse[1] <= height/2 - 160:
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2 - 200, 500,40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2 - 200, 500,40])

        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 150 <= mouse[1] <= height/2 - 110:
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2 - 150, 500,40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2 - 150, 500,40])

        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 100 <= mouse[1] <= height/2 - 60:
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2 - 100, 500,40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2 - 100, 500,40])

        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 - 50 <= mouse[1] <= height/2 - 10:
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2 - 50, 500,40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2 - 50, 500,40])

        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 <= mouse[1] <= height/2 + 40:
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2, 500, 40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2, 500, 40])

        if width/2 - 200 <= mouse[0] <= width/2 - 200 + 500 and height/2 + 50 <= mouse[1] <= height/2+90: 
            pygame.draw.rect(screen,color_light,[width/2 - 200,height/2 + 50, 500, 40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2 - 200,height/2 + 50, 500, 40])

        screen.blit(dfs_text, (width/2 - 200, height/2 - 200))
        screen.blit(bfs_text, (width/2 - 200, height/2 - 150))
        screen.blit(ucs_text, (width/2 - 200, height/2 - 100))
        screen.blit(gbfs_text, (width/2 - 200, height/2 - 50))
        screen.blit(a_star_text, (width/2 - 200, height/2))
        screen.blit(quit, (width/2 - 200, height/2 + 50))


        screen.blit(legenda1, (width/2 - 360, height/2 + 200))
        screen.blit(legenda2, (width/2 - 360, height/2 + 230))
        screen.blit(legenda3, (width/2 - 360, height/2 + 260))
        screen.blit(legenda4, (width/2 - 360, height/2 + 290))
        screen.blit(legenda5, (width/2 - 360, height/2 + 320))
        screen.blit(legenda6, (width/2 - 360, height/2 + 350))
        
        pygame.display.update() 