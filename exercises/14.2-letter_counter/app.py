par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for x in par.lower():
    if x is not " ":
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1    
print(counts)

