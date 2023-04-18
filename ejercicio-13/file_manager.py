import pickle

class FileManager:
    def __init__(self, path):
        self.path = path

    def save_object(self, object):
        f = open(self.path, 'wb')
        pickle.dump(object, f, -1)

    def get_object(self):
        f = open(self.path, 'rb')
        return pickle.load(f)