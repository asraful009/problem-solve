
#include <iostream>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

int main()
{
    GLFWwindow* window;

    /* Initialize the library */
    if (!glfwInit())
        return -1;

    
    window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }
    
    glfwMakeContextCurrent(window);

    std::cout<< "GL_VERSION :" << glGetString(GL_VERSION)<< std::endl;
    std::cout<< "GL_RENDERER :" << glGetString(GL_RENDERER)<< std::endl;

    GLenum err = glewInit();
    if(err != GLEW_OK) std::cout<< glewGetErrorString(err)<<std::endl;
    std::cout<< "GLEW_VERSION :" <<glewGetString(GLEW_VERSION) << std::endl;

    GLfloat trianglePointsArray[6] = {
        -0.5f, -0.5f,
         0.0f,  0.5f,
         0.5f, -0.5f
    };

    GLuint vertexBufferIndex;
    glGenBuffers(1, &vertexBufferIndex);
    glBindBuffer(GL_ARRAY_BUFFER, vertexBufferIndex);
    glBufferData(GL_ARRAY_BUFFER, 6* sizeof(GLfloat), trianglePointsArray, GL_STATIC_DRAW);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(GLfloat)*2, 0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    std::cout<< "vertexBufferIndex : " << vertexBufferIndex << std::endl;

    /* Loop until the user closes the window */
    while (!glfwWindowShouldClose(window)) {
        /* Render here */
        glDrawArrays(GL_TRIANGLES, 0, 3);
        /* Swap front and back buffers */
        glfwSwapBuffers(window);

        /* Poll for and process events */
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}