from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
import sys

def drawAxes():  ## 축을 그리는 함수
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()

class MyGLWindow(QOpenGLWidget):
    def __init__(self): # 생성자
        super().__init__()
        self.setWindowTitle('glortho 연습')

    def initializeGL(self) :
        pass

    def resizeGL(self, w:int, h:int):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        range = 2
        aspR = w/h              #종횡비 알아볼것
        glOrtho(-range*aspR, range*aspR, -range, range, -range, range)

    def paintGL(self):
        glBegin(GL_POLYGON)
        glVertex3f(1,0,0)
        glVertex3f(0,1,0)
        glVertex3f(-1,0,0)
        glVertex3f(0,-1,0)
        glEnd()
        drawAxes()

def main(argv = sys.argv):
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()

    app.exec()

if __name__ == '__main__':
    main(sys.argv)