import os

def main():
    path = os.path.abspath(f'{__file__}/../myfile.txt')

    f = open(path, 'a')
    f.write('Lorem ipsum \n')
    f.close()

    f = open(path)
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()