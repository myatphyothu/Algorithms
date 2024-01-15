import sys

def inverse_s(A,start,end):
    for i in range(start,end):
        if (A*i) % end == 1:
            return i


if __name__ == '__main__':
    script, A, start, end = sys.argv
    print(inverse_s(int(A), int(start),int(end)))