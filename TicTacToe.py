import os
import logging
import game_mech

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


def ResetGame():
  pass

class GameData(db.Model):
  pass

def MoveTTT(col,row,big_board,turn):
  big_board,turn = game_mech.make_move(turn,col,row,big_board)
  logging.info(big_board)
  message,highlight = game_mech.checkifwon(big_board)
  if message != None:
    win = message
  else:
    win = " "
  return big_board, turn, win,highlight

def MoveTTT_crazy(table_n,col,row,big_board,turn,win_t,bmn,bn):
    #columns of the big board
    big_board[table_n],turn = game_mech.make_move_crazy(big_board[table_n],row,col,turn)
    logging.info(big_board[table_n])
    logging.info(win_t[table_n])
    message,win_t[table_n] = game_mech.checkifwon_crazy(big_board[table_n],win_t[table_n])
    if message != None:
      win,temp = game_mech.checkifwon_crazy_f(win_t)
    else:
      win = " "
    return big_board, turn, win_t,win

def TransImage(win_t): 
  trans_image = ["/static/None.png"for _ in range(9)]
  for x in range(9):
    if win_t[x] == 1:
      trans_image[x]="/static/CircleTrans.png"
    if win_t[x] == 2:
      trans_image[x]="/static/CrossTrans.png"
  return trans_image
    
def Highlight_game(win_t):
  trans_image = ["white"for _ in range(9)]
  for x in range(9):
    if win_t == 1:
      trans_image[x]="red"
    if win_t == 2:
      trans_image[x]="black"
  return trans_image

def HighlightButton(highlight,template_values):
  button_color = [["","",""],["","",""],["","",""]]
  if highlight != "":
    for x in highlight:
       button_color[x[0]][x[1]] = "background-color:lightgreen"
  return button_color
    

class HomeHandler(webapp.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), "home.html")
    self.response.out.write(template.render(path, template_values))

class CrazyGameHandler(webapp.RequestHandler):
  def get(self):
    turn = 1
    big_board = [[[0,0,0]for _ in range(3)]for _ in range(9)]
    win_t = [0for _ in range(9)]
    template_values = game_mech.ConverttoDict_crazy(big_board)
    template_values["highlight_current"] = ["#999"for _ in range(9)]
    logging.info(template_values["highlight_current"])
    template_values["StringMatrix"] = game_mech.ConverttoString_crazy(big_board,turn,win_t," ")
    template_values["last_move"] = "99"
    template_values["button_color"] = [[[""for _ in range(3)]for _ in range(3)]for _ in range(9)]
    template_values["blank_image"]= "display:none"
    template_file = "crazy.html"
    logging.info(template_values["StringMatrix"])
    path = os.path.join(os.path.dirname(__file__), template_file)
    self.response.out.write(template.render(path, template_values))
  def post(self):
    if self.request.get('block'):
      big_board,turn,win_t,win = game_mech.ConverttoMatrix_crazy(self.request.get('StringMatrix'))
      last_move=self.request.get('last_move')
      logging.info(big_board)
      location = self.request.get('block')
      table_n = int(location[1])-1
      col = int(location[3])-1
      row = int(location[5])-1
      logging.info(win)
      bn = (table_n)%3
      if table_n in [0,1,2]:
        bmn = 0
      if table_n in [3,4,5]:
        bmn = 1
      if table_n in [6,7,8]:
        bmn = 2
      message,win_t[table_n] = game_mech.checkifwon_crazy(big_board[table_n],win_t[table_n])
      if message != None:
        win,temp = game_mech.checkifwon_crazy_f(win_t)
      else:
        win = " "
      highlight_current = ["#999"for _ in range(9)]
      if (win != "Win" and bmn==int(last_move[0]) and bn==int(last_move[1])) or last_move=="99":
        big_board, turn, win_t,win = MoveTTT_crazy(table_n,col,row,big_board,turn,win_t,bmn,bn)
        last_move = str(row)+str(col)
      highlight_current[int(last_move[1])+int(last_move[0])*3] = "lightgreen"
      template_values = game_mech.ConverttoDict_crazy(big_board)
      template_values["blank_image"]= "display:none"
      if win == "Win":
	      template_values["blank_image"]= "position:absolute"
	      template_values["highlight_current"] = ["#999"for _ in range(9)]
      logging.info(template_values)
      #button_color= HighlightButton(highlight,template_values)
      template_values["highlight_current"] = highlight_current
      template_values["button_color"] = [[[""for _ in range(3)]for _ in range(3)]for _ in range(9)]
      template_values["StringMatrix"] = game_mech.ConverttoString_crazy(big_board,turn,win_t,win)
      template_values["last_move"] = last_move
      template_values["Winner"] = win
      template_values["Turn"] = str(turn)
      template_values["trans_img"] = TransImage(win_t)
      template_file = "crazy.html"
      path = os.path.join(os.path.dirname(__file__), template_file)
      self.response.out.write(template.render(path, template_values))
  def reset(self):
    self.get()

