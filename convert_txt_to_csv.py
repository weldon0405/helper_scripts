#!/usr/bin/env python

import os
import re
import shutil


def name_convert(orig_file_loc, dest_file_loc):
    '''Copies .txt files to .csv files from and to specified
    locations.'''

    find = re.compile(r"^[^.]*")
    counter = 0

    working_dir = os.path.abspath('.')
    full_orig_loc = f'{working_dir}/{orig_file_loc}'
    full_dest_loc = f'{working_dir}/{dest_file_loc}'

    for text_file in os.listdir(f'{orig_file_loc}'):
        file_name = find.search(text_file).group()

        if file_name == None:
            continue

        shutil.copy(f'{full_orig_loc}/{file_name}.us.txt', 
                    f'{full_dest_loc}/{file_name}.csv')
        counter += 1


    print(f'Copied and reformatted {counter} .txt files to .csv from {working_dir}/{orig_file_loc} to {working_dir}/{dest_file_loc}')