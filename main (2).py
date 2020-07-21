import pygame
from PIL import Image

#Initialize pygame
pygame.init()

#Create a screen
pixelGap = 1
gridX = gridY = 20

screen = pygame.display.set_mode((800 + (pixelGap * gridX), 800 + (pixelGap * gridY)))

#Title and Icon
pygame.display.set_caption('A* Path Finding')

whiteSquare = Image.new('RGBA', (40, 40), (255, 255, 255))

gridImages = []
def showGrid():
    for x in range(0, 800, 40 + pixelGap):
        for y in range(0, 800, 40 + pixelGap):
            gridImg = screen.blit(whiteSquare, (x,y))
            gridImages.append(gridImg)
            
# def checkMousePos():
#     for img in gridImages:
#         if(img.collidepoint(pygame.mouse.get_pos())):
#             print()






#Close when Quit
running = True
while running:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #Show Grid 
    showGrid()

    #Find which node is the mouse on
    # checkMousePos()


    pygame.display.update()