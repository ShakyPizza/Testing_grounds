import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ELEVATOR_WIDTH = 50
ELEVATOR_HEIGHT = 40
NUM_FLOORS = 10
NUM_ELEVATORS = 4
FLOOR_HEIGHT = SCREEN_HEIGHT // NUM_FLOORS

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Elevator class
class Elevator:
    def __init__(self, id, x_pos):
        self.id = id
        self.current_floor = random.randint(0, NUM_FLOORS - 1)
        self.target_floor = self.current_floor
        self.y_pos = SCREEN_HEIGHT - ((self.current_floor + 1) * FLOOR_HEIGHT)
        self.x_pos = x_pos
        self.moving = False

    def move(self):
        if self.moving:
            if self.current_floor < self.target_floor:
                self.y_pos -= 1
                if self.y_pos <= SCREEN_HEIGHT - ((self.target_floor + 1) * FLOOR_HEIGHT):
                    self.current_floor = self.target_floor
                    self.moving = False
            elif self.current_floor > self.target_floor:
                self.y_pos += 1
                if self.y_pos >= SCREEN_HEIGHT - ((self.target_floor + 1) * FLOOR_HEIGHT):
                    self.current_floor = self.target_floor
                    self.moving = False

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x_pos, self.y_pos, ELEVATOR_WIDTH, ELEVATOR_HEIGHT))

    def call_elevator(self, floor):
        self.target_floor = floor
        self.moving = True

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elevator Simulation")

# Create elevators
elevators = [Elevator(i, i * (SCREEN_WIDTH // NUM_ELEVATORS)) for i in range(NUM_ELEVATORS)]

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw floors
    for i in range(NUM_FLOORS):
        floor_y = SCREEN_HEIGHT - (i + 1) * FLOOR_HEIGHT
        pygame.draw.line(screen, GRAY, (0, floor_y), (SCREEN_WIDTH, floor_y), 2)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                elevators[0].call_elevator(random.randint(0, NUM_FLOORS - 1))
            if event.key == pygame.K_2:
                elevators[1].call_elevator(random.randint(0, NUM_FLOORS - 1))
            if event.key == pygame.K_3:
                elevators[2].call_elevator(random.randint(0, NUM_FLOORS - 1))
            if event.key == pygame.K_4:
                elevators[3].call_elevator(random.randint(0, NUM_FLOORS - 1))

    # Update and draw elevators
    for elevator in elevators:
        elevator.move()
        elevator.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Frame rate
    pygame.time.delay(50)

pygame.quit()