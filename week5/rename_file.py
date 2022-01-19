# have user input name of file to be renamed and name to change it to
# also includes other python os tools

import os

# get working dir
print(os.getcwd())

# list directory content
print(os.listdir())

# joining paths
print(os.path.join(os.getcwd(), 'sample_files'))

# create a directory
# os.mkdir('Dataset')
# print(os.listdir())

# rename a filename
# os.rename('sample_files', 'Samples')
print(os.listdir())

# check existing file
print(os.path.exists('Dataset'))

# get metadata
print(os.path.abspath('rename_file.py'))
