import sys

def solve():
    
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, x, k = map(int, line1)
    s = sys.stdin.readline().strip()
    
    first_hit_time = -1
    current_pos = x
    for i in range(n):
        if s[i] == 'L':
            current_pos -= 1
        else:
            current_pos += 1
        
        if current_pos == 0:
            first_hit_time = i + 1
            break
    
    if first_hit_time == -1 or first_hit_time > k:
        print(0)
        return

    time_rem = k - first_hit_time
    cycle_time = -1
    current_pos = 0
    for i in range(n):
        if s[i] == 'L':
            current_pos -= 1
        else:
            current_pos += 1
        
        if current_pos == 0:
            cycle_time = i + 1
            break
            
    if cycle_time == -1:
        print(1)
    else:
        print(1 + (time_rem // cycle_time))

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()
