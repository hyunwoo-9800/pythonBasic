# 키보드를 통해 쉼표로 구분된 상품 자료를 입력받아 조건에 맞게 가공한 후 출력하는 예제
from openpyxl.styles.builtins import total


def inputfunc():
    datas = []                                      # 입력값을 저장할 리스트
    prices = {'새우깡' : 450, '감자깡' : 300}        # 단가 고정
    regions = {'100' : '강북', '200' : '강남'}      # 지역 고정

    while True:
        items = input('지역코드, 상품명, 수량 입력 (쉼표로 구분합니다.): ')
        parts = items.split(',')

        region_code = parts[0].strip()                   # 지역코드
        product = parts[1].strip()                       # 상품명
        qty = int(parts[2].strip())                      # 수량

        region = regions.get(region_code, '알 수 없음')   # 지역코드를 지역명으로 변환
        price = prices.get(product, 0)                   # 상품명으로 단가 계산
        total = qty * price                              # 총 금액

        datas.append([region, product, qty, price, total])

        cont = input('계속 할까요? [y/n]: ')
        if cont.lower() == 'n':     # N/n 모두 인식
            break

    return datas

def processfunc(data):
    # 머리글 출력
    print(f"{'지역':<6}{'상품명':<8}{'수량':<6}{'단가':<6}{'금액':<6}")
    
    # datas에 있는 리스트를 하나씩 꺼내 출력
    for d in data:
        print(f"{d[0]:<6}{d[1]:<8}{d[2]:<6}{d[3]:<6}{d[4]:<6}")

    # 총 건수 / 총액
    count = len(data)
    total_amount = sum(d[4] for d in data)

    print("-" * 40)
    print(f"총 건수: {count}건")
    print(f"총  금액: {total_amount}원")

# 실행
data = inputfunc()
processfunc(data)
