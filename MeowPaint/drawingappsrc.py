from utils import * #runs inits too

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meow Paint!")

def init_grid(rows, cols, color):
    grid = [] #empty list(array), each item is a px in the grid

    for i in range(rows):
        grid.append([])
        for j in range(cols): #can use an _ if u don't need j 4 anything
            grid[i].append(color)#if u dont come back 2 this at some point, how is each col item beign added
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid): #enum numbers each loop result, so a list would look like (1.A) (2.B)
        for j, pixel in enumerate(row): #^ is used 2 iterate thru list items but just prints items by default
            #j/i*px allows each pixel 2 be drawn thru row n col index V
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def draw(win, grid, buttons):
    win.fill(BG_COLOR)#fill window w a color
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos 
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

run = True
#limit loop speed
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR) 
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
buttons = [Button(10, button_y, 50, 50, BLACK),
           Button(70, button_y, 50, 50, RED),
           Button(130, button_y, 50, 50, GREEN),
           Button(190, button_y, 50, 50, BLUE),
           Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
           Button(310, button_y, 50, 50, WHITE, "Clear", BLACK)]

#event loop, ends when ur pygame 'x button' is clicked
while run:
    #loop speed limit = FPS var
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color

                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK


    draw(WIN, grid, buttons)

pygame.quit()