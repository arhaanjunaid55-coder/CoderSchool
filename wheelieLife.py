import pygame
import random
import math

# ======================
# SETTINGS
# ======================

WIDTH = 1000
HEIGHT = 600
GROUND_Y = HEIGHT - 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Wheelie Life - Pygame Edition")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)

# ======================
# GAME CLASS
# ======================

class WheelieGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.angle = 0
        self.angular_velocity = 0
        self.speed = 0
        self.fuel = 100
        self.score = 0
        self.combo = 0
        self.alive = True
        self.bg_offset = 0
        self.road_offset = 0
        self.wheel_rotation = 0
        self.traffic = []
        self.spawn_timer = 0

        self.buildings = [random.randint(80, 220) for _ in range(20)]

    # ======================
    # UPDATE
    # ======================

    def update(self, keys):

        if not self.alive:
            return

        # Throttle
        if keys[pygame.K_d] and self.fuel > 0:
            self.speed += 0.3
            self.fuel -= 0.2

        # Brake
        if keys[pygame.K_a]:
            self.speed -= 0.5

        # Clamp speed
        self.speed = max(0, min(self.speed, 20))
        self.speed *= 0.985

        # Lean back
        if keys[pygame.K_w]:
            self.angular_velocity += 0.7

        # Lean forward
        if keys[pygame.K_s]:
            self.angular_velocity -= 0.7

        # Gravity + instability
        self.angular_velocity -= 0.3
        self.angular_velocity -= self.speed * 0.02

        self.angular_velocity *= 0.95
        self.angle += self.angular_velocity

        # Crash detection
        if self.angle > 80:
            self.alive = False
            self.crash = "LOOP OUT"

        if self.angle < -25:
            self.alive = False
            self.crash = "FRONT SLAM"

        # Score
        self.score += self.speed

        # Wheel rotation
        self.wheel_rotation += self.speed * 0.3

        # Background movement
        self.bg_offset += self.speed * 0.5
        self.road_offset += self.speed * 6

        # Traffic
        self.spawn_timer += 1
        if self.spawn_timer > 120:
            self.spawn_timer = 0
            self.traffic.append(WIDTH + 100)

        self.traffic = [x - self.speed * 2 for x in self.traffic]

        for car in self.traffic:
            if abs(car - WIDTH//2) < 40 and self.angle < 15:
                self.alive = False
                self.crash = "HIT TRAFFIC"

    # ======================
    # DRAW
    # ======================

    def draw(self):

        # SKY
        screen.fill((10, 10, 40))

        # BUILDINGS
        for i, height in enumerate(self.buildings):
            x = (i * 200 - self.bg_offset) % (WIDTH + 200)
            pygame.draw.rect(screen, (30, 30, 80),
                             (x, GROUND_Y - height, 120, height))

        # ROAD
        pygame.draw.rect(screen, (40, 40, 40),
                         (0, GROUND_Y, WIDTH, HEIGHT))

        # ROAD STRIPES
        for i in range(20):
            stripe_x = (i * 150 - self.road_offset) % (WIDTH + 150)
            pygame.draw.rect(screen, (255, 255, 255),
                             (stripe_x, GROUND_Y + 30, 60, 10))

        # TRAFFIC
        for car in self.traffic:
            pygame.draw.rect(screen, (200, 0, 0),
                             (car - 30, GROUND_Y - 30, 60, 30))

        # BIKE
        rear_x = WIDTH // 2
        rear_y = GROUND_Y

        bike_length = 120
        angle_rad = math.radians(self.angle)

        front_x = rear_x + bike_length * math.cos(angle_rad)
        front_y = rear_y - bike_length * math.sin(angle_rad)

        # Wheels
        self.draw_wheel(rear_x, rear_y, 25)
        self.draw_wheel(front_x, front_y, 25)

        # Frame
        pygame.draw.line(screen, (0, 255, 0),
                         (rear_x, rear_y),
                         (front_x, front_y), 6)

        # Rider
        self.draw_rider(rear_x, rear_y, angle_rad)

        # HUD
        screen.blit(font.render(f"Speed: {round(self.speed,1)}", True, (255,255,255)), (20,20))
        screen.blit(font.render(f"Fuel: {int(self.fuel)}", True, (255,255,255)), (20,50))
        screen.blit(font.render(f"Score: {int(self.score)}", True, (255,255,255)), (20,80))

        if not self.alive:
            crash_text = font.render(self.crash + " - Press R", True, (255,0,0))
            screen.blit(crash_text, (WIDTH//2 - 150, HEIGHT//2))

    def draw_wheel(self, x, y, r):
        pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), r, 2)

        for i in range(4):
            angle = self.wheel_rotation + i * math.pi/2
            spoke_x = x + r * math.cos(angle)
            spoke_y = y + r * math.sin(angle)
            pygame.draw.line(screen, (255,255,255),
                             (x, y),
                             (spoke_x, spoke_y), 2)

    def draw_rider(self, rear_x, rear_y, angle_rad):

        bike_length = 120
        seat_x = rear_x + (bike_length * 0.4) * math.cos(angle_rad)
        seat_y = rear_y - (bike_length * 0.4) * math.sin(angle_rad)

        torso_length = 40

        shoulder_x = seat_x - torso_length * math.sin(angle_rad)
        shoulder_y = seat_y - torso_length * math.cos(angle_rad)

        head_x = shoulder_x - 15 * math.sin(angle_rad)
        head_y = shoulder_y - 15 * math.cos(angle_rad)

        pygame.draw.circle(screen, (255,180,100),
                           (int(head_x), int(head_y)), 10)

        pygame.draw.line(screen, (0,0,255),
                         (seat_x, seat_y),
                         (shoulder_x, shoulder_y), 6)

# ======================
# MAIN LOOP
# ======================

game = WheelieGame()
running = True

while running:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not game.alive:
                game.reset()

    game.update(keys)
    game.draw()

    pygame.display.flip()

pygame.quit()
