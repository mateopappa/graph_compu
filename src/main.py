from window import Window
from shader_program import ShaderProgram
from cube import Cube
from sphere import Sphere
from camera import Camera
from scene import Scene


#VENTANA
window = Window(800, 600, "Motor grafico basico de mateo")

#shader
shader_program = ShaderProgram(window.ctx, "shaders/basic.vert", "shaders/basic.frag")

#camara
camera = Camera((0,0,6),(0,0,0),(0,1,0), 45, window.width/window.height, 0.1, 100)
cube1 = Cube((-2,0,0), (0,45,45), (1,1,1), name="cube1")
cube2 = Cube((2,0,0), (0,45,0), (1,1,1,), name="cube2")
#sphere1 = Sphere((0,0,0), (0,0,0), (1,1,1), name="sphere1")

# Rotar ambos cubos 45 grados en el eje Y
cube1 = Cube((-2,0,0), (0,45,45), (1,1,1), name="cube1")
cube2 = Cube((2,0,0), (0,45,0), (1,1,1), name="cube2")

#objetos
cube1 = Cube((-2, 0, 0), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 0), (0, 45, 0), (1, 0.5, 1), name="Cube2")

#escena

scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader_program)
scene.add_object(cube2, shader_program)
#scene.add_object(sphere1, shader_program)

#carga de la escena y loop principal
window.set_scene(scene)
window.run()