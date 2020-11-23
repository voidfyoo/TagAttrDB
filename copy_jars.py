#!/usr/bin/env python3

import glob
import sys
import os
from shutil import copyfile


def copy_jar_to_dir(src_file, dst_dir):
    name = os.path.basename(src_file).rstrip('.jar')

    dst_file = f'{dst_dir}/{name}.jar'
    if not os.path.exists(dst_file):
        copyfile(src_file, dst_file)
    else:
        uniq = 1
        while os.path.exists(f'{dst_dir}/{name}._{uniq}.jar'):
            uniq += 1
        dst_file = f'{dst_dir}/{name}._{uniq}.jar'
        copyfile(src_file, dst_file)


if __name__ == '__main__':

    # src_dir = sys.argv[1]
    # dst_dir = sys.argv[2]

    src_dir = ''
    dst_dir = ''


    print(f'copy jar files from {src_dir} to {dst_dir} ...')

    for filename in glob.iglob(f'{src_dir}/**/*.jar', recursive=True):
        if os.path.isfile(filename):
            copy_jar_to_dir(filename, dst_dir)

    print('done!')
