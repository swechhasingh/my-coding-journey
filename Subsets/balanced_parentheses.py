from collections import deque

def generate_balanced_parentheses(N):
    """generate all combination of 'N' pairs of balanced parentheses."""
    result = deque()
    result.append(("",0,0))
    all_combs = []
    while result:
        n_comb = len(result)
        for i in range(n_comb):
            # add left parentheses
            curr_comb = result.popleft()
            if curr_comb[1] < N:
                result.append((curr_comb[0]+"(",curr_comb[1]+1,curr_comb[2]))
                
            # add right parentheses
            if curr_comb[1] > curr_comb[2]:
                result.append((curr_comb[0]+")",curr_comb[1],curr_comb[2]+1))

            if curr_comb[1] == N and curr_comb[2] == N:
                all_combs.append(curr_comb[0])
    return all_combs

def generate_balanced_parentheses_rec(N):
    results = []
    generate_balanced_parentheses_recursive("", 0, 0, N, results)
    return results

def generate_balanced_parentheses_recursive(curr, left_count, right_count, N, results):
    if left_count == N and right_count == N:
        results.append(curr)
        return
    if left_count < N:
        generate_balanced_parentheses_recursive(curr + "(", left_count+1, right_count, N, results)
    if right_count < left_count:
        generate_balanced_parentheses_recursive(curr + ")", left_count, right_count+1, N, results)



def main():
    print(f"All combinations of balanced parentheses are: {generate_balanced_parentheses_rec(2)}")
    print(f"All combinations of balanced parentheses are: {generate_balanced_parentheses_rec(3)}")


main()