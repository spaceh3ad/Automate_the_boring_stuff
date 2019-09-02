#! python3
#search for specified file extension and copy 'em to a specified location

import shutil,os,re,logging,sys,errno,shutil,time

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.info('Script startup!')
print('\n' + 55*'*'+'\nWelcome to the extension finder.\nCopy files with matching extension to a specified location.\n' + 55*'*')

def main():
    global dirpath
    dirpath = os.getcwd()
    print('Current directory ' + dirpath)
    print('\n******REMEBER TO SET REGEX********\n')
    print('Choose option:')
    print('0) Set regex')
    print('1) See directory tree')
    print('2) Change directory')
    print('3) Scan directory')
    print('4) Quit')
    options()

def options():

    a = input()
    if(a == '0'):
        global regex
        try:
            print('Current regex: ' + regex)
        except NameError:
            print('Extension not set')
        regex = input('Set the extension\n')
        logging.info("User typed: '{}'. Input type: {}.".format(regex, type(regex)))
        logging.info(regex)

    elif(a == '1'):
        # print('Current path is: ' + dirpath)
        os.system("tree " + dirpath)
    # Change directory
    elif(a == '2'):
        try:
            path = input('Input the path:')
            if(path == ''):
                print('Path not changed')
            else:
                os.chdir(path)
                # print(path)
                return path
        except FileNotFoundError:
            logging.error('No such file or directory: ' + path)
            pass
    # Scan directory
    elif(a == '3'):
        scanDir(dirpath, regex)
    elif(a == '4'):
        sys.exit()
    else:
        options()



# scan dir and subfolders for assigned pattern
def scanDir(pathe, rege):
    match_array = []
    file_counter = 0
    file_weight = 0

    for foldername, subfolders, filenames in os.walk(pathe):
        logging.info('Scanning ' + foldername)
        logging.info('Current folder is '+ foldername)

        for subfolder in subfolders:
            logging.info('Scanning '+ foldername + '/' + subfolder)
        for filename in filenames:
            m = re.search(r'.*\.' + rege, filename)
            if(m == None):
                continue
            else:
                print(m)
                match_array.append(foldername +'/' + filename)
                file_counter += 1
                # logging.info(foldername)
                file_weight += os.path.getsize(foldername)
        # print('')


    print('Found %d files' % (file_counter))
    print('Files weight: %d' % (file_weight))
    # print(match_array)
    copylocation(match_array, pathe)

def toolbar(arr, dir_name):
    toolbar_width = 40

    for c in range(toolbar_width):
        sys.stdout.write('\r')
        for i in arr:
            shutil.copy(i, dir_name)
        sys.stdout.write("[%-39s] %d%%" % ('='*c, 2.5*c))
    sys.stdout.flush()
    print('\n')
    logging.info('Files moved succcesfully!')

def copylocation(arr, path2):

    print('Current directory: '+path2 + ' where to move files?')
    print('1) Create a new directory')
    print('2) Move to existing directory')
    answ = input()

    if(answ == '1'):
        ans = input('Do you want to create a new directory at this location?(y/n)')
        if(ans == '' or ans == 'y'):
            dir_name = input('Give the name of directory: ')
            logging.info('Creating directory ' + dir_name)
            os.system('mkdir ' + dir_name)
    elif(answ == '2'):
            dir_name = input('Give the name of directory: ')
    else:
        print('Wrong input')


    try:
        toolbar(arr, dir_name)
    except shutil.SameFileError:
        print('ERROR: File already exists in this location')


while True:
        try:
            main()
        except KeyboardInterrupt:
            print('\n')
            sys.exit()


