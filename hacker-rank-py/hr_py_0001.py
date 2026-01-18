def print_formatted(number):
    # your code goes here
    max_width = len(format(number, 'b'))
    for decimal in range(1, number+1):
        print(f"{decimal:>{max_width}} {decimal:>{max_width}o} {decimal:>{max_width}X} {decimal:>{max_width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)