class Robot:

    # 생성자? 객체화 할때 호출되는 함수의 일종으로
    # 객체화가 될때 가장 먼저 호출된다.
    # self?
    def __init__(self):
        print('robot 이 복사될때 제일 먼저 호출되는 멤버')

    def doit(self):
        print('나는 robot 의 함수 입니다.')

robot = Robot()
robot.doit()

