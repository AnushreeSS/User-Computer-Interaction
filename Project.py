from aiml import Kernel
from os import startfile, listdir, remove, rename, walk, mkdir, getcwd
from os.path import join, isfile
from shutil import move, rmtree
from validate import validate_dir, validate_file
from webbrowser import open as open_browser
from Steganography import Steganography
from random import choice
from sys import argv, exit

FILE_PATH = getcwd()+"\\"


def start():
    kernel = Kernel()
    kernel.verbose(False)
    if isfile(FILE_PATH+"aimlFiles\\brain.brn"):
        kernel.bootstrap(brainFile=FILE_PATH+"aimlFiles\\brain.brn")
    else:
        print("Please run brain.py file present in aimlFiles directory")
        exit()

    return kernel


def open_file(filename):
    try:
        if '.' not in filename:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to open a folder?(Y/N)? ").upper()
            if ch == "Y":
                filename = validate_dir(filename)
            else:
                filename = validate_file(filename)
        else:
            filename = validate_file(filename)
        if filename == -1:
            return False
        startfile(filename)
        s = filename + " has been opened"
        print(s)
        return True
    except Exception as e:
        print("Exception occurred in open()"+str(e))
        return False


def create_file_in_directory(filename, directory_name):
    try:
        if directory_name.upper() in ["THIS", "CURRENT", "PRESENT"]:
            directory_name = getcwd()
        valid_dir = validate_dir(directory_name)
        if valid_dir == -1:
            return False
        filename = valid_dir + "\\" + filename
        if '.' not in filename:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to create a folder?(Y/N)? ").upper()
            if ch == 'Y':
                print("Folder has been created")
                mkdir(filename)
                startfile(filename)
                return True
            else:
                with open(filename, "a"):
                    print("File has been created")
                startfile(filename)
                return True
        with open(filename, "a"):
            print("File has been created")
        startfile(filename)
        return True
    except Exception as e:
        print("Exception occurred in create()"+str(e))
        return False


def create_file(filename):
    try:
            str1 = "Do you want to create " + filename + " in the current working directory?(Y/N) "
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input(str1).upper()
            if ch == 'Y':
                if '.' not in filename:
                    ch = ''
                    while ch != 'Y' and ch != 'N':
                        ch = raw_input("Are you trying to create a folder?(Y/N)? ").upper()
                    if ch == 'Y':
                        print("Folder has been created")
                        mkdir(filename)
                        startfile(filename)
                        return True
                    else:
                        with open(filename, "a"):
                            print("File has been created")
                        startfile(filename)
                        return True
                with open(filename, "a"):
                    print("File has been created")
                startfile(filename)
                return True
            directory_name = raw_input("Enter the path to the directory where the file has to be created: ")
            valid_dir = validate_dir(directory_name)
            if valid_dir == -1:
                return False
            filename = valid_dir+"\\" + filename
            if '.' not in filename:
                ch = ''
                while ch != 'Y' and ch != 'N':
                    ch = raw_input("Are you trying create a folder?(Y/N)?").upper()
                if ch == 'Y':
                    print("Folder has been created")
                    mkdir(filename)
                    startfile(filename)
                    return True
                else:
                    with open(filename, "a"):
                        print("File has been created")
                    startfile(filename)
                    return True
            with open(filename, "a"):
                print("File has been created")
            startfile(filename)
            return True
    except Exception as e:
        print("Exception occurred in create()"+str(e))
        return False


def list_files(directory_name):
    try:
        dir_name = validate_dir(directory_name)
        if dir_name == -1:
            return False

        files_list = listdir(dir_name)
        if len(files_list) == 0:
            print("No files in that directory")
            return False
        print("Files in the directory:")
        for i in files_list:
            print i
        return True
    except Exception as e:
        print("Exception occurred in listFiles()" + str(e))
        return False


