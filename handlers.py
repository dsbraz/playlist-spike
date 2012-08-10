import os
import cgi
import webapp2
from google.appengine.api import channel
from google.appengine.ext.webapp import template

class BasePage(webapp2.RequestHandler):
  def render(self, name, context = {}):
    path = os.path.join(os.path.dirname(__file__), 'templates/' + name)
    self.response.out.write(template.render(path, context))

class HomePage(BasePage):
  def get(self):
    self.render('index.html')

class RemoteControlPage(BasePage):
  def get(self):
    pairing_key = cgi.escape(self.request.get('p'))
    self.render('remote_control.html', { 'p': pairing_key })

  def post(self):
    pairing_key = cgi.escape(self.request.get('p'))
    message = cgi.escape(self.request.get('message'))
    channel.send_message(pairing_key, message)

class PlayerPage(BasePage):
  def get(self):
    pairing_key = cgi.escape(self.request.get('p'))
    token = channel.create_channel(pairing_key)
    self.render('player.html', { 'token': token })
