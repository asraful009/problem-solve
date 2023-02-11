
#include <iostream>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

static unsigned int complieShader(unsigned int type, const std::string &source) {
    unsigned int shaderIndex = glCreateShader(type);
    const char *src = source.c_str();
    glShaderSource(shaderIndex, 1, &src, nullptr);
    glCompileShader(shaderIndex);

    int complierStatus;
    glGetShaderiv(shaderIndex, GL_COMPILE_STATUS, &complierStatus);
    if(complierStatus == GL_FALSE) {
        int errLogLength;
        glGetShaderiv(shaderIndex, GL_INFO_LOG_LENGTH, &errLogLength);
        char *errMsg = (char *) alloca(errLogLength * sizeof(char));
        glGetShaderInfoLog(shaderIndex, errLogLength, & errLogLength, errMsg);
        std::cout
            << "ShaderCompiler Err [ " 
            << (type == GL_VERTEX_SHADER ? "GL_VERTEX_SHADER": "GL_FRAGMENT_SHADER") << " ]: "
            << errMsg<< std::endl;
        glDeleteShader(shaderIndex);
        return 0;
    }

    return shaderIndex;
}

static unsigned int createShader(const std::string &vertexShader, const std::string &fragmentShader) {
    unsigned int programIndex = glCreateProgram();
    unsigned int vertexShaderIndex = complieShader(GL_VERTEX_SHADER, vertexShader);
    unsigned int fragmentShaderIndex = complieShader(GL_FRAGMENT_SHADER, fragmentShader);

    glAttachShader(programIndex, vertexShaderIndex);
    glAttachShader(programIndex, fragmentShaderIndex);
    glLinkProgram(programIndex);
    glValidateProgram(programIndex);

    glDeleteShader(vertexShaderIndex);
    glDeleteShader(fragmentShaderIndex);

    return programIndex;
}

int main() {
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

    unsigned int err = glewInit();
    if(err != GLEW_OK) std::cout<< glewGetErrorString(err)<<std::endl;
    std::cout<< "GLEW_VERSION :" <<glewGetString(GLEW_VERSION) << std::endl;

    GLfloat trianglePointsArray[6] = {
        -0.5f, -0.5f,
         0.0f,  0.5f,
         0.5f, -0.5f
    };

    unsigned int vertexBufferIndex;
    glGenBuffers(1, &vertexBufferIndex);
    std::cout<< "vertexBufferIndex : " << vertexBufferIndex << std::endl;

    glBindBuffer(GL_ARRAY_BUFFER, vertexBufferIndex);
    glBufferData(GL_ARRAY_BUFFER, 6* sizeof(GLfloat), trianglePointsArray, GL_STATIC_DRAW);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(GLfloat)*2, 0);
    

    std::string vertexShader = 
        "#version 330 core\n"
        "\n"
        "layout(location = 0) in vec4 trianglePointsArrayPosition;\n"
        "\n"
        "void main() {\n"
        "   gl_Position = trianglePointsArrayPosition;\n"
        "}"
        ;
    std::string fragmentShader = 
        "#version 330 core\n"
        "\n"
        "layout(location = 0) out vec4 color;\n"
        "\n"
        "void main() {\n"
        "   color = vec4(0.0, 0.678, 0.709, 1.0);\n"
        "}"
        ;

    unsigned int shaderProgramIndex = createShader(vertexShader, fragmentShader);
    std::cout<<"shaderProgramIndex: " <<shaderProgramIndex<<std::endl;
    glUseProgram(shaderProgramIndex);
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