# Notations
# Colors: R,G,B,Y,O,W
# Rotations: F,f, B,b, L,l, R,r, U,u, D,d
# https://www.rubiks.com/en-uk/rubiks-cube-3x3-guide#content1

class Game:
  cube = []

  def __init__(self):
    self.resetCube()

  def resetCube(self):
    def generateBlock(xC, yC, zC):
      return {
        'z': 'R' if zC == 0 else ('O' if zC == 2 else ''),
        'y': 'Y' if yC == 0 else ('W' if yC == 2 else ''),
        'x': 'B' if xC == 0 else ('G' if xC == 2 else ''),
      }

    self.cube = map(lambda x:
      map(lambda y:
        map(lambda z:
          generateBlock(x, y, z)
        , range(0,3))
      , range(0,3))
    , range(0,3))

  def rotate(self, rotation):
    if rotation in ['L', 'R', 'U', 'D', 'F', 'B']:
      direction = 0
    else:
      direction = 1 # can be an elifz

    if rotation in ['L', 'l', 'R', 'r']:
      axis = 'x'
    elif rotation in ['U', 'u', 'D', 'd']:
      axis = 'y'
    elif rotation in ['F', 'f', 'B', 'b']:
      axis = 'z'

    if rotation in ['L', 'l', 'F', 'f', 'U', 'u']:
      index = 0
    elif rotation in ['R', 'r', 'B', 'b', 'D', 'd']:
      index = 2

    def _cube(x,y,val=None):
      _c = self.cube[0][x][y]
      if axis == 'x': _c = self.cube[index][x][y]
      if axis == 'y': _c = self.cube[x][index][y]
      if axis == 'z': _c = self.cube[x][y][index]
      if val:
        if axis == 'x': self.cube[index][x][y] = val
        if axis == 'y': self.cube[x][index][y] = val
        if axis == 'z': self.cube[x][y][index] = val
      return _c

    for y in range(0, 2):
      _bl = [_cube(0,y), _cube(y,2), _cube(2,2-y), _cube(2-y,0)]
      tmp = _bl[0]
      if direction == 0:
        _cube(0,y, _bl[1])
        _cube(y,2, _bl[2])
        _cube(2,2-y, _bl[3])
        _cube(2-y,0, tmp)
      else:
        _cube(0,y, _bl[3])
        _cube(2-y,0, _bl[2])
        _cube(2,2-y, _bl[1])
        _cube(y,2, tmp)
      for block in _bl:
        if axis == 'x': block['y'], block['z'] = block['z'], block['y']
        if axis == 'y': block['x'], block['z'] = block['z'], block['x']
        if axis == 'z': block['y'], block['x'] = block['x'], block['y']

    self.draw()
    pass

  def draw(self):
    def _c(x,y,z, axis):
      return self.cube[x][y][z][axis]

    for i in reversed(range(0,3)):
      print('    | '+_c(0,0,i,'y')+_c(1,0,i,'y')+_c(2,0,i,'y')+' |')
    #     | YYY |
    #     | YYY |
    #     | YYY |
    print('---------------------')

    for i in range(0,3):
      print(_c(0,i,2,'x')+_c(0,i,1,'x')+_c(0,i,0,'x')+' | '+_c(0,i,0,'z')+_c(1,i,0,'z')+_c(2,i,0,'z')+' | '+_c(2,i,0,'x')+_c(2,i,1,'x')+_c(2,i,2,'x')+' | '+_c(2,i,2,'z')+_c(1,i,2,'z')+_c(0,i,2,'z'))
    # BBB | RRR | GGG | OOO
    # BBB | RRR | GGG | OOO
    # BBB | RRR | GGG | OOO
    print('---------------------')

    for i in range(0,3):
      print('    | '+_c(0,2,i,'y')+_c(1,2,i,'y')+_c(2,2,i,'y')+' |')
    #     | WWW |
    #     | WWW |
    #     | WWW |

    return None

# face = [c00, c10, c20]

# import main
# g=main.Game()
# g.rotate('L')
# g.draw()
