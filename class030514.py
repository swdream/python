#!usr/bin/env python2

class Cat():
    # every class has __init__(self,...)
    def __init__(self, catname, catowner, catage, catcolor, catheight):
        # setup attributes for our cat class
        self.name = catname
        self.owner = catowner
        self.age = catage
        self.color = catcolor
        self.height = catheight
        self.stupid = False

    # Define eat () method
    def eat(self):
        if self.stupid:
            print self.stupid
            print ' stupid is False, hehe'
            self.stupid = False
        else:
            print 'stupid is True, haha'


Thanh = Cat(' )
# print out all the attributes of Thanh'Thanh', 'swdream', '24 years', 'white', '165 Cm
print 'my name is %s' % Thanh.name
print 'my owner is %s' % Thanh.owner
print 'my age is %s' % Thanh.age
print 'my color is %s' % Thanh.color
print 'my height is %s' % Thanh.height

Thanh.eat()
Thanh.stupid = True
Thanh.eat()