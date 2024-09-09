
board = {'wrook1':'a1','wknight1':'b1','wbishop1':'c1','wqueen':'d1','wking':'e1','wbishop2':'f1','wknight2':'g1','wrook2':'h1',
        'wpawn1':'a2','wpawn2':'b2','wpawn3':'c2','wpawn4':'d2','wpawn5':'e2','wpawn6':'f2','wpawn7':'g2','wpawn8':'h2',
        'brook1':'a8','bknight1':'b8','bbishop1':'c8','bqueen':'d8','bking':'e8','bbishop2':'f8','bknight2':'g8','brook2':'h8',
        'bpawn1':'a7','bpawn2':'b7','bpawn3':'c7','bpawn4':'d7','bpawn5':'e7','bpawn6':'f7','bpawn7':'g7','bpawn8':'h7'}

columns = ['a','b','c','d','e','f','g','h']
rows = ['1','2','3','4','5','6','7','8']
validPosition = [f'{col}{row}' for col in columns for row in rows]

def isValidChessBoard(board):
    
    # validate the positions of the pieces 
    
    for piece, position in board.items():
        if position not in validPosition:
            print(f'invalid move: {position}') 
            return False
            
    #count the pawns for both white and black 
    
    whitePawnCount = 0 
    blackPawnCount = 0 
    for piece in board: 
        if piece.startswith('wp'):
            whitePawnCount += 1 
        if piece.startswith('bp'):
            blackPawnCount += 1
    if whitePawnCount != 8 or blackPawnCount != 8:
        print(f'white has {whitePawnCount} pawns and black has {blackPawnCount} pawns')
        return False
        
    #check the number of pieces per player
    
    whiteTotalCount = 0 
    blackTotalCount = 0 
    
    for piece in board:
        if piece.startswith('w'):
            whiteTotalCount += 1
        if piece.startswith('b'):
            blackTotalCount += 1 
            
    if whiteTotalCount != 16 or blackTotalCount != 16:
        print(f'white has {whiteTotalCount} and black has {blackTotalCount} total each')
        return False
        
    # do we have exactly 1 white king and exactly 1 black king 
    
    wkingcount = 0
    bkingcount = 0
    for piece in board.keys():
        if piece == 'wking':
            wkingcount += 1 
        if piece == 'bking':
            bkingcount += 1
    if wkingcount != 1 or bkingcount != 1:
        print('kings dont have exactly have 1')
        return False
    
        
    print('all checks pass, valid chess board')
    return True
    

print(isValidChessBoard(board))
