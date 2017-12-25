#!/usr/bin/env python

import os
import re
import shutil


def name_convert(orig_file_loc, dest_file_loc):
    '''Copies .txt files to .csv files from and to specified locations.'''

    find = re.compile(r"^[^.]*")
    counter = 0

    for text_file in os.listdir(f'{orig_file_loc}'):
        file_name = find.search(text_file).group()

        if file_name == None:
            continue

        working_dir = os.path.abspath('.')
        shutil.copy(f'{working_dir}/{orig_file_loc}/{file_name}.us.txt', f'{working_dir}/{dest_file_loc}/{file_name}.csv')
        counter += 1


    print(f'Copied and reformatted {counter} .txt files to .csv from {working_dir}/{orig_file_loc} to {working_dir}/{dest_file_loc}')