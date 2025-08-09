if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score=max(arr)
    
    filter_max=[]
    for i in arr:
        if i != max_score:
            filter_max.append(i)
    runner_up=max(filter_max)
    
    print(runner_up)
