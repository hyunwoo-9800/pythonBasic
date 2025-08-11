# 딕셔너리 자료형의 매핑
def func(w, h, **other):  # other는 딕셔너리 형 자료와 매핑
    print('몸무게 {}, 키 {}'.format(w, h))
    print(other)


func(65, 175, irum='지구인', nai=23)  # 변수 = 값은 **변수에 매핑
func(w=75, h=185, irum='한국인')  # w와 h는 이름으로 매핑


# 함수의 매개변수에 인수를 전달할 때 *, ** 혼합도 가능
def functotal(a, b, *v1, **v2):
    print(a, b)
    print(v1)
    print(v2)


functotal(1, 2)                          # 매개변수 v1, v2는 매핑값이 없다.

functotal(1, 2, 3, 4, 5)            # 매개변수 v2는 매핑값이 없다.

functotal(1, 2, 3, 4, 5, m=6, n=7)  # 모든 매개변수에 매핑
