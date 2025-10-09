import numpy as np
import glm

class Sphere:
    def __init__(self, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), name="sphere", sectors=24, stacks=16):
        self.name = name
        self.position = glm.vec3(*position)
        self.rotation = glm.vec3(*rotation)
        self.scale = glm.vec3(*scale)
        self.sectors = sectors
        self.stacks = stacks
        self.vertices, self.indices = self.create_sphere()

    def create_sphere(self):
        vertices = []
        indices = []
        pi = np.pi
        for i in range(self.stacks + 1):
            stack_angle = pi / 2 - i * pi / self.stacks
            xy = np.cos(stack_angle)
            z = np.sin(stack_angle)
            for j in range(self.sectors + 1):
                sector_angle = j * 2 * pi / self.sectors
                x = xy * np.cos(sector_angle)
                y = xy * np.sin(sector_angle)
                # Color simple basado en la posición
                r = (x + 1) / 2
                g = (y + 1) / 2
                b = (z + 1) / 2
                vertices.append([x, y, z, r, g, b])
        for i in range(self.stacks):
            k1 = i * (self.sectors + 1)
            k2 = k1 + self.sectors + 1
            for j in range(self.sectors):
                if i != 0:
                    indices += [k1 + j, k2 + j, k1 + j + 1]
                if i != (self.stacks - 1):
                    indices += [k1 + j + 1, k2 + j, k2 + j + 1]
        return np.array(vertices, dtype='f4'), np.array(indices, dtype='i4')

    def get_model_matrix(self):
        model = glm.mat4(1)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, glm.radians(self.rotation.x), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.rotation.y), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.rotation.z), glm.vec3(0, 0, 1))
        model = glm.scale(model, self.scale)
        return model
