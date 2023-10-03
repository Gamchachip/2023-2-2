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
    
class MyGLwidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()

    def initializeGL(self) :
        pass
    
    def resizeGL(self,w,h):
        pass

    def paintGL(self) :
        pass
        

class MyWindow(QMainWindow) :
    def __init__(self, title = 'opengl'):
        super().__init__()
        self.setWindowTitle(title)

        ##GUI 정의
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        ## 중심 위짓이 가질 레이아웃 설정
        layout = QHBoxLayout()
        central_widget.setLayout(layout)


        # 두개 의 GL 위짓을 생성하고,
        # 이 두 위짓 객체를 각각 이 클래스의 멤버로 저장
        self.glwidget1 = MyGLwidget() #클래스의 멤버로 만드는 문법 다른 클래스에서 사용가능
        self.glwidget2 = MyGLwidget()

        layout.addWidget(self.glwidget1)
        layout.addWidget(self.glwidget2)


#두 위짓을 끼움
def main(argv = sys.argv):
    app = QApplication()
    window = MyWindowGL("Two open wigets")
    window.setFixedSize(1200,600)
    window.show()
    app.exec()


if __name__ == '__main__' :
    main(sys.argv)