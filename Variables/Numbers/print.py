if __name__ == "__main__":
    n = int(input())
    arr = map(int, n)
    arr = list(set(list(arr)))
    print(arr)
