'''
Author: Billy Cobb
Created: 10/2/2020
Disc: Automatic file sorter for homework organization. Homework files
      must be titled with class name first follow (ex: COMP206...)
'''

import os
from time import sleep

''' updated list of prefixes for current semester '''
class_prefixes = ['COMP206', 'COMP350', 'MGMT426', 'MGMT454', 'MGMT445']

''' updated path to homework dir here '''
main_dir_path = '.'

while True:

      with os.scandir(main_dir_path) as i:  # creates an itterator for items in directory
            for item in i:
                  for prefix in class_prefixes:
                        if item.name.__contains__(prefix) and item.is_file():
                              print(item.name)  # to be removed, used for debugging
                              os.rename(main_dir_path+ '/'+ item.name, main_dir_path+ '/'+ prefix+ '/'+ item.name)  # moves file to proper directory
                              break  # proceeds to next item

      sleep(3600)  # runs every hour (may be easier just to schedule it see here: https://datatofish.com/python-script-windows-scheduler/)