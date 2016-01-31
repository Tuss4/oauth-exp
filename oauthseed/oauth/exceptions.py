class StatusNotOkay(Exception):

    """Should be raised when the status code of a response isn't 200"""

    def ___init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Non 200 status returned. Status: {}".format(self.value))
