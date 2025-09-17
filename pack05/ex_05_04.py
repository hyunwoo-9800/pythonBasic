# 클래스로 자료형 생성

class Singer:
    title_song = "가시"

    def sing(self):
        msg = "노래는"
        print(msg, self.title_song, "제발 가라고\n")


boys = Singer()
print("타이틀 송은? ", Singer.title_song)
print("boys: ")
boys.sing()

girls = Singer()
print("girls: ")
girls.sing()

girls.title_song = "비도 오고 그래서"
girls.sing()
girls.co = "FM"
print("소속사: " + girls.co)

print(Singer.title_song)
Singer.title_song = "나에게로 떠나는 여행"
print("타이틀 송은? ", Singer.title_song)
boys.sing()
girls.sing()