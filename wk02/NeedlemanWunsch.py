##################################
##################################
##################################
#######     PROBLEM 1     ########
##################################
##################################
##################################


def print_matrix(mat):
    # Loop over all rows
    for i in range(0, len(mat)):
        print("[", end = "")
        # Loop over each column in row i
        for j in range(0, len(mat[i])):
            # Print out the value in row i, column j
            print(mat[i][j], end = "")
            # Only add a tab if we're not in the last column
            if j != len(mat[i]) - 1:
                print("\t", end = "")
        print("]\n")

# A function for making a matrix of zeroes
def zeros(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

# Use these values to calculate scores
gap_penalty = -1
match_award = 1
mismatch_penalty = -1

# Make a score matrix with these two sequences
seq1 = "ATTACA"
seq2 = "ATGCT"

# A function for determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty

# The function that actually fills out the matrix of scores
def needleman_wunsch(seq1, seq2):
    
    # lengths of the two sequences
    n = len(seq1) 
    m = len(seq2)
    
    # generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
    
    ########################
    # Your code starts here
    ########################
    
    # Use the following steps as a guide to calculate the score matrix
    
    # 1. Fill out first column
    
    # 2. Fill out first row
    
    # 3. Fill out all other values in the score matrix

    # Return the final score matrix
    return score

# Test out the needleman_wunsch() function
print_matrix(needleman_wunsch(seq1, seq2))




















##################################
##################################
##################################
#######     PROBLEM 2     ########
##################################
##################################
##################################
exit() # Delete this line once you
       # reach this problem.

def nw_backtrace(seq1, seq2):
    # Calculate score table using the function we wrote earlier
    score = needleman_wunsch(seq1, seq2)
    
    # Create variables to store alignment
    align1 = ""
    align2 = ""
    
    ########################
    # Your code starts here
    ########################
    
    # Back-trace from bottom right of the score matrix
    # and compute the alignment 
    
    return(align1, align2)

output1, output2 = nw_backtrace(seq1, seq2)

print(output1 + "\n" + output2)