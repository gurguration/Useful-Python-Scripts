import os
from pathlib import Path, PurePath
import webbrowser
import glob
import shutil

file_name = r'python_course\threaded_downloader.py'
curr_path = os.getcwd()
abs_path = os.path.abspath(curr_path)
user_dir = os.path.expanduser('~')
real_path = os.path.realpath(r'python_course\threaded_downloader.py')
rel_path = os.path.relpath(r'python_course\threaded_downloader.py')
dir_size = os.path.getsize(curr_path)
dir_name = os.path.dirname(curr_path)
split_path = os.path.split(curr_path)
base_name = os.path.basename(curr_path)
split_text = os.path.splitext(real_path)
print(curr_path)
print(abs_path)
print(base_name)
print(dir_name)
print(dir_size)
print(real_path)
print(rel_path)
print(split_path)
print(split_text)
print(user_dir)


# pathlib is better

fileto_open = Path(r'python_course\threaded_downloader.py')
absolute_path = fileto_open.absolute()
pure_path = PurePath(fileto_open)
print(absolute_path)
print(fileto_open.name)
print(fileto_open.suffix)
print(fileto_open.stem)
print(fileto_open.exists())
print(pure_path.suffix)


# BAD VERSION
os.chdir('./python_course')
for f_name in glob.glob('*.py'):
    # print(f_name)
    # print(os.path.abspath(f_name))
    new_path = os.path.join('archive', f_name)
    # print(new_path)
    # exit()
    shutil.copy(f_name, new_path)

# BETTER VERSION with Pathlib
current_dir = Path.cwd()
home_path = Path.home()
folderin_home = Path.home() / 'myfolder' / 'backup'
print(current_dir)
print(home_path)
print(folderin_home)

# same as above
folderin_home = Path.home().joinpath('myfolder', 'backup')
print(folderin_home)
print(type(folderin_home))  # Either WindowsPath or PosixPath (on linux/mac)

