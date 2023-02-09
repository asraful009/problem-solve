
#include <math.h>
#include <GL/glut.h>

#define pi 3.142857
#define size .4
#define srof3 1.73205080757
#define gridN 20

void init() {
  glClearColor(0.0, 0.0, 0.0, 0.0);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glOrtho(0.0, 10.0, 0.0, 10.0, -10.0, 10.0);
}

void drawGridPoint() {
  float x = 0, y = 0;
  for(int i=1; i<=gridN; i++) {
    for(int j=1; j<=gridN; j++) {
      x = srof3 * size * i;
      y = 1.5 * size * j;
      glBegin(GL_POINTS);
      glColor3f(0.969f, 0.984f, 0.988f);
        glVertex3f(x, y, 0.0f);
      glEnd();
    }
  }
}

void drawGridLine() {
  float x = 0, y = 0;
  //draw vertical line
  y = gridN * 1.5 * size;
  glColor3f(0.741, 0.824, 0.714);
  for(int i=1; i<=gridN; i++) {
      x = srof3 * size * i;
      glBegin(GL_LINES);
        glVertex3f(x, 0, 0.0f);
        glVertex3f(x, y, 0.0f);
      glEnd();
  }
  // draw hoizontal line
  x = srof3 * size * gridN;
  glColor3f(0.741, 0.824, 0.714);
  for(int j=1; j<=gridN; j++) {
    y = 1.5 * size * j;
    glBegin(GL_LINES);
      glVertex3f(0, y, 0.0f);
      glVertex3f(x, y, 0.0f);
    glEnd();
  }
}

void display(void) {
  
  glClear(GL_COLOR_BUFFER_BIT);
  drawGridPoint();
  drawGridLine();
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