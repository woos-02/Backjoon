def solution(slice, n):
    if n > slice:
        if n % slice == 0:
            return n // slice
        else:
            return n // slice +1
    else:
        return 1