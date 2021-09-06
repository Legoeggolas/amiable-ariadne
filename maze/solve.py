import threading
from .draw import DrawBuffer
from PIL import Image
from .process import MazeProcessor
import pygame
from math import floor
from pathfinder.interface import Pathfinder


class MazeSolver:

    def __init__(self, image: Image, maze: list) -> None:
        self.image = image
        self.pathfinder = Pathfinder()
        self.mp = MazeProcessor(maze)

    # Will run as a thread
    def solve(self, method, buffer: DrawBuffer):
        #sleep(0.5)
        path = method(self.mp.start, self.mp.end, buffer, (0, 122, 122))

        r = len(path)
        r = 255 / r

        tail = path[0]
        for i in range(1, len(path)):
            buffer.push(tail, path[i], (floor(r * i), floor((r * i) / 2), 255 - floor(
                (r * i) / 1.5)))
            tail = path[i]

    def render(self, MAZE_SIZE: tuple, rate=1000):
        pathfinder = self.pathfinder.pick()
        pygame.init()
        clock = pygame.time.Clock()

        # Upscale the image to a higher resolution for better visibility
        # This serves mostly as a magnification
        # Since mazes are drawn from bitmaps, and entities (walls and paths) are 1px squares
        # The best results can be obtained by upscaling by a power of two
        # This makes each entity get evenly thicker
        upscale_size = list(MAZE_SIZE)
        upscale_ratio = 1
        while floor(MAZE_SIZE[0] * upscale_ratio) <= 1500 and floor(
                MAZE_SIZE[1] * upscale_ratio) <= 780:
            upscale_size[0] = floor(MAZE_SIZE[0] * upscale_ratio)
            upscale_size[1] = floor(MAZE_SIZE[1] * upscale_ratio)
            upscale_ratio *= 2
        upscale_size = tuple(upscale_size)

        print(f"Original image {MAZE_SIZE} upscaled to {upscale_size}")
        screen = pygame.display.set_mode(upscale_size)

        # Initialize the Draw Buffer
        img_data = self.image.load()
        buffer = DrawBuffer(img_data)

        # Start the pathfinding algorithm
        solver = threading.Thread(target=self.solve, args=(pathfinder, buffer))
        solver.run()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return

            # Draw a path on the current frame
            buffer.draw()

            # Convert the image to a PyGame image and upscale it to fit the screen size
            frame = pygame.image.fromstring(self.image.tobytes("raw", 'RGB'), MAZE_SIZE, 'RGB')
            frame = pygame.transform.scale(frame, upscale_size)

            screen.fill((0, 0, 0))
            screen.blit(frame, frame.get_rect())
            pygame.display.flip()
            clock.tick(rate)

            if not solver.is_alive() and buffer.empty():
                print("Maze solved")
                pygame.time.wait(3000)
                pygame.quit()
                pygame.display.quit()
                return