def move_file_type_1(source, destination):
    try:
        if source.upper() in ["THIS", "CURRENT", "PRESENT", "THE"]:
            source = getcwd()
        if destination.upper() in ["THIS", "CURRENT", "PRESENT", "THE"]:
            destination = getcwd()
        if '.' not in source:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to move a folder?(Y/N)? ").upper()
            if ch == 'Y':
                src1 = validate_dir(source)
            else:
                src1 = validate_file(source)
        else:
            src1 = validate_file(source)

        if src1 == -1:
            return False
        dst1 = validate_dir(destination)
        if dst1 == -1:
            return False
        move(src1, dst1)
        s = src1 + " has been moved to " + dst1
        print(s)
        return True
    except Exception as e:
        print("Exception occurred in moveFile(s,d)" + str(e))
        return False


def move_file_type_2(filename, source, destination):
    try:
        if source.upper() in ["THIS", "CURRENT", "PRESENT", "THE"]:
            source = getcwd()
        if destination.upper() in ["THIS", "CURRENT", "PRESENT", "THE"]:
            destination = getcwd()
        src1 = source + "\\" + filename
        if '.' not in src1:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to move a folder?(Y/N)? ").upper()
            if ch == 'Y':
                src1 = validate_dir(src1)
            else:
                src1 = validate_file(src1)
        else:
            src1 = validate_file(src1)
        if src1 == -1:
            return False
        dst1 = validate_dir(destination)
        if dst1 == -1:
            return False
        move(src1, dst1)
        s = src1 + " has been moved to " + dst1
        print(s)
        return True
    except Exception as e:
        print("Exception occurred in moveFile(f,s,d)" + str(e))
        return False


def delete_file(filename):
    try:
        if '.' not in filename:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to delete a folder?(Y/N)? ").upper()
            if ch == 'Y':
                directory = validate_dir(filename)
                if directory == -1:
                    return False
                rmtree(directory)
                s = directory + " has been deleted"
                print(s)
                return True
            else:
                final_path = validate_file(filename)
        else:
            final_path = validate_file(filename)
        if final_path != -1:
            remove(final_path)
            s = final_path+" has been deleted"
            print(s)
            return True
        return False
    except Exception as e:
        print('Exception thrown in deleteFile() ' + str(e))


def rename_file(old_name, new_name):
    try:
        if '.' not in old_name:
            ch = ''
            while ch != 'Y' and ch != 'N':
                ch = raw_input("Are you trying to rename a folder?(Y/N)? ").upper()
            if ch == 'Y':
                final_path = validate_dir(old_name)
            else:
                final_path = validate_file(old_name)
        else:
            final_path = validate_file(old_name)

        if final_path != -1:
            rename(final_path, final_path.replace(old_name, new_name))
            s = old_name + " has been renamed with " + new_name
            print(s)
            return True
        return False
    except Exception as e:
        print('Exception thrown in renameFile() ' + str(e))


def find_all(name, path):
    result = []
    for root, dirs, files in walk(path):
        if name in dirs:
            result.append(join(root, name))
        if name in files:
            result.append(join(root, name))
    return result


def search_file(filename):
    try:
        ch = ''
        while ch != 'Y' and ch != 'N':
            ch = raw_input("Would you like to start from the current working directory?(Y/N)? ").upper()
        if ch == 'Y':
            path = getcwd()
            print("Searching \"" + filename + "\"...")
        else:
            resp = ''
            while resp != 'Y' and resp != 'N':
                resp = raw_input("Would you like to enter a start path for searching the file/folder?(Y/N)? ").upper()
            if resp == 'N':
                path = '/'
                print("This might take some time...\nSearching \"" + filename + "\"...")
            else:
                path = raw_input("Please enter the search path: ")
                path = validate_dir(path)
                if path == -1:
                    return False
                print("Searching \"" + filename + "\"...")
        result = find_all(filename, path)
        if len(result) == 0:
            print("\""+filename+"\" not found in this drive")
            return False
        elif len(result) == 1:
            print(filename + " was found in the following location: "+result[0])
            return True
        else:
            print(filename + " was found in the following locations:")
            for i in result:
                print(i)
            return True

    except Exception as e:
        print('Exception thrown in searchFile() ' + str(e))


