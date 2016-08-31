
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
            <input type="texte" name="nome">
            <input type="submit">
          </form>
        </body>
      </html>
      """
    )
    
  def post(self):
    texto = self.request.get("nome")
    self.response.out.white(texto)

app = webapp2.WSGIApplication([
  ('/', MainHandler)
])
