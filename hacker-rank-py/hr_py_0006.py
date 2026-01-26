if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #here set is used to get the unique elements
    arr = set(arr)
    arr = sorted(arr)
    print(arr[-2])

    
   
