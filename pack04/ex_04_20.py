# turtle로 도형 그리거
import turtle

def func():
    a = turtle.Pen()    # 그림을 그리기 위한 펜을 생성
    a.pendown()         # 도형 그리기를 위해 펜을 그림판에 내려놓는다.
    a.forward(100)      # 펜의 초기 방향은 오른쪽이며 앞으로 100px만큼 수평 이동하며 선을 그린다
    a.right(90)         # 시계 방향으로 90도 회전한다.
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)

    a.pencolor("blue")   # 선 색상을 변경
    a.circle(50, 360)   # 원을 그린다(반지름, 회전량)
    a.up()              # 펜을 들어 올린다.

    a.forward(100)
    a.pendown()

    a.write("문자 그리기", True, "left", font=("돋움", 24, "normal"))
    turtle.done()         # 그래픽 화면의 자동 종료 방지
    
# 메인 모듈 함수 호출
if __name__ == "__main__":
    func();