import pygame

def main():
    pygame.init()
    # screen
    screen = pygame.display.set_mode((640, 480))
    #clock
    clock = pygame.time.Clock()
    
    # radius for drawing
    radius = 15
    # Initial mode or color
    mode = 'blue'
    # List to store points for drawing
    points = []
    # Initial shape to draw
    shape = 'line'
    
    while True:
        # Get the state of keyboard keys
        pressed = pygame.key.get_pressed()
        
        # Check if Alt or Ctrl keys are held
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # Check if the window's close button is clicked
            if event.type == pygame.QUIT:
                return
            # Check for keyboard input
            if event.type == pygame.KEYDOWN:
                # Check for specific key combinations to quit the program
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Check for color selection keys
                if event.key == pygame.K_r: # switch to red
                    mode = 'red'
                elif event.key == pygame.K_g: # switch to green
                    mode = 'green'
                elif event.key == pygame.K_b: # switch to blue
                    mode = 'blue'
                elif event.key == pygame.K_e: # Eraser mode
                    mode = 'eraser'
                elif event.key == pygame.K_c: # Circle mode
                    shape = 'circle'
                elif event.key == pygame.K_l: # Line  mode
                    shape = 'line'
                elif event.key == pygame.K_t: # Rectangle mode
                    shape = 'rectangle'
                # Add following tasks: Draw square, right triangle, equilateral triangle, rhombus
                elif event.key == pygame.K_s: # Square mode
                    shape = 'square'
                elif event.key == pygame.K_p: # Right triangle mode
                    shape = 'right_triangle'
                elif event.key == pygame.K_q: # Equilateral triangle mode
                    shape = 'equilateral_triangle'
                elif event.key == pygame.K_h: # Rhombus mode
                    shape = 'rhombus'
            
            # Check for mouse button input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click to increase radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # Right click to decrease radius
                    radius = max(1, radius - 1)
            
            # Check for mouse motion
            if event.type == pygame.MOUSEMOTION:
                # Add the current mouse position to the points list
                position = event.pos
                points = points + [position]
                
        screen.fill((0, 0, 0))
        
        # Draw all points based on the selected shape and mode
        i = 0
        while i < len(points) - 1:
            if shape == 'line':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif shape == 'circle':
                drawCircle(screen, points[i], radius, mode)
            elif shape == 'rectangle':
                drawRectangle(screen, points[i], points[i + 1], radius, mode)
            elif shape == 'square':
                drawSquare(screen, points[i], radius, mode)
            elif shape == 'right_triangle':
                drawRightTriangle(screen, points[i], points[i + 1], radius, mode)
            elif shape == 'equilateral_triangle':
                drawEquilateralTriangle(screen, points[i], points[i + 1], radius, mode)
            elif shape == 'rhombus':
                drawRhombus(screen, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
 
        clock.tick(60)

# Function to draw a line between two points
def drawLineBetween(screen, index, start, end, width, color_mode):
    # Calculate colors based on its index and color
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue': # Set color to blue
        color = (c1, c1, c2)
    elif color_mode == 'red': # Set color to red
        color = (c2, c1, c1)
    elif color_mode == 'green': # Set color to green
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)  # Set color to white for eraser
    
    # Calculate the number of iterations for drawing the line
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    # Draw the line
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Function to draw a circle
def drawCircle(screen, center, radius, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.circle(screen, color, center, radius)

# Function to draw a rectangle
def drawRectangle(screen, start, end, width, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.rect(screen, color, (start[0], start[1], end[0] - start[0], end[1] - start[1]), width)

# Function to draw a square
def drawSquare(screen, start, side_length, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.rect(screen, color, (start[0], start[1], side_length, side_length))

# Function to draw a right triangle
def drawRightTriangle(screen, start, end, width, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.polygon(screen, color, [(start[0], start[1]), (start[0], end[1]), (end[0], end[1])], width)

# Function to draw an equilateral triangle
def drawEquilateralTriangle(screen, start, end, width, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.polygon(screen, color, [(start[0], end[1]), ((start[0] + end[0]) / 2, start[1]), (end[0], end[1])], width)

# Function to draw a rhombus
def drawRhombus(screen, start, end, width, color_mode):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        if color_mode == 'blue':
            color = (0, 0, 255)
        elif color_mode == 'red':
            color = (255, 0, 0)
        elif color_mode == 'green':
            color = (0, 255, 0)
    pygame.draw.polygon(screen, color, [((start[0] + end[0]) / 2, start[1]), (end[0], (start[1] + end[1]) / 2), ((start[0] + end[0]) / 2, end[1]), (start[0], (start[1] + end[1]) / 2)], width)

main()