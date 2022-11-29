import pickle


# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[], []]
collision_group = dict()
#objects 랑 collision_group를 피클해주면 됨!!

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        try:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
        except:
            pass
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()





def add_collision_pairs(a, b, group):

    if group not in collision_group:
        print('Add new group ', group)
        collision_group[group] = [ [], [] ] # list of list : list pair

    if a:
        if type(a) is list:
            collision_group[group][1] += a
        else:
            collision_group[group][1].append(a)

    if b:
        if type(b) is list:
            collision_group[group][0] += b
        else:
            collision_group[group][0].append(b)

    print(collision_group)



def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def update():
    for game_object in all_objects():
        game_object.update()




def save():
    game = [objects, collision_group] #우리가 저장해야 할 대상을 먼저 정해야 함.
    with open('game.sav', 'wb') as f:
        pickle.dump(game, f)
        #이러면 game_world 몽땅 세이브 끝!!!

def load():
    global objects, collision_group
    with open('game.sav', 'rb') as f:
        game = pickle.load(f)
        objects, collision_group = game[0], game[1]
        #로드도 끝!!!

#만약, 내 게임이 배경이 변하지 않는다면, game_world를 전부 저장할 필요가 없다. 그건 조정해야 함.