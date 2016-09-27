
import webapp2


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
      """
      <html>
        <head>
          <title>Awesome blog</title>
        </head>
        <body>
          <form method="post">
            <input type="number" name="numero">
            <input type="submit">
          </form>
        </body>
      </html>
      """
    )
    
  def post(self):
    nome = self.request.get("numero")
    self.response.out.write(int(numero)**2)

app = webapp2.WSGIApplication([
  ('/', MainHandler)
])
