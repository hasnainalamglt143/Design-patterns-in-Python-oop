class NetWorkService:
    def __init__(self):
        self._headers = {}  # instance variable (unique per object)

    def add(self, key, value):
        self._headers[key] = value

    def add_auth(self, key, value):
        self._headers["Authorization"] = {str(key): value}

    def add_cache(self, key, value):
        self._headers["CACHE-CONTROL"] = {str(key): value}

   

class NetWorkServiceBuilder:
    
    def __init__(self):
        self.header=NetWorkService()
    
    def show(self):
        print(self.header._headers)
    
    

    


if __name__=="__main__":
    builder=NetWorkServiceBuilder()
    builder.header.add("URL","https://www.example.com")
    builder.header.add_cache("time",34000)
    builder.header.add_auth("token",23444)
    builder.show()
    
    builder2=NetWorkServiceBuilder()
    builder2.header.add("URL","https://www.example.com")
    builder2.header.add_cache("time",34000)
    builder2.show()