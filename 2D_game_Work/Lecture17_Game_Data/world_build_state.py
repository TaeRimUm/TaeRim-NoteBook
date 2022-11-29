# import json
#
# import game_world
# import server
# from boy import Boy
# from zombie import Zombie
#
#
# def create_new_world():
#     server.boy = Boy()
#     game_world.add_object(server.boy, 1)
#     # load json object data
#     with open('zombie_data.json', 'r') as f:
#         zombie_list = json.load(f)
#         for o in zombie_list:
#             zombie = Zombie(o['name'], o['x'], o['y'], o['size'])
#             game_world.add_object(zombie, 1)