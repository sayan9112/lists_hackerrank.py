# Enter your code here. Read input from STDIN. Print output to STDOUT
l = []

for _ in range(int(raw_input())):
    line = raw_input().strip()
    if line == "print":
        print l
        continue
    parts = line.split()
    getattr(l, parts[0])(*(map(int, parts[1:])))