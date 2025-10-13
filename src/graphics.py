class Graphics:
    def __init__(self, ctx, model, material):
        self._ctx = ctx
        self._model = model
        self._material = material

        self._vbo = self.create_buffers()
        self._ibo = ctx.buffer(model.indices.tobytes())
        self._vao = ctx.vertex_array(
            material.shader_program.prog, [*self._vbo], self._ibo
        )

        self._textures = self.load_textures(material.textures_data)

    def create_buffers(self):
        buffers = []
        shader_attributes = self._material.shader_program.attributes

        for attribute in self._model.vertex_layout.get_attributes():
            if attribute.name in shader_attributes:
                vbo = self._ctx.buffer(attribute.array.tobytes())
                buffers.append((vbo, attribute.format, attribute.name))

        return buffers

    def load_textures(self, textures_data):
        textures = []

        for texture in textures_data:
            if texture.image_data:
                texture_ctx = self._ctx.texture(
                    texture.size,
                    texture.channels_amount,
                    texture.image_data
                )

                if texture.build_mipmaps:
                    texture_ctx.build_mipmaps()

                texture_ctx.repeat_x = texture.repeat_x
                texture_ctx.repeat_y = texture.repeat_y

                textures.append((texture.name, texture_ctx))

        return textures

    def render(self, uniforms):
        # Actualizar uniforms dinámicos
        for name, value in uniforms.items():
            if name in self._material.shader_program.prog:
                self._material.set_uniform(name, value)

        # Vincular texturas
        for i, (name, texture_ctx) in enumerate(self._textures):
            texture_ctx.use(i)
            self._material.shader_program.set_uniform(name, i)

        # Dibujar VAO
        self._vao.render()
