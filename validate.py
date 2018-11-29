from os.path import isfile, isdir


def validate_file(filename):
    try:
        if isfile(filename):
            return filename
        else:
            print("\"" + filename + "\" does not exist in the current directory.")
            response = raw_input("Would you like to specify a search path?(Y/N)? ")
            while response.lower() != 'y' and response.lower() != 'n':
                response = raw_input("Would you like to specify a search path?(Y/N)? ")
            while response == 'Y' or response == 'y':
                path = raw_input("Enter the path: ")
                print(path)
                if isdir(path):
                    if isfile(path + '\\' + filename):
                        return path + '\\' + filename
                    else:
                        msg = "\"" + filename + "\" does not exist in the specified path"
                        msg += "\nWould you like to specify the search path again?(Y/N)? "
                        response = raw_input(msg)
                        while response.lower() != 'y' and response.lower() != 'n':
                            response = raw_input("Would you like to specify the path again?(Y/N)? ")
                elif isfile(path):
                    return path
                else:
                    msg = "\"" + path + "\" is not a valid directory \nWould you like to specify the path again?(Y/N)? "
                    response = raw_input(msg)
                    while response.lower() != 'y' and response.lower() != 'n':
                        response = raw_input("Would you like to specify the path again?(Y/N)? ")
            if response == 'N' or response == 'n':
                return -1
    except Exception as e:
        print('Exception thrown in validateFile() ' + str(e))


def validate_dir(directory_name):
    if isdir(directory_name):
        return directory_name
    else:
        print("\"" + directory_name + "\" does not exist in the current working directory")
        ch = raw_input("Would you like to specify a search path?(Y/N)? ").upper()
        while True:
            if ch == "Y":
                path = raw_input("Enter the path: ")
                if isdir(path):
                    return path
                else:
                    print("\"" + path + "\" is not a valid directory")
            elif ch == 'N':
                return -1
            ch = raw_input("Would you like to specify the path again?(Y/N)? ").upper()
