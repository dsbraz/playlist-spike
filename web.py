import webapp2
from handlers import HomePage, RemoteControlPage, PlayerPage

config = {}

app = webapp2.WSGIApplication([
  ('/', HomePage),
  ('/remotecontrol', RemoteControlPage),
  ('/player', PlayerPage),
], config=config, debug=True)
