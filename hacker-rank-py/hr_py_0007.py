from collections import defaultdict

if __name__ == '__main__':
    scores = defaultdict(list)
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores[score].append(name)
    
    low_score_2 = list(sorted(scores.keys()))[1]
    
    for name in sorted(scores[low_score_2]):
        print(name)
