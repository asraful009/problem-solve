
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include "vertex_op.hpp"

struct ShaderProgramSource {
    std::string vertexSource;
    std::string fragmentSource;
};

static ShaderProgramSource loadShaderProgram(const std::string &filePath) {
    enum class ESHADER_TYPE {
        NONE = -1, VERTEX = 0, FRAGMENT = 1
    };
    std::ifstream stream(filePath);
    std::string line;
    ESHADER_TYPE shaderTypeMode = ESHADER_TYPE::NONE;
    std::stringstream ss[2];

    int lineIndex = 1;
    // std::cout << "load Shader Source Code ..."<<std::endl;
    while (getline(stream, line)) {
        // std::cout
        // << lineIndex++ 
        // <<  "\t [ " 
        //     << ( shaderTypeMode ==ESHADER_TYPE::VERTEX ? "VERTEX" 
        //         : shaderTypeMode == ESHADER_TYPE::FRAGMENT ? "FRAGMENT" 
        //         : shaderTypeMode == ESHADER_TYPE::NONE ? "NONE" : "UNKNOWN" 
        //     )
        //     << " ]: " 
        // << line << std::endl;
        if(line.find("#shader") != std::string::npos) {
            if(line.find("vertex") != std::string::npos) {
                shaderTypeMode = ESHADER_TYPE::VERTEX;
            } else if(line.find("fragment") != std::string::npos) {
                shaderTypeMode = ESHADER_TYPE::FRAGMENT;
            }
        } else if(line.find("#end_shader") != std::string::npos) {
            shaderTypeMode = ESHADER_TYPE::NONE;
        } else {
            if(shaderTypeMode == ESHADER_TYPE::VERTEX) {
                ss[0] << line << "\n";
            } else if(shaderTypeMode == ESHADER_TYPE::FRAGMENT) {
                ss[1] << line << "\n";
            }
        }
    }
    std::cout << "Shader Source Code loaded"<<std::endl;
    return { ss[0].str(), ss[1].str() };
}

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

int init(const std::string wTitle, const std::vector<Vertex*>& vertices, GLenum glEnum) {
    GLFWwindow* window;

    /* Initialize the library */
    if (!glfwInit())
        return -1;

    
    window = glfwCreateWindow(640, 480, wTitle.c_str(), NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }
    
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1);

    std::cout<< "GL_VERSION :" << glGetString(GL_VERSION)<< std::endl;
    std::cout<< "GL_RENDERER :" << glGetString(GL_RENDERER)<< std::endl;

    unsigned int err = glewInit();
    if(err != GLEW_OK) std::cout<< glewGetErrorString(err)<<std::endl;
    std::cout<< "GLEW_VERSION :" <<glewGetString(GLEW_VERSION) << std::endl;

    float trianglePointsArray[] = {
        -0.5f, -0.5f,
         0.5f, -0.5f,
         0.5f,  0.5f,
        -0.5f,  0.5f
    };

    unsigned int indeies [] = {
        0, 1, 2,
        0, 3, 2,
    };

    unsigned int vertexBufferIndex;
    glGenBuffers(1, &vertexBufferIndex);
    glBindBuffer(GL_ARRAY_BUFFER, vertexBufferIndex);
    glBufferData(GL_ARRAY_BUFFER, 2 * 6 * sizeof(float), trianglePointsArray, GL_STATIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(float)*2, 0);

    unsigned int indeiesBufferIndex;
    glGenBuffers(1, &indeiesBufferIndex);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indeiesBufferIndex);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 2 * 3 * sizeof(unsigned int), indeies, GL_STATIC_DRAW);
    
    ShaderProgramSource shaderProgramSource = 
        loadShaderProgram("shader/basic.shader");
    // std::cout<< "++++++++++++++++ Vertex   Source ++++++++++++++\n" << shaderProgramSource.vertexSource<<std::endl;
    // std::cout<< "++++++++++++++++ Fragment Source ++++++++++++++\n" << shaderProgramSource.fragmentSource<<std::endl;

    unsigned int shaderProgramIndex = 
        createShader(shaderProgramSource.vertexSource, shaderProgramSource.fragmentSource);
    std::cout<<"shaderProgramIndex: " <<shaderProgramIndex<<std::endl;
    glUseProgram(shaderProgramIndex);
    
    float r = 0.223, incrementalRate = 0.05f;
    unsigned int colorUniformIndex = glGetUniformLocation(shaderProgramIndex, "u_Color");
    if(colorUniformIndex != -1) 
        glUniform4f(colorUniformIndex, r, 0.356, 0.392, 1.0);

    while (!glfwWindowShouldClose(window)) {
        glUniform4f(colorUniformIndex, r, 0.356, 0.392, 1.0);
        if(r > 1.0f) incrementalRate = -0.05f;
        else if(r < 0.0f) incrementalRate = 0.05f;
        
        r+= incrementalRate;

        glDrawElements(GL_POINT, 6, GL_UNSIGNED_INT, nullptr);
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glDeleteProgram(shaderProgramIndex);
    glfwTerminate();
    return 0;
}