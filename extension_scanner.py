import shutil,os,re,logging,sys,errno,shutil,time

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.info('Script startup!')
print('\n' + 55*'*'+'\nWelcome to the extension finder.\nCopy files with matching extension to a specified location.\n' + 55*'*')

def main():
    global dirpath
    dirpath = os.getcwd()
    print('Current directory ' + dirpath)
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
        os.system('clear')
        global regex
        global extension

        while True:
            try:
                print('Current regex: ' + regex)
            except NameError:
                print('Extension not set')
            print('Upon how many extensions you want to scan:\n0)one\n1)more\n2)Back')
            extension = input(str())

            if(extension == '0'):
                regex = input('Type the extension: ')
                if(regex == ''):
                    print("Can't be blank...\n")
                    continue
                logging.info("User typed: '{}'. Input type: {}.".format(regex, type(regex)))
                break

            elif(extension == '1'):
                regex = input(str('Type extensions devided by coma(,): '))
                if(regex == ''):
                    print("Can't be blank...\n")
                    continue            
                regex = regex.split(',')
                logging.info("User typed: '{}'. Input type: {}.".format(regex, type(regex)))
                regex = "|".join(regex)
                print(regex)
                break

            elif(extension == '2'):
                break

            else:
                print('Wrong input')
                continue
                
        os.system('clear')

    elif(a == '1'):
        os.system("ls -l ")
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
    # Scan directory
    elif(a == '3'):
        try:
            scanDir(dirpath, regex)
        except NameError:
            print('Regex not set!\n')
    elif(a == '4'):
        sys.exit()
    else:
        print('Wrong input...')



# scan dir and subfolders for assigned pattern
def scanDir(pathe, rege):
    match_array = []
    file_counter = 0
    file_weight = 0

    for foldername, subfolders, filenames in os.walk(pathe):
        logging.info('Current folder is '+ foldername)

        for subfolder in subfolders:
            logging.info('Scanning '+ foldername + '/' + subfolder)
        for filename in filenames:
            m = re.search(r'.*\.' + rege, filename)
            if(m == None):
                continue
            else:
                m = str(m)
                print("Found match " + m)
                match_array.append(foldername +'/' + filename)
                file_counter += 1
                file_weight += os.path.getsize(foldername)

    if(int(file_counter) == 0):
        print('No matches!\n')
    else:
        print('Found %d files' % (file_counter))
        print('Files weight: %d' % (file_weight))
        print("Some files might by duplicate, they won't be copied")
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

    while True:
        print('Current directory: '+path2 + ' where to move files?')
        print('1) Create a new directory\n2) Move to existing directory\n3) Abort')

        answ = input()

        if(answ == '1'):
            ans = input('Do you want to create a new directory at this location?(y/n)')
            if(ans == '' or ans == 'y'):
                dir_name = input('Give the name of directory: ')
                logging.info('Creating directory ' + dir_name)
                os.system('mkdir ' + dir_name)
                break
        elif(answ == '2'):
            dir_name = input('Give the name of directory: ')
            continue
        elif(answ == '3'):
            break
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
