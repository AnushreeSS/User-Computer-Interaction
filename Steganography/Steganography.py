from wave import open
from cv2 import imread, imwrite
from numpy import array

SPECIAL_SYMBOL = '#'


def audio_encryption(aud, msg):
    """
    This module is used to encrypt audio to hide a given message. It takes an instance of audio file.
    The frames are read and the LSBs of the first few bytes are modified according to the message.
    Initially a special symbol is encrypted to identify mark that the audio file has been encrypted by this system.
    Next, the size of the message is stored.
    Therefore the first 32 bits are reserved for 8 bit special symbol and 24 bit length of the message.
    Next 8*(length_of_message) bits are used to encrypt the message.
    :param aud: instance - Audio stream pointer
    :param msg: string - Message to be hidden
    :return: string - String of modified bytes of the audio
    """
    data = aud.readframes(aud.getnframes())
    n = len(data)
    x = 0
    new_data = [i for i in data]
    if (len(msg) + 32) > n:
        raise Exception("Length Exceeded")
    binary = bin(ord(SPECIAL_SYMBOL))[2:].zfill(8)
    for i in binary:
        if i == '1':
            new_data[x] = chr(ord(new_data[x]) | 1)
        else:
            new_data[x] = chr(ord(new_data[x]) & 254)
        x += 1
    binary = bin(len(msg))[2:].zfill(24)
    for i in binary:
        if i == '1':
            new_data[x] = chr(ord(new_data[x]) | 1)
        else:
            new_data[x] = chr(ord(new_data[x]) & 254)
        x += 1
    for i in msg:
        binary = bin(ord(i))[2:].zfill(8)
        for j in binary:
            if j == '1':
                new_data[x] = chr(ord(new_data[x]) | 1)
            else:
                new_data[x] = chr(ord(new_data[x]) & 254)
            x += 1
    return ''.join(new_data)


def set_params(new_aud, aud):
    """
    This module is used to set up the new audio file.
    Some parameters are necessary to be build a new audio file.
    :param new_aud: instance - The pointer to the new audio stream
    :param aud: instance - The pointer to the given audio file
    :return: instance - The pointer to the new audio stream with all the parameters set as the previous one
    """
    new_aud.setframerate(aud.getframerate())
    new_aud.setnchannels(aud.getnchannels())
    new_aud.setnframes(aud.getnframes())
    new_aud.setsampwidth(aud.getsampwidth())
    new_aud.setparams(aud.getparams())
    return new_aud


def audio_decryption(aud):
    """
    This module is used to decrypt the message out of the given audio file. It takes the instance of the audio.
    It first decrypts the LSBs of first 8 bytes to get the special symbol that will help in determining
    if the was encrypted using the same system.
    Then the length of the message is decrypted following which the message of the obtained length is retrieved by
    identifying the LSBs of the following bytes.
    :param aud: instance - Audio stream pointer
    :return: string - Hidden message
    """
    data = aud.readframes(aud.getnframes())
    x = 0
    binary = ""
    for i in range(8):
        if ord(data[x]) % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        x += 1
    if bin(ord(SPECIAL_SYMBOL))[2:].zfill(8) == binary:
        print("Encrypted by this system")
    else:
        raise Exception("Not encrypted by this system")
    binary = ""
    for i in range(24):
        if ord(data[x]) % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        x += 1
    len_of_msg = int(binary, 2)
    print "Length of the hidden message =", len_of_msg
    msg = ""
    for i in range(len_of_msg):
        binary = ""
        for j in range(8):
            if ord(data[x]) % 2 == 0:
                binary += '0'
            else:
                binary += '1'
            x += 1
        msg += chr(int(binary, 2))
    return msg


def audio_processing():
    """
    This module is used to perform audio steganography
    :return: None
    """
    filename = raw_input("Enter the audio file name(*.wav): ")
    if not filename.endswith(".wav"):
        raise Exception("Invalid audio file format.")
    aud = open(filename, "rb")
    menu = "1. Steganographic Encryption of audio file\n2. Steganographic Decryption of audio file\nEnter your choice: "
    ch = input(menu)
    if ch == 1:
        msg = raw_input("Enter the message to be hidden: ")
        output_filename = raw_input("Enter the output filename(*.wav): ")
        if not output_filename.endswith(".wav"):
            raise Exception("Invalid audio file format.")
        new_data = audio_encryption(aud, msg)
        new_aud = open(output_filename, "wb")
        new_aud = set_params(new_aud, aud)
        new_aud.writeframes(new_data)
        new_aud.close()
        print("Encryption done")
        print ("Encrypted filename : " + output_filename)
    elif ch == 2:
        msg = audio_decryption(aud)
        print "Message is: ", msg
    aud.close()


