
# GL과 GLU는 그래픽스 라이브러리로 
# GL은 저수준 기본렌더링 함수들을
# GLU는 원뿔, 구등을 렌더링, 특수용도의 변환과 행렬등을 지원한다
from OpenGL.GL import *
from OpenGL.GLU import *



# PyQt는 그래픽 유저 인터페이스를 제공하는 라이브러리
# widget은 UI,화면(사용자 인터페이스)를 구성하는 핵심요소 간단한거는 이녀석이 하지만
# QtOpenGLWidgets은 더 어려운 그래픽을 처리하는데 사용됨
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

#파이썬 인터프리터를 제어하는 기본모듈
import sys
import math
### 나의 첫번째 오픈지엘 윈도우

class MyGLWindow(QWidget) :
    def __init__(self):
        super().__init__()

    #### 다음 세 기본 콜백은 이름을 바꿀 수 없다.
    def initializeGL(self):
        glClearColor(0.0, 1.0, 1.0, 1.0)

    def resizeGL(self, w, h):
        pass

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON)
        
        #원그리기
        for i in range(0,360,5):
            angle = 2*3.141592*i/360.0
            glVertex2f(math.cos(angle),math.sin(angle))
 
        glEnd()



def main(argv = []):        
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main(sys.argv)      #argv는 프로그램 이름을 포함한 명령행 인자 리스트를 반환함
                        #첫번째 요소가 이름 이후 요소부터가 명령행줄임