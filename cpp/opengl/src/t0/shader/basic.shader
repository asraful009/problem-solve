#shader vertex
#version 330 core

layout(location = 0) in vec4 trianglePointsArrayPosition;

void main() {
    gl_Position = trianglePointsArrayPosition;
}
#end_shader
#shader fragment
#version 330 core

layout(location = 0) out vec4 color;

void main() {
    color = vec4(0.062, 0.058, 0.058, 1.0);
}
#end_shader