
# Define global constant
A = ((5**.5 - 1)/2)  # Golden ratio φ

# Define functions

def h(cpa):
    '''
    Explanation:
        Generates a hash from a given CPA (Código Postal Argentino).
    Params:
        cpa: An string of 8 characters, with numbers and letters (not case sensitive), A9999AAA.
    '''
    # Define hash value
    hashSum = 0

    # Check length condition
    if len(cpa) != 8:
        hashSum = None
    else:
        # Uppercase the CPA
        cpa = cpa.upper()

        # Do a summatory of the unicode code of each character
        summatory = 0
        for i in range(0, 8):
            summatory += ord(cpa[i])

        # Calc the hash of the summatory using the multiplication method (φ)
        hashSum = int(m*(summatory*A % 1))

    # Return the result value
    return hashSum


m = 100
print(h('A9999AAA'))
