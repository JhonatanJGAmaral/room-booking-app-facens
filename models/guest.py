class Guest():
    def __init__(self, id=None, cpf=None, name=None, date_birth=None, phone=None):
        self.__id = id
        self.__cpf = cpf
        self.__name = name
        self.__date_birth = date_birth
        self.__phone = phone
        
    @property
    def id(self):
        return self.__id
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def name(self):
        return self.__name
    
    @property
    def date_birth(self):
        return self.__date_birth
    
    @property
    def phone(self):
        return self.__phone
