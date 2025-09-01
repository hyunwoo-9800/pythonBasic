# 내장된 모듈 읽기

print('뭔가를 하다가... 모듈 사용하기\n')

import sys                                                      # sys 모듈의 멤버를 사용할 수 있게 된다.
print('모듈 경로: ', sys.path, '\n')

# 수학 함수 읽기
import math
print('pi 값은? ', math.pi)
print('sin(30) 값은? ', math.sin(math.radians(30)), '\n')

# 달력 출력하기
import calendar
calendar.setfirstweekday(6)                                     # 일요일을 첫 요일로 설정
calendar.prmonth(2025,9)                       # 출력 날짜 설정
del calendar                                                    # calendar 객체 삭제

#작업 경로 관련 정보 읽기
import os
print('현재 작업 경로는?', os.getcwd())
print('root 내 파일목록은? ', os.listdir('/'))
