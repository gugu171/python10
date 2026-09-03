class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language in India")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington D.C. (not New York) is the capital of the USA")
    def language(self):
        print("The USA does not have an official language, although the primary language is English")
    def type(self):
        print("The USA is a developed country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()