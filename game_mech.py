#Game Mechanics
import random
def make_move(turn,col,row, m):
	if m[row][col] != 0:
		pass
	elif turn==1:
		m[row][col]= 1
		turn=2
	else:
		m[row][col]=2
		turn=1
	return m,turn


def checkifwon(m):
	for x in range(3):
		#check horizontal
		if (m[x][0]==m[x][1]==m[x][2]) and (m[x][0] != 0):
			highlight = [[x,0],[x,1],[x,2]]
			return "Win",highlight
		elif (m[0][x]==m[1][x]==m[2][x]) and (m[2][x] != 0):
			highlight = [[0,x],[1,x],[2,x]]
			#checking vertical
			return "Win",highlight
	#Checks diagonals
	if (m[0][0]==m[1][1]==m[2][2]) and (m[2][2] != 0 ):
		highlight = [[0,0],[1,1],[2,2]]
		return "Win",highlight
	elif (m[2][0]==m[1][1]==m[0][2]) and (m[1][1]!= 0):
		highlight = [[2,0],[1,1],[0,2]]
		return "Win",highlight
	if 0 not in m[0] and 0 not in m[1] and 0 not in m[2]:
		return "Tie",""
	return None,""

def ConverttoDict(m):
	board = {}
	for row in range(1,4):
		for col in range(1,4):
			if m[row-1][col-1] == 0:
				board['c'+str(col)+'r'+str(row)] = "None.png"
			elif m[row-1][col-1] == 1:
				board['c'+str(col)+'r'+str(row)] = "CircleBig.png"
			elif m[row-1][col-1] == 2:
				board['c'+str(col)+'r'+str(row)] = "CrossBig.png"
	return board

def ConverttoString(big_board,turn,win):
	board_s = ""
	for row in range(3):
		for col in range(3):
			board_s += str(big_board[row][col])
			if col < 2:
				board_s += "."
		if row < 2:
			board_s += "/"
	board_s += "/"+str(turn)
	board_s += "/"+win
	return board_s

def ConverttoMatrix(board_s):
	board_split = board_s.split("/")
	turn = int(board_split[-2])
	win = board_split[-1]
	board_split.pop(-1)
	big_board = []
	for x in range(3):
		big_board.append(board_split[x].split("."))
		for y in range(3):
			big_board[x][y] = int(big_board[x][y])
	return big_board, turn, win

def compMove(m):
	count=0
	for x in range(2):
		for y in range(3):
			if (m[y][0]==m[y][1] and m[y][2]==0 and m[y][0]==(2-x) and count==0):
				m[y][2]=2
				count+=1
			elif (m[y][2]==m[y][1] and m[y][0]==0 and m[y][2]==(2-x)and count==0):
				m[y][0]=2
				count+=1
			elif (m[y][0]==m[y][2] and m[y][1]==0 and m[y][2]==(2-x)and count==0):
				m[y][1]=2
				count+=1
			elif (m[0][y]==m[1][y] and m[2][y]==0 and m[0][y]==(2-x)and count==0):
				m[2][y]=2
				count+=1
			elif (m[0][y]==m[2][y] and m[1][y]==0 and m[0][y]==(2-x)and count==0):
				m[1][y]=2
				count+=1
			elif (m[2][y]==m[1][y] and m[0][y]==0 and m[1][y]==(2-x)and count==0):
				m[0][y]=2
				count+=1
			elif (m[1][1]==m[0][0] and m[2][2]==0 and m[1][1]==(2-x)and count==0):
				m[2][2]=2
				count+=1
			elif (m[1][1]==m[2][2] and m[0][0]==0 and m[1][1]==(2-x)and count==0):
				m[0][0]=2		 
				count+=1
			elif (m[2][2]==m[0][0] and m[1][1]==0 and m[2][2]==(2-x)and count==0):
				m[1][1]=2
				count+=1
			elif (m[2][0]==m[0][2] and m[1][1]==0 and m[0][2]==(2-x)and count==0):
				m[1][1]=2
				count+=1
			elif (m[0][2]==m[1][1] and m[2][0]==0 and m[1][1]==(2-x)and count==0):
				m[2][0]=2
				count+=1
			elif (m[1][1]==m[2][0] and m[0][2]==0 and m[1][1]==(2-x)and count==0):
				m[0][2]=2
				count+=1
	if (count==0) and(0 in m[0] or 0 in m[1] or 0 in m[2]):
		randomMove(m)
        return m

