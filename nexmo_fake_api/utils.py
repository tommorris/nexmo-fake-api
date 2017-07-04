class ErrorCollection(object):
    def __init__(self):
         self.__collection__ = list() #

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


class DefaultErrorCollection(ErrorCollection):
    def __init__(self, error_code, error_text):
        super(DefaultErrorCollection, self).__init__()
        item = {
            "status": error_code,
            "error-text": error_text
        }
        self.append(item)


NO_API_KEY = DefaultErrorCollection("2", "Missing username")

