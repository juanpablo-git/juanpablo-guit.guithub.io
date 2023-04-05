class validations:
    @staticmethod
    def is_number(*args):
        for a in args:
            if type(a) is not str:
                return True
