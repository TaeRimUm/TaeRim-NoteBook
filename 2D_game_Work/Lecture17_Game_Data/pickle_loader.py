class Npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

import pickle

with open('npc.pickle', 'rb') as f:
    #list를 세이브 했으니까
    npc_list = pickle.load(f)

for npc in npc_list:
    print(npc.name, npc.x, npc.y)

#실행하면 yuri 100 200
#       Tomp 100 200 이렇게 나옴. 저장하고 불러오기가 됨.
#하지만 클레스 변수는 pickle가 안됨....