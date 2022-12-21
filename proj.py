import os
import shutil
from_dir='C:/Users/KskYm/Desktop/Photos'
to_dir='C:/Users/KskYm/Downloads'
list=os.listdir(to_dir)
for file in list:
  root,extension=os.path.splitext(file)
  if extension=='.zip':
    print(file)
