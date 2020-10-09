'''
Author: Billy Cobb
Project: FileSorter
Created on: 10/2/2020
Disc: Automatic file sorter for file organization. Files must be
      titled with a file tag somewhere in the file name.
'''

import os
from time import sleep

''' updated list of file tags used to determine destination dir (one of these tags must be somewhere in the file name) '''
file_tags = []

''' updated path to main dir here '''
main_dir_path = '.'

while True:

      with os.scandir(main_dir_path) as i:  # creates an itterator for items in directory
            for item in i:
                  for prefix in file_tags:
                        if item.name.__contains__(prefix) and item.is_file():
                              print(item.name)  # to be removed, used for debugging
                              os.rename(main_dir_path+ '/'+ item.name, main_dir_path+ '/'+ prefix+ '/'+ item.name)  # moves file to proper directory
                              break  # proceeds to next item

      sleep(3600)  # runs every hour (may be easier just to schedule it see here: https://datatofish.com/python-script-windows-scheduler/)