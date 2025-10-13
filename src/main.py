from window import Window
from shader_program import ShaderProgram
from cube import Cube
from sphere import Sphere
from camera import Camera
from scene import Scene



window = Window(800, 600, "Motorcito de Marcos y Mateo")
shader_program = ShaderProgram(window.ctx, 'shaders/basic.vert', 'shaders/basic.frag')
cube1 = Cube(position=(-2, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), name="Cube1")
cube2 = Cube(position=(2, 0, 0), rotation=(0, 45, 0), scale=(1, 0.5, 1), name="Cube2")
camera = Camera((0, 0, 6), (0, 0, 0), (0, 1, 0), 45, window.width / window.height, 0.1, 100.0)
scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader_program)
scene.add_object(cube2, shader_program)
window.set_scene(scene)

window.run()

