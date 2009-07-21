import cgi
import friendfeed

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
      <html>
        <body>
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")
    
class TestFriendFeed(webapp.RequestHandler):
    def get(self):
        session = friendfeed.FriendFeed()        
        feed = session.fetch_public_feed()
        
        for entry in feed["entries"]:
            self.response.out.write(entry["published"].strftime("%m/%d/%Y")+": "+entry["title"]+"<br/>")
            
        

class Guestbook(webapp.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write('</pre></body></html>')

ROUTE = [('/', MainPage),
         ('/sign', Guestbook),
         ('/hello', MainPage),
         ('/testfriendfeed',TestFriendFeed)]

application = webapp.WSGIApplication(ROUTE,debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
