class Npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

yuri = Npc('yuri', 100, 200)
print(yuri.__dict__)
yuri.__dict__['age'] = 30 # 객체 변수를 만드는 또 하나의 방법.
print(yuri.name, yuri.x, yuri.y, yuri.age) #원해는 3줄에 self.age 넣고 = age 해줘여 함.

yuri.name, yuri.x, yuri.y = 'monika', 4, 5             # 이 역할을 함
                                                       # ㅅ
new_data = {'name':'jeny', 'x':5, 'y':100, 'age':30}   # ㅣ
yuri.__dict__.update(new_data) #기존의 딕셔너리 업테이트. 내부 객체는 딕셔너리가 처리하기 때문에.

tom = Npc('Tom', 100, 200)
print(tom.__dict__)
npc_list = [yuri, tom]

import pickle

with open('npc.pickle', 'wb') as f:
    pickle.dump(npc_list, f)

with open('npc.pickle', 'rb') as f:
    read_npc = pickle.load(f)
#실행하면 npc.pickle 이란 파일 만들어짐.