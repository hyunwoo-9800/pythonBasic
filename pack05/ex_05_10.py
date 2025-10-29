# 가전 제품 클래스(부모)
class ElecProduct:
    volume = 0;
    
    # 소리 조절용
    def volumeControl(self, volume):
        pass

# TV클래스(자식)
class ElecTv(ElecProduct):
    
    # 오버라이드
    def volumeControl(self, volume):
        self.volume += volume
        print("TV의 소리 크기 : ", self.volume)
        print()

# 라디오클래스(자식)
class ElecRadio(ElecProduct):

    def showProduct(self):
        print("라디오 고유 메서드")
        
    # 오버라이드
    def volumeControl(self, volume):
        vol = volume
        self.volume += vol
        print("라디오의 소리 크기 : ", self.volume)
        print()

# TV 객체 생성
tv = ElecTv()
tv.volumeControl(5)
tv.volumeControl(-3)

# 라디오 객체 생성
radio = ElecRadio()
radio.volumeControl(7)
radio.showProduct()

# 다형성 처리
product = tv
product.volumeControl(3)
product = radio
product.volumeControl(3)