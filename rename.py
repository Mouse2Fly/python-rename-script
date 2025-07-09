import os

def main():

    folder = 'E:\\projects\\rename'
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"track_{str(count + 316)}.ogg"
        src = f"april_10{str(count + 0)}.ogg"
        dst =f"./done/{dst}"

        os.rename(src, dst)

        print(f'Renamed {src} to {dst}')

main()