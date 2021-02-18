def fibonacci(n):
    fn = [0, 1]

    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])
    print(*fn)
fibonacci(int(input()))
