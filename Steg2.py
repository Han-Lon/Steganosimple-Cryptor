from stegano import lsb
from tkinter import filedialog


# A personal project to test out some Steganography functions. Steganography involves hiding data inside
# image files (e.g. in the buffer, in unused bits, etc) without altering the physical appearance of the image at all.


# Hide a message into an image using LSB method, and designate an output
def hide(message, image, output):
    secret = lsb.hide(image, message)
    secret.save(output)


# Reveal a message hidden in an image that was hidden using LSB method. Handles errors for if image
# doesn't have a message hidden within it.
def reveal(image):
    try:
        revealed = str.encode(lsb.reveal(image))
        revealedfinal = str(revealed, encoding='utf-8')
        return revealedfinal
    except TypeError:
        print('ERROR! Image doesn\'t seem to have any hidden message.')


if __name__ == '__main__':
    looper = True
    while looper:
        # Logic for interacting with the program in a CLI manner
        operation = input('Enter an operation - 1. Hide 2. Reveal \n')
        if operation == '1':
            print('Hide data option selected...')
            # Time to hide data in an image file
            message = input('\n Enter a message! \n')
            img_input = filedialog.askopenfilename()
            temp_path = img_input.split('.')
            output_path = temp_path[0] + '1' + '.png'
            hide(message, img_input, output_path)
            print('Message has been hidden in {}'.format(output_path))
        elif operation == '2':
            # Time to pull data hidden in an image file
            print('Reveal data option selected...')
            img_input = filedialog.askopenfilename()
            output = reveal(img_input)
            print('Data hidden in the image file: {}'.format(output))
        else:
            # Exit the function
            looper = False
            break

