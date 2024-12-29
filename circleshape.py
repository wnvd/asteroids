import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    

    def draw():     
        pass


    def update():
        pass


    def collision_detection(self, entity):
        check_distance = pygame.Vector2.distance_to(self.position, entity.position)
        dist = self.radius + entity.radius
        if check_distance <= dist:
            return True
        return False

