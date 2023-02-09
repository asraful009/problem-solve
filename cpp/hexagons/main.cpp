
#include <math.h>
#include <GL/glut.h>

#define pi 3.142857
#define pointSize 5.5
#define lineSize 0.2
#define size .4
#define srof3 1.73205080757
#define gridN 12

void init() {
  glClearColor(0.961, 0.961, 0.961, 0.0);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glOrtho(0.0, 10.0, 0.0, 10.0, -10.0, 10.0);
}

void drawGridPoint() {
  float x = 0, y = 0;
  glColor3f(0.231, 0.204, 0.525);
  glPointSize(pointSize);
  for(int i=1; i<=gridN; i++) {
    for(int j=1; j<=gridN; j++) {
      x = srof3 * size * i;
      y = 1.5 * size * j;
      glBegin(GL_POINTS);
        glVertex3f(x, y, 0.0f);
      glEnd();
    }
  }
}

void drawGridLine() {
  float x = 0, y = 0;
  //draw vertical line
  y = 1.5 * size * (gridN);
  glColor3f(0.741, 0.824, 0.714);
  for(int i=1; i<= gridN; i++) {
      x = srof3 * size * i;
      glBegin(GL_LINES);
        glVertex3f(x, 1.5 * size, 0.0f);
        glVertex3f(x, y, 0.0f);
      glEnd();
  }
  // draw hoizontal line
  x = srof3 * size * (gridN);
  glColor3f(0.741, 0.824, 0.714);
  for(int j=1; j<= gridN; j++) {
    y = 1.5 * size * j;
    glBegin(GL_LINES);
      glVertex3f(srof3 * size, y, 0.0f);
      glVertex3f(x, y, 0.0f);
    glEnd();
  }
}

void display(void) {
  
  glClear(GL_COLOR_BUFFER_BIT);
  drawGridLine();
  drawGridPoint();
  glutSwapBuffers();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
  glutInitWindowSize(800, 800);
  glutInitWindowPosition(400, 400);
  glutCreateWindow("Hello world!");
  init();
  glutDisplayFunc(display);
  glutMainLoop();
  return 0;
}