def image_encryption(img, msg):
    """
    This module is used to encrypt a given image. It takes an image in the form of a 2D matrix with each cell
    containing RGB values.
    The least significant bit of the first few bytes of the image is changed according to the message.
    Initially a special symbol is encrypted to identify mark that image has been encrypted by this system.
    Next, the size of the message is stored.
    Therefore the first 32 bits are reserved for 8 bit special symbol and 24 bit length of the message.
    Next 8*(length_of_message) bits are used to encrypt the message.
    :param img: numpy.array - Byte representation of image
    :param msg: string - Message to be hidden in the image
    :return: numpy.array - Modified Byte representation of the image
    """
    x, y, z = 0, 0, 0
    m, n, o = len(img), len(img[0]), len(img[0][0])
    new_img = [i for i in img]
    new_img = array(new_img)
    if (len(msg) + 32) > (m * n * o):
        raise Exception("Length Exceeded")
    binary = bin(ord(SPECIAL_SYMBOL))[2:].zfill(8)
    for i in binary:
        if i == '1':
            new_img[x][y][z] = new_img[x][y][z] | 1
        else:
            new_img[x][y][z] = new_img[x][y][z] & 254
        if (z + 1) == o:
            z = 0
            if (y + 1) == n:
                y = 0
                if (x + 1) == m:
                    break
                else:
                    x += 1
            else:
                y += 1
        else:
            z += 1
    binary = bin(len(msg))[2:].zfill(24)
    for i in binary:
        if i == '1':
            new_img[x][y][z] = new_img[x][y][z] | 1
        else:
            new_img[x][y][z] = new_img[x][y][z] & 254
        if (z + 1) == o:
            z = 0
            if (y + 1) == n:
                y = 0
                if (x + 1) == m:
                    break
                else:
                    x += 1
            else:
                y += 1
        else:
            z += 1

    for i in msg:
        binary = bin(ord(i))[2:].zfill(8)
        for j in binary:
            if j == '1':
                new_img[x][y][z] = new_img[x][y][z] | 1
            else:
                new_img[x][y][z] = new_img[x][y][z] & 254
            if (z + 1) == o:
                z = 0
                if (y + 1) == n:
                    y = 0
                    if (x + 1) == m:
                        break
                    else:
                        x += 1
                else:
                    y += 1
            else:
                z += 1
    return new_img


def image_decryption(img):
    """
    This module is used to decrypt the message out of the given image. It takes the byte representation of an image.
    It decrypts the LSBs of first 8 bytes to get the special symbol to know if it was encrypted using the same system.
    Then the length of the message is decrypted following which the message of the obtained length is retrieved by
    identifying the LSBs of the following bytes.
    :param img: numpy.array - Byte representation of image
    :return: string - Hidden message
    """
    binary = ""
    x = 0
    y = 0
    z = 0
    m, n, o = len(img), len(img[0]), len(img[0][0])
    for i in range(8):
        if img[x][y][z] % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        if (z + 1) == o:
            z = 0
            if (y + 1) == n:
                y = 0
                if (x + 1) == m:
                    break
                else:
                    x += 1
            else:
                y += 1
        else:
            z += 1
    if bin(ord(SPECIAL_SYMBOL))[2:].zfill(8) == binary:
        print("Encrypted by this system")
    else:
        raise Exception("Not encrypted by this system")
    binary = ""
    for i in range(24):
        if img[x][y][z] % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        if (z + 1) == o:
            z = 0
            if (y + 1) == n:
                y = 0
                if (x + 1) == m:
                    break
                else:
                    x += 1
            else:
                y += 1
        else:
            z += 1
    len_of_msg = int(binary, 2)
    print "Length of the hidden message =", len_of_msg
    msg = ""
    for i in range(len_of_msg):
        binary = ""
        for j in range(8):
            if img[x][y][z] % 2 == 0:
                binary += '0'
            else:
                binary += '1'
            if (z + 1) == o:
                z = 0
                if (y + 1) == n:
                    y = 0
                    if (x + 1) == m:
                        break
                    else:
                        x += 1
                else:
                    y += 1
            else:
                z += 1
        msg += chr(int(binary, 2))
    return msg


def image_processing():
    """
    This module is used to perform image steganography
    :return: None
    """
    filename = raw_input("Enter the image file name(*.png): ")
    if not filename.endswith(".png"):
        raise Exception("Invalid image file format.")
    img = imread(filename)
    menu = "1. Steganographic Encryption of image file\n2. Steganographic Decryption of image file\nEnter your choice: "
    ch = input(menu)
    if ch == 1:
        msg = raw_input("Enter the message to be hidden: ")
        output_filename = raw_input("Enter the output filename(*.png): ")
        if not output_filename.endswith(".png"):
            raise Exception("Invalid image file format.")
        new_img = image_encryption(img, msg)
        imwrite(output_filename, new_img)
        print("Encryption done")
        print ("Encrypted filename : " + output_filename)
    elif ch == 2:
        msg = image_decryption(img)
        print "Message is: ", msg


if __name__ == "__main__":
    try:
        inp_menu = "1. Image Steganography\n2. Audio Steganography\nEnter your choice: "
        choice = input(inp_menu)
        if choice == 1:
            print "Image Steganography"
            image_processing()
        elif choice == 2:
            print "Audio Steganography"
            audio_processing()
    except Exception as e:
        print("Error: " + str(e))
