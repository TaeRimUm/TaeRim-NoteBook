import os
#소스코드를 import하면 그 소스를 실행하는 것임.
# ex) import show_files 실행하면 파일들을 보여줌ㄴ

file_name_list = os.listdir()
for name in file_name_list:
    print(name)

