# 사용자 정의 모듈 읽기 1
print('경로지정 방법1 → import 패키지명.모듈명')
import moduleTest01.mymod1

print(dir(moduleTest01.mymod1))     # 정의된 멤버 목록 확인

print('\nmymod1의 함수 호출 ---')
list1=[1,3]
list2=[1,2]
moduleTest01.mymod1.listhap(list1, list2)
print('다른 모듈의 전역변수 읽기 tot: ', moduleTest01.mymod1.tot)

print('\n경로지정 방법2 → from 패키지명 import 모듈명')
from moduleTest01 import mymod1
mymod1.kbs()
print('다른 모듈의 전역변수 읽기 tot: ', mymod1.tot)

print('\n경로지정 방법3 → from 패키지명.모듈명 import 함수명, 변수')
from moduleTest01.mymod1 import mbc
mbc()   # 함수명만 적어도 호출 가능