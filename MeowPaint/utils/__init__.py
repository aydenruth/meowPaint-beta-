#makes utils treated like a package... so u can import it 2 main which why wouldn't it already python devs? hm?
# init is our initialization script

from .settings import * #dot bc rel import; import smth within same package(folder)
from .button import Button
import pygame
pygame.init()
pygame.font.init()

