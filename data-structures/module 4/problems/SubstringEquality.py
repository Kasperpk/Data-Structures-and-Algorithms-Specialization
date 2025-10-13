def substring_equality(s,a,b,l):
    if s[a:a+l] == s[b:b+l]:
        return print('Yes')
    else:
        return print('No')
    
if __name__ == '__main__':
    # Read the input string
    string = input().strip()  # strip() removes any trailing whitespace
    
    # Read number of queries
    n_queries = int(input())
    
    # Process each query
    for _ in range(n_queries):
        # Read a, b, l from one line
        a, b, l = map(int, input().split())
        
        # Call substring_equality and let it print the result
        substring_equality(string, a, b, l)