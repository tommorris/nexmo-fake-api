class ErrorCollection(object):
    def __init__(self):
        self.__collection__ = list()
        pass

    def append(self, item):
        if (type(item) != dict):
            raise TypeError("Error Collection expects a dictionary.")

        self.__collection__.append(item) 

    def format(self):
        out = {
            "message-count": len(self.__collection__),
            "messages": self.__collection__
        }
        return out


NO_API_KEY = ErrorCollection()
NO_API_KEY.append({"status": "2", "error-text": "Missing username"})


