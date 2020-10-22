# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import time
import os.path

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(os.path.basename('C:/abc/fwef/uuu/'))
    print(os.sep)
    print(os.path.join('/one','two','\\three'))
    print(os.path.expandvars('$OS'))
    print(os.path.normpath('C:\\GitProjects\\samples\\UnityProject\\Assets\\CenturyGamePackageRes/../../Packages/manifest.json'))
    print(os.path.abspath('.'))
    print('File : ',__file__)
    print('Access Time : ',time.ctime(os.path.getatime(__file__)))
    for user in ['','username','nosuchuser']:
        lookup = '~'+user
        print(os.path.expanduser(lookup))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
