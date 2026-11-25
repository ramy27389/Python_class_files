matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for row in matrix for num in row ]
print(flat)


colours=["red",'yellow']
objects=['car','pen']
pairs=[(c,o) for c in colours for o in objects]
print(pairs)

pro_pairs = [(c,o) for c,o in zip(colours,objects)]
print(pro_pairs)