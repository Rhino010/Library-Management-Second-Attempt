class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    
