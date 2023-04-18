import os

from vehicle import Vehicle

from file_manager import FileManager

def main():

    vehicle = Vehicle('White', 4, '200km/h')

    path = os.path.abspath('{loc}/../{fname}'
                           .format(loc=__file__, fname='myfile.pkl'))
    
    fm = FileManager(path)
    
    fm.save_object(vehicle)

    del vehicle

    print(fm.get_object())


if __name__ == '__main__':
    main()