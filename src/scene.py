
from graphics import Graphics
import glm
import math

class Scene:
    def __init__(self, ctx, camera):
        self.ctx = ctx
        self.objects = []
        self.graphics = {}
        self.camera = camera
        self.model = glm.mat4(1)
        self.view = camera.get_view_matrix()
        self.projection = camera.get_perspective_matrix()
        self.time = 0.0

    def add_object(self, obj, shader_program=None):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
        self.time += 0.01

        # Obtener view y projection actuales de la cámara
        view = self.camera.get_view_matrix()
        projection = self.camera.get_perspective_matrix()
        for obj in self.objects:
            obj.rotation.x += 0.8
            obj.rotation.y += 0.6
            obj.rotation.z += 0.4
           # obj.position.x = math.sin(self.time) * 2
            model = obj.get_model_matrix()
            # MVP = Projection * View * Model
            mvp = projection * view * model
            # Enviar la matriz MVP al shader antes de renderizar
            self.graphics[obj.name].set_uniform('Mvp', mvp)
            self.graphics[obj.name].vao.render()

    def on_mouse_click(self, u, v):
        ray = self.camera.raycast(u, v)
        for obj in self.objects:
            if obj.check_hit(ray.origin, ray.direction):
                print(f"Golpeaste al objeto {obj.name}!")

    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.projection = glm.perspective(glm.radians(45), width / height, 0.1, 100.0)
