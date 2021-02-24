import webapp2

class ShowNumber (webapp2.RequestHandler):
    def get(self, firstNumber):
        self.response.write("<html><body><p>%d + %d = %d</p></body></html>" % firstNumber)

