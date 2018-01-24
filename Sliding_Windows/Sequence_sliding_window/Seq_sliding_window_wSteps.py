"""
AUTHOR: Dale Bridges
CREATION DATE: 24 Jan 2018
ENV: Python 3.6

NAME: Seq_sliding_window_wSteps.py

SLIDING WINDOW ON A SEQUENCE

1.  Sequence is read in from user input
2.  Window size is set (length of seq chunks or k-mers)
3.  Step size is set (default = 1, number of bases to skip before capturing next chunk (k-mer)

"""

def slide(seq, window, step):

    print(seq)
    seqLen = len(seq)
    window

    start, finish, pos = 0, window, 0

    seqRes = []

    for i in range(seqLen): # loop over length of the sequence
        if (0 < window <= seqLen) and (0 < step < window): # check win_size and steps within boundaries

            # WINDOW SETTINGS CALCULATION
            wSeq = seq[start:finish]
            start += step
            finish += step

            if len(wSeq) == window:
                seqRes += [wSeq] # STORE EACH SEQUENCE

                # print output vor visualization
                print(" " * (pos) + wSeq) # shift as per step
                pos = pos + step

        else: # if not within boundaries Error gracefully
            if window == 0:
                print("Window size out of range: The window cannot be set to zero.")
                exit()
            if step == 0:
                print("Window size out of range: Step size cannot be set to zero")
                exit()
            if step >= true_window:
                print("Window size out of range: Step size will not allow for overlap")
                exit()
            if window > (seqLen):
                print("Window size out of range: The window size is greater than the sequence length")
                exit()

    return (seqRes) # returns an array [list] of k-mer chunks

def main():

    # TEST INPUTS
    #seq = "AAAGGGCCCTTT"
    #window = 4
    #step = 1

    # USER DEFINED INPUTS
    seq = input("Enter a sequence: \n").upper()
    window = int(input("Enter a window size: \n"))
    step = int(input("Enter the step size: \n"))

    # SLIDE METHOD
    result = slide(seq, window, step)

    print(result)

    print("Number of windows with window size set to " + str(window) +
          " and step size set to " + str(step) +
          " is: " + str(len(result))
          )

if __name__ == '__main__':
    main()