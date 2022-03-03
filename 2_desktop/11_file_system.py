import os

# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("2_desktop") # 해당 작업 공간으로 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동

# 파일 경로
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\YSJ\Desktop\RPA\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# ctime = os.path.getctime("trash_icon.png")
# print(ctime)
# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("trash_icon.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("trash_icon.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize("trash_icon.png") # 파일 크기를 byte 단위로 가져옴.
# print(size)


# 파일 목록 가져오기
# print(os.listdir()) # 작업공간 내의 모든 폴더, 파일목록 가져옴
# print(os.listdir("1_excel"))

# 파일 목록 가져오기 (하위 폴더 내의 파일도 포함)
# result = os.walk(".")
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일 찾기
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 폴더 내에서 특정 패턴을 가진 파일들을 찾기
# *.xlsx, *.txt ...
# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)


# 주어진 경로가 파일인지 폴더인지
# print(os.path.isdir("2_desktop"))
# print(os.path.isfile("2_desktop"))

# 주어진 경로가 존재하는지?
# if os.path.exists("2_desktop"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")


# 파일 만들기
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") 
# os.makedirs("new_folders/a/b/c") #하위 폴더를 가지는 폴더 생성

# 폴더 지우기
# os.rmdir("new_folders") # 폴더 안이 비었을 때만 삭제 가능

import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더 안이 비어있지 않아도 완전 삭제 가능

# 파일 복사하기
# shutil.copy("trash_icon.png", "test_folder") # 원본 경로, 대상 경로
# shutil.copy("trash_icon.png", "test_folder/copied_trash_icon.png") # 원본 파일 경로, 대상 경로에 파일 이름까지
# shutil.copy2("trash_icon.png", "test_folder/copy2.png") # 워본 파일 경로, 대상 폴더(파일) 경로

# copy, copyfile : 메타 정보 복사 x (복사한 시점의 시간으로 복사됨)
# copy2 : 메타정보 복사 o (원본 파일이 만들어진 시간으로 복사됨)

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")

# 폴더 이동
# shutil.move("test_folder", "test_folder2")
shutil.move("test_folder2", "test_folder") # 폴더명이 변경되는 효과