while True:
    N = int(input())
    if N == -1:
        break
    arr = [i for i in range(1,N) if N % i == 0]
    if sum(arr) == N:
        newArr = " + ".join(map(str, arr))
        print(f"{N} = {newArr}")
    else:
        print(f"{N} is NOT perfect.")