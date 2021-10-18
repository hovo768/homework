#1
import os
import shutil
# os.makedirs('my_project/settings')
# os.mkdir('my_project/mainapp')
# os.mkdir('my_project/adminapp')
# os.mkdir('my_project/authapp')
#
# dirs = {'my_project' : ['settings', 'mainapp', 'adminapp', 'authapp']}
# for root, folder in dirs.items():
#     if os.path.exists(root):
#         print(root, 'существует')
#     else:
#         for folders in folder:
#             join_dir = os.path.join(root, folders)
#             os.makedirs(join_dir)

#2 не возможно
#3
new_dir = 'my_dir'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
floder = 'my_project'
files = []

for r, d, f in os.walk(floder):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
for path1 in files:
    folder= os.path.join(new_dir, os.path.basename(os.path.dirname(path1)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path1))
    shutil.copy(path1, save_path)

#4
files = []
for r,d,f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r,file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
u = 0
new_dict = {}

for i in range(len(str(max_size))):
    i *= 10
    new_dict[i] = u

for some in files:
    new_dict[10 ** len(str(some))] += 1


print(new_dict)