#!/usr/bin/env python3


class PrettyGirl:
    def __init__(self, name, skin, height, *BWH):
        self.name, self.skin, self.height, self.BWH = name, skin, height, BWH

    def sing(self):
        print("{} can sing pop music song".format(self.name))

    def dance(self):
        print(
            "{0} can dancing national dance, my skin {1}, my height is {2}, my BWH is {3}".format(self.name, self.skin, self.height, self.BWH))

    def cooking(self, cuisine):
        # self.dish =dish
        print(
            "{0} can cook rice fried with eggs and Hunam cuisine series food and {1}.".format(self.name, cuisine))

    def washing(self):
        print("{} can wash all all the the clothes".format(self.name))

class SmallPrettyGirl(PrettyGirl):
        pass   
