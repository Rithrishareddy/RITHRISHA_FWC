# Define the NOT gate as a function
def NOT(x):
    return 0 if x else 1

# Define the logic expression from question 36
def logic_expression(X, Y, Z):
    # First term: [X + Z {Y' + (Z' + X Y')}]
    inner1 = NOT(Y) or (NOT(Z) or (X and NOT(Y)))
    term1 = X or (Z and inner1)
    
    # Second term: [X' + Z'(X + Y)]
    inner2 = X or Y
    term2 = NOT(X) or (NOT(Z) and inner2)
    
    # Final output
    return term1 and term2

# Test all combinations of Y and Z with X = 1
X = 1

print("Y Z | Output")
print("---------")
for Y in [0, 1]:
    for Z in [0, 1]:
        output = logic_expression(X, Y, Z)
        print(f"{Y} {Z} |   {output}")