def search_file_in_directory(filename, directory):
    try:
        if directory.upper() in ["THIS", "CURRENT", "PRESENT", "THE"]:
            path = getcwd()
        else:
            path = validate_dir(directory)
            if path == -1:
                return False
            print("Searching \"" + filename + "\"...")
        result = find_all(filename, path)
        if len(result) == 0:
            print("\"" + filename + "\" not found in this drive")
            return False
        elif len(result) == 1:
            print(filename + " was found in the following location: " + result[0])
            return True
        else:
            print(filename + " was found in the following locations:")
            for i in result:
                print(i)
            return True

    except Exception as e:
        print('Exception thrown in searchFile() ' + str(e))


def browse(query):
    try:
        url = "https://www.google.com.tr/search?q={}".format(query)
        open_browser(url)
        print("Search has been made")
        return True

    except Exception as e:
        print('Exception thrown in browse() ' + str(e))
        return False


def encrypt(filename,  msg):
    output_filename = ""
    if filename != "":
        if not filename.endswith(".png"):
            print("Invalid image file format! Encryption only accepts .png file")
            return False
        filename = validate_file(filename)
        if filename == -1:
            return False
    else:
        files = listdir(getcwd())
        for i in files:
            if i.endswith(".png"):
                filename = i
                print filename
                break
        flag = 0
        if filename != "":
            print("Found some image files in the current directory")
            ch = raw_input("Do you want me to encrypt on "+filename+"?(Y/N)? ").upper()
            if ch == 'Y':
                flag = 1
        if flag == 0:
            ch = raw_input("Would you like to enter a filename?(Y/N)? ").upper()
            if ch == 'Y':
                filename = raw_input("Enter the filename: ")
                filename = validate_file(filename)
                if filename == "-1":
                    return False
            else:
                ch = raw_input("Would you like me to encrypt it on any random file?(Y/N)").upper()
                if ch == 'Y':
                    files = listdir(FILE_PATH+"Image")
                    output_filename = choice(files)
                    filename = FILE_PATH+"Image\\"+output_filename
                    output_filename = output_filename[:-4]+"_encrypted.png"
                else:
                    return False
    img = Steganography.imread(filename)
    if msg == "":
        msg = raw_input("Enter a message to be hidden: ")

    new_img = Steganography.image_encryption(img, msg)
    x = 1
    if output_filename == "":
        output_filename = filename[:-4] + "_encrypted.png"
    while isfile(output_filename):
        output_filename = output_filename[:-4] + str(x) + ".png"
        x += 1
    Steganography.imwrite(output_filename, new_img)
    print("Encryption Done")
    print("File is saved as: "+output_filename)
    startfile(output_filename)
    return True


def decrypt(filename):
    if not filename.endswith(".png"):
        print("Invalid input filename")
        return False
    filename = validate_file(filename)
    if filename == -1:
        return False
    try:
        img = Steganography.imread(filename)
        msg = Steganography.image_decryption(img)
        print "Message is: ", msg
    except Exception as e:
        print str(e)
    return True


def audio_encrypt(filename, msg):
    output_filename = ""
    if filename != "":
        if not filename.endswith(".wav"):
            print("Invalid image file format! Encryption only accepts .wav audio file")
            return False
        filename = validate_file(filename)
        if filename == -1:
            return False
    else:
        files = listdir(getcwd())
        for i in files:
            if i.endswith(".wav"):
                filename = i
                print filename
                break
        flag = 0
        if filename != "":
            print("Found some audio files in the current directory")
            ch = raw_input("Do you want me to encrypt on "+filename+"?(Y/N)? ").upper()
            if ch == 'Y':
                flag = 1
        if flag == 0:
            ch = raw_input("Would you like to enter a filename?(Y/N)? ").upper()
            if ch == 'Y':
                filename = raw_input("Enter the filename: ")
                filename = validate_file(filename)
                if filename == "-1":
                    return False
            else:
                ch = raw_input("Would you like me to encrypt it on any random file?(Y/N)").upper()
                if ch == 'Y':
                    files = listdir(FILE_PATH+"Audio")
                    output_filename = choice(files)
                    filename = FILE_PATH+"Audio\\"+output_filename
                    output_filename = output_filename[:-4]+"_encrypted.wav"
                else:
                    return False
    aud = Steganography.open(filename, "rb")
    if msg == "":
        msg = raw_input("Enter a message to be hidden: ")
    new_data = Steganography.audio_encryption(aud, msg)
    x = 1
    if output_filename == "":
        output_filename = filename[:-4] + "_encrypted.wav"
    while isfile(output_filename):
        output_filename = output_filename[:-4] + str(x) + ".wav"
        x += 1
    new_aud = Steganography.open(output_filename, "wb")
    new_aud = Steganography.set_params(new_aud, aud)
    new_aud.writeframes(new_data)
    new_aud.close()
    print("Encryption Done")
    print("File is saved as: "+output_filename)
    startfile(output_filename)
    return True


