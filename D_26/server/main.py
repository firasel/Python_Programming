""" Object processor """
import glob
import os
import shutil

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

source_object = glob.glob(source_path)

object_path = source_object[0]
shutil.copy(object_path, '.')

object_name = object_path.split('/')[-1].split('.')


for item in range(len(postfix)):
    filename = f'_{item}.'.join(object_name)
    shutil.copy(object_path, f'{destination_path}/{filename}')

os.remove(object_path)
os.remove('.'.join(object_name))
