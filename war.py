def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return round(sq ** 0.5, 0)


print(find_next_square(121))