def audio_decrypt(filename):
    if not filename.endswith(".wav"):
        print("Invalid input filename")
        return False
    filename = validate_file(filename)
    if filename == -1:
        return False
    try:
        aud = Steganography.open(filename, "rb")
        msg = Steganography.audio_decryption(aud)
        print "Message is: ", msg
    except Exception as e:
        print str(e)
    return True


def process(kernel, inp):
    inp = inp.replace('.', 'DOT')
    resp = kernel.respond(inp)
    resp = resp.replace("DOT", ".")
    list_current_folder = ["THIS FOLDER", "THIS DIRECTORY", "CURRENT WORKING DIRECTORY", "CURRENT FOLDER"]
    response = resp.split()
    if response[0] == "open":
        open_file(response[1])
    elif response[0] == "open1":
        if any([x in resp.upper() for x in list_current_folder]):
            f = response[1]
        else:
            f = response[2] + "\\" + response[1]
        open_file(f)
    elif response[0] == "create":
        create_file(response[1])
    elif response[0] == "create1":
        if any([x in resp.upper() for x in list_current_folder]):
            create_file_in_directory(response[1], getcwd())
        else:
            create_file_in_directory(response[1], response[2])
    elif response[0] == "list":
        if any([x in resp.upper() for x in list_current_folder]):
            list_files(getcwd())
        else:
            list_files(response[1])
    elif response[0] == "move":
        move_file_type_1(response[1], response[2])
    elif response[0] == "move1":
        move_file_type_2(response[1], response[2], response[3])
    elif response[0] == "delete":
        delete_file(response[1])
    elif response[0] == "delete1":
        if any([x in resp.upper() for x in list_current_folder]):
            f = response[1]
        else:
            f = response[2] + "\\" + response[1]
        delete_file(f)
    elif response[0] == "rename":
        rename_file(response[1], response[2])
    elif response[0] == "search":
        search_file(response[1])
    elif response[0] == "browse":
        browse(' '.join(response[1:]))
    elif response[0] == "search1":
        search_file_in_directory(response[1], response[2])
    elif response[0] == "help":
        with open("help.txt") as f:
            s = f.read()
            print(s)
    elif response[0] == "ENCRYPT":
        x = response.index("MESSAGE")
        if response[x+1] == "NO":
            msg = ""
        else:
            msg = ' '.join(response[x+1:])
        if response[1] == "IMAGE":
            filename = ""
            encrypt(filename, msg)
        elif response[1] == "AUDIO":
            filename = ""
            audio_encrypt(filename, msg)
        else:
            filename = response[1]
            if filename.endswith(".wav"):
                audio_encrypt(filename, msg)
            else:
                encrypt(filename, msg)

    elif response[0] == "DECRYPT":
        if response[1].endswith(".wav"):
            audio_decrypt(response[1])
        else:
            decrypt(response[1])
    else:
        print(resp)


if __name__ == "__main__":
    try:
        ker = start()  # Kernel
        if len(argv) > 1:
            cmd = " ".join(argv[1:])
            process(ker, cmd)
        else:
            print("\"hey\" version 1.2 <System Software Project>\nType \"help\" for more information")
            while True:
                cmd = raw_input("Enter your query: ")
                if cmd.lower() in ["exit", "close", "end"]:
                    print ("Program ends here")
                    break
                process(ker, cmd)

    except KeyboardInterrupt as k:
        print("Program ends here")
    except Exception as er:
        print("Program ends here")
        error_file_name = FILE_PATH + "error.txt"
        with open(error_file_name, "a") as filePtr:
            filePtr.write(str(er))
            filePtr.write("\n")
