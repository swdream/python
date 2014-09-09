class AttrExample(dict):
    """ Example of overloading __setattr__ and __getattr__
    This example creates a dictionary where members can be
    accessed as attributes
    """

    def __init__(self, indict=None, attribute=None):
        if indict is None:
            indict = {}
        # set any attributes here - before initialisation
        # these remain as normal attributes
        self.attribute = attribute
        dict.__init__(self, indict)
        self.__initialised = True
        # after initialisation, setting attributes is the same as setting an item

    def __getattr__(self, item):
        """ Map value to attributes.
        Only called if there is not an attribute with this name
        """
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, item, value):
        """Map attributes to values.
        Only called if we are __initialised
        """
        if not self.__dict__.has_key('_attrExample__initialised'):  # this test allows attributes to be set in the __init__ method
            return dict.__setattr__(self, item, value)
        elif self.__dict__.has_key(item):       # any normal attributes are handled normally
            dict.__setattr__(self, item, value)
        else:
            self.__setitem__(item, value)


if __name__ == '__main__':
    example = AttrExample(attribute='fish')
    print example.attribute

    example.fish = 'test'
    #print example['fish']
    print example.fish



