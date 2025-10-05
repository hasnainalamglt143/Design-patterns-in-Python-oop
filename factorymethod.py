# without factory method

# Python Code for Object
# Oriented Concepts without
# using Factory method 

# class FrenchLocalizer:

#     """ it simply returns the french version """

#     def __init__(self):

#         self.translations = {"car": "voiture", "bike": "bicyclette",
#                              "cycle":"cyclette"}

#     def localize(self, msg):

#         """change the message using translations"""
#         return self.translations.get(msg, msg)

# class SpanishLocalizer:
#     """it simply returns the spanish version"""

#     def __init__(self):

#         self.translations = {"car": "coche", "bike": "bicicleta",
#                              "cycle":"ciclo"}

#     def localize(self, msg):

#         """change the message using translations"""
#         return self.translations.get(msg, msg)

# class EnglishLocalizer:
#     """Simply return the same message"""

#     def localize(self, msg):
#         return msg

# if __name__ == "__main__":

#     # main method to call others
#     f = FrenchLocalizer()
#     e = EnglishLocalizer()
#     s = SpanishLocalizer()

#     # list of strings
#     message = ["car", "bike", "cycle"]

#     for msg in message:
#         print(f"french for '{msg}' {f.localize(msg)}")
#         print(f"english for '{msg}' {e.localize(msg)}")
#         print(f"spanish for '{msg}' {s.localize(msg)}")



# with factory method



class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):

        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


def Factory(language="English"):
    localizers = {
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
        "English": EnglishLocalizer
    }
    return localizers[language]()

if __name__ == "__main__":
    factory=Factory(language="French")
    print(factory.localize("car"))
    print(Factory("Spanish").localize("car"))
    



   