class DevelopersHandler(webapp.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), "developers.html")
    self.response.out.write(template.render(path, template_values))

class GameInfoHandler(webapp.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), "gameinfo.html")
    self.response.out.write(template.render(path, template_values))

class HelpHandler(webapp.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), "help.html")
    self.response.out.write(template.render(path, template_values))

class vsCompHandler(webapp.RequestHandler):
  def get(self):
    turn = 1
    big_board = [[0,0,0]]*3
    template_values = game_mech.ConverttoDict(big_board)
    template_values["StringMatrix"] = game_mech.ConverttoString(big_board,turn," ")
    template_file = "vsComp.html"
    logging.info(template_values)
    path = os.path.join(os.path.dirname(__file__), template_file)
    self.response.out.write(template.render(path, template_values))
  def post(self):
    if self.request.get('block'):
      a = self.request.get('StringMatrix')
      big_board,turn,win = game_mech.ConverttoMatrix(self.request.get('StringMatrix'))
      logging.info(big_board)
      location = self.request.get('block')
      if turn == 1:
        col = int(location[1])-1
        row = int(location[3])-1
        logging.info(win)
        message,highlight = game_mech.checkifwon(big_board)
        if message !="Win":
          big_board,  turn, win,highlight = MoveTTT(col,row,big_board,turn)
      message,highlight = game_mech.checkifwon(big_board) 
      if turn==2 and message!="Win":
        big_board = game_mech.compMove(big_board)
        turn=1
      message,highlight = game_mech.checkifwon(big_board)
      template_values = game_mech.ConverttoDict(big_board)
      logging.info(template_values)
      button_color= HighlightButton(highlight,template_values)
      template_values["button_color"] = button_color
      logging.info(button_color)
      template_values["StringMatrix"] = game_mech.ConverttoString(big_board,turn,win)
      template_values["Winner"] = win
      template_values["Turn"] = str(turn)
      template_file = "vsComp.html"
      path = os.path.join(os.path.dirname(__file__), template_file)
      self.response.out.write(template.render(path, template_values))
      if turn ==2 and message!="Win":
        self.post()
  def reset(self):
    self.get()

class OriginalGameHandler(webapp.RequestHandler):
  def get(self):
    turn = 1
    big_board = [[0,0,0]]*3
    template_values = game_mech.ConverttoDict(big_board)
    template_values["StringMatrix"] = game_mech.ConverttoString(big_board,turn," ")
    template_file = "original.html"
    logging.info(template_values)
    path = os.path.join(os.path.dirname(__file__), template_file)
    self.response.out.write(template.render(path, template_values))
  def post(self):
    if self.request.get('block'):
      a = self.request.get('StringMatrix')
      big_board,turn,win = game_mech.ConverttoMatrix(self.request.get('StringMatrix'))
      logging.info(big_board)
      location = self.request.get('block')
      col = int(location[1])-1
      row = int(location[3])-1
      logging.info(win)
      if win != "Win":
        big_board, turn, win,highlight = MoveTTT(col,row,big_board,turn)
      else:
        message,highlight = game_mech.checkifwon(big_board)
      template_values = game_mech.ConverttoDict(big_board)
      logging.info(template_values)
      button_color= HighlightButton(highlight,template_values)
      template_values["button_color"] = button_color
      logging.info(button_color)
      template_values["StringMatrix"] = game_mech.ConverttoString(big_board,turn,win)
      template_values["Winner"] = win
      template_values["Turn"] = str(turn)
      template_file = "original.html"
      path = os.path.join(os.path.dirname(__file__), template_file)
      self.response.out.write(template.render(path, template_values))
  def reset(self):
    self.get()



def main():
  application = webapp.WSGIApplication([('/original.*', OriginalGameHandler),
                                        ('/crazy.*',CrazyGameHandler),
                                        ('/vscomp.*', vsCompHandler),
                                        ('/developers.*', DevelopersHandler),
                                        ('/info.*',GameInfoHandler),
                                        ('/help.*',HelpHandler),
                                        ('/.*',HomeHandler)],
                                     debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
