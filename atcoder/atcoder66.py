A = list(input())
B = list(input())
C = list(input())
turn = A[0]

while True:
  if turn == 'a':
    if A == []:
      print('A')
      break
    turn = A.pop(0)
  elif turn == 'b':
    if B == []:
      print('B')
      break
    turn = B.pop(0)
  elif turn == 'c':
    if C == []:
      print('C')
      break
    turn = C.pop(0)
    
    