class PauyError(Exception):
    def __init__(self, message):
        super().__init__(message)

if __name__ == "__main__":
    raise PauyError("Test")