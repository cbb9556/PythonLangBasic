import os
import time


def main():
    content = "you are the best!..."

    while True:
        os.system('cls')
        print(content)
        time.sleep(0.1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
