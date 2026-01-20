def minion_game(string):
    # your code goes here
    # kevin = 0
    # stuart = 0
    # lis = []
    # vowels = ('A','E','I','O','U')
    
    # size = len(string)
    # for i in range(size):
    #     temp1 = string[i:size]
    #     for j in range(len(temp1)):
    #         temp2 = temp1[0:j+1]
    #         lis.append(temp2)
    
    # for item in lis:
    #     if item.startswith(vowels):
    #         kevin += 1
    #     else:
    #         stuart += 1
            
    
    
    # if kevin > stuart:
    #     print(f'Kevin {kevin}')
    # elif stuart > kevin:
    #     print(f'Stuart {stuart}')
    # else:
    #     print('Draw')
            
    vowels = "AEIOU"
    kevin = 0 
    stuart = 0 
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i #this adds the length of substring starting with vowel
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
    
    return 
                
    

if __name__ == '__main__':
    s = input()
    minion_game(s)