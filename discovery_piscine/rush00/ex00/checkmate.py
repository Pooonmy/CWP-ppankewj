ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
QUEEN_DIRS = ROOK_DIRS + BISHOP_DIRS
PAWN_DIRS = [(-1, -1), (-1, 1)]

def parse_board(board_str):
    if not board_str:
        raise Exception("empty board")

    rows = board_str.split("\n")
    size = len(rows)

    for row in rows:
        if len(row) != size:
            raise Exception("board isn't square")

    return rows


def find_king(rows):
    king_pos = None

    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char == "K":
                if king_pos is not None:
                    raise Exception("more than one King")
                king_pos = (r, c)

    if king_pos is None:
        raise Exception("no King on the board")

    return king_pos


def slides_to_king(rows, start, directions, king_pos, size):
    start_r, start_c = start

    for dr, dc in directions:
        r, c = start_r + dr, start_c + dc
        while 0 <= r < size and 0 <= c < size:
            if (r, c) == king_pos:
                return True
            if rows[r][c] in "KPBRQ":
                break
            r += dr
            c += dc

    return False


def pawn_attacks_king(pos, king_pos):
    pr, pc = pos
    return king_pos in [(pr + dr, pc + dc) for dr, dc in PAWN_DIRS]


def is_in_check(rows):
    size = len(rows)
    king_pos = find_king(rows)

    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char == "R" and slides_to_king(rows, (r, c), ROOK_DIRS, king_pos, size):
                return True
            if char == "B" and slides_to_king(rows, (r, c), BISHOP_DIRS, king_pos, size):
                return True
            if char == "Q" and slides_to_king(rows, (r, c), QUEEN_DIRS, king_pos, size):
                return True
            if char == "P" and pawn_attacks_king((r, c), king_pos):
                return True

    return False


def checkmate(board_str):
    try:
        rows = parse_board(board_str)
        in_check = is_in_check(rows)
    except Exception as exc:
        print(f"Error: {exc}")
        return
    
    if in_check:
        print("Success")
    else:  
        print("Fail")
