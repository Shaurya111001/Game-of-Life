import pygame
pygame.init()
pygame.display.set_caption("GAME OF LIFE")
icon = pygame.image.load('unnamed.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((500,540))
running = True
grid = []
alive_grid = []
delayed_alive = []
delayed_dead = []
GREY = (211,211,211)
var = 0
smallfont = pygame.font.SysFont('Corbel',35) 
text1 = smallfont.render('Start' , True , (0,0,255)) 
text2 = smallfont.render('Clear' , True , (0,0,255)) 
text3 = smallfont.render('Stop' , True , (0,0,255)) 
for row in range(50):
    grid.append([])
    for column in range(50):
        grid[row].append(0)


def alive_or_dead(a,b):
    count = 0
    i = a-1
    j = b-1
    m = a+1
    n = b+1
    if a == 0:
        i = a
    if b == 0:
        j = b
    if a == 49:
        m = a
    if b == 49:
        n = b
    while i <= m: 
        while j <= n:
            if grid[i][j] == 1 and (i != a or j != b): 
                count = count + 1
            j = j + 1
        if b == 0:
            j = b
        if b == 49:
            j == b-1
        else:
            j = b-1
        i = i + 1
    return count

def clear_all(grid, alive_grid):
    alive_grid.clear()
    for i in range(50):
        for j in range(50):
            if grid[i][j] == 1:
                grid[i][j] = 0
                pygame.draw.rect(screen, (0,0,0), [10*i ,10*j ,10,10])
                pygame.draw.rect(screen, (211,211,211), [10*i ,10*j ,10,10],2)

def birth(grid, alive_grid):
    for i in range(50):
        for j in range(50):
            if grid[i][j] == 0:
                n = alive_or_dead(i,j)
                if n == 3:
                    delayed_alive.append((i,j))


def kill(alive_grid):
    for k in alive_grid:
        (i,j) = k
        n = alive_or_dead(i,j)
        if n<2 or n>3:
            delayed_dead.append((i,j))
            
def apply_changes(delayed_alive,delayed_dead):
    for l in delayed_alive:
        (i,j) = l
        grid[i][j] = 1
        pygame.draw.rect(screen, (0,0,255), [10*i ,10*j ,10,10])
        alive_grid.append((i,j))
    for d in delayed_dead:
        (i,j) = d
        grid[i][j] = 0
        pygame.draw.rect(screen, (0,0,0), [10*i ,10*j ,10,10])
        pygame.draw.rect(screen, (211,211,211), [10*i ,10*j ,10,10],2)
        alive_grid.remove((i,j))
    delayed_alive.clear()
    delayed_dead.clear() 
            



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            r = pos[0]
            c = pos[1]
            if r<120 and c>500:
                var = 1
            elif r>380 and c>500:
                var = 0
            elif r>190 and r<310 and c>500:
                var = 2
            elif c>500:
                pass
            else:
                grid[r//10][c//10]=1
                alive_grid.append((r//10,c//10))

    dim = 540
    pygame.draw.rect(screen,(211,211,211),[0,dim-40,120,40])
    screen.blit(text1,(35,dim-40))
    pygame.draw.rect(screen,(211,211,211),[190,dim-40,120,40])
    screen.blit(text2,(210,dim-40))
    pygame.draw.rect(screen,(211,211,211),[380,dim-40,120,40])
    screen.blit(text3,(dim-130,dim-40))
    if var == 1:
        birth(grid, alive_grid)
        kill(alive_grid)
        apply_changes(delayed_alive,delayed_dead)
    if var == 2:
        clear_all(grid, alive_grid)
        var = 0
    for i in range(50):
        for j in range(50):
            color = GREY
            if grid[i][j] == 1:
                color = (0,0,255)
                pygame.draw.rect(screen, color, [10*i ,10*j ,10,10])
            else:
                pygame.draw.rect(screen, color, [10*i ,10*j ,10,10],2)
            pygame.display.flip()
    
pygame.quit()