def randomMove(m):
	row=random.randint(0,2)
	col=random.randint(0,2)
	if m[row][col]>0:
		randomMove(m)
	else:
		m[row][col]=2
	return m
	


#-----------Done--------------------------
def make_move_crazy(m,row,col,turn):
  if m[row][col]>0:
    pass
  else:
    if turn==1:
      m[row][col]=1
      turn=2
    else:
      m[row][col]=2
      turn=1
  return m,turn
#-----------Done---------------------------



#-----------------Done (I think)-----------
def checkifwon_crazy(m,win):
  for x in range(3):
    #check horizontal
    if (m[x][0]==m[x][1]==m[x][2]) and (m[x][0]>0) and win==0:      
      return "Win", m[x][0]
    elif (m[0][x]==m[1][x]==m[2][x]) and (m[2][x]>0)and win==0:
      #checking vertical
      return "Win",m[0][x]
  #Checks diagonals
  if (m[0][0]==m[1][1]==m[2][2]) and (m[2][2]>0)and win==0:
    return "Win",m[1][1]
  elif (m[2][0]==m[1][1]==m[0][2]) and (m[1][1]>0)and win==0:
    return "Win", m[1][1]
  if 0 not in m[0] and 0 not in m[1] and 0 not in m[2]:
    return "Tie", 3
  return None, 0
#------------------Done-------------------------------

def checkifwon_crazy_f(win_t):
  if (win_t[0]==win_t[1]==win_t[2]) and (win_t[1]>0):
    return "Win",win_t[0]
  elif (win_t[3]==win_t[4]==win_t[5]) and (win_t[4]>0):
    return "Win",win_t[4]
  elif (win_t[6]==win_t[7]==win_t[8]) and (win_t[7]>0):
    return "Win",win_t[7]
  elif (win_t[0]==win_t[3]==win_t[6]) and (win_t[0]>0):
    return "Win",win_t[0]
  elif (win_t[1]==win_t[4]==win_t[7]) and (win_t[4]>0):
    return "Win",win_t[4]
  elif (win_t[2]==win_t[5]==win_t[8]) and (win_t[5]>0):
    return "Win",win_t[5]
    #Checks diagonals
  elif win_t[0]==win_t[4]==win_t[8] and (win_t[4]>0):
    return "Win",win_t[4]
  elif win_t[6]==win_t[4]==win_t[2] and (win_t[4]>0):
    return "Win", win_t[4]
  elif 0 not in win_t:
    return "Tie", 3
  return " ", 0

def ConverttoDict_crazy(m):
  board = {}
  for table in range(1,10):
    for row in range(1,4):
      for col in range(1,4):
        if m[table-1][row-1][col-1] == 0:
          board['t'+str(table)+'c'+str(col)+'r'+str(row)] = "NoneSmall.png"
        elif m[table-1][row-1][col-1] == 1:
          board['t'+str(table)+'c'+str(col)+'r'+str(row)] = "CircleSmall.png"
        elif m[table-1][row-1][col-1] == 2:
          board['t'+str(table)+'c'+str(col)+'r'+str(row)] = "CrossSmall.png"
  return board

def ConverttoString_crazy(big_board,turn,win_t,win):
  board_s = ""
  for game in range(9):
    for row in range(3):
      for col in range(3):
        board_s += str(big_board[game][row][col])
        if col < 2:
          board_s += "."
      if row < 2:
        board_s += "/"
    board_s += "/"+str(win_t[game])
    if game < 8:
      board_s += ","
  board_s += ","+str(turn)
  board_s += ","+win
  return board_s

def ConverttoMatrix_crazy(board_s):
  board_split = board_s.split(",")
  win_t = []
  win = board_split[-1]
  turn = int(board_split[-2])
  big_board = []
  for z in range(9):
    big_board.append(board_split[z].split("/"))
    win_t.append(int(big_board[z][-1]))
    big_board[z].pop(-1)
    for x in range(3):
      big_board[z][x]=big_board[z][x].split(".")
      for y in range(3):
        big_board[z][x][y] = int(big_board[z][x][y])
  return big_board, turn, win_t,win

