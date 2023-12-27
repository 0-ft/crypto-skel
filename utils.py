import math
import builtins

ilevel = 0
def indent():
    global ilevel
    ilevel += 1

def dedent():
    global ilevel
    ilevel -= 1

def print(s):
    global ilevel
    id = '   ' * ilevel
    builtins.print(id + str(s).replace('\n', '\n' + id))
    # builtins.print('   ' * ilevel, end='')
    # builtins.print(*args, **kwargs)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def mod_inverse(x, n):
    """
    Compute the modular inverse of x modulo n using the Extended Euclidean Algorithm
    """
    print(f"computing modular inverse of {x} mod {n}")
    indent()
    assert math.gcd(x, n) == 1
    print(f"{x} is coprime to {n} ✅")
    if n == 1:
        return 0
    original_x = x
    original_n = n

    eq = []

    indent()
    while x > 1:
        q = n // x
        m = n % x
        print(f"{n} = {q} * {x} + {m}")
        eq.append((n, q, x, m))

        n = x
        x = m
    dedent()

    # print("backtracking...")
    # print(eq)
    a, b = 0, 1
    for n, q, x, m in reversed(eq):
        a, b = b, a - q * b

        # n, x = x, (n - q * x) % original_n
    assert a * original_n + b * original_x == 1
    print(f"solved ax + bn = 1: a = {a}, b = {b}")

    if a < 0:
        a += original_n
        print(f"negative a, a+n={a+original_n}")
    if b < 0:
        b += original_x
        print(f"negative b, b+n={b+original_n}")

    inv = pow(original_x, -1, original_n)

    assert (original_x * inv) % original_n == 1
    print(f"modular inverse of {original_x} mod {original_n} is {inv} 🏁")
    dedent()
    return inv
    
def double_and_add(a, b):
    print(f"computing {a} * {b} using double and add algorithm")
    indent()    
    # Initialize the accumulator and the count of addition operations
    accumulator = 0
    addition_count = 0

    # Convert a and b to binary representations of the same length
    # b_binary = bin(b)[2:].zfill(len(bin(a)[2:]))
    # # a_binary = bin(a)[2:]
    b_binary = bin(b)[2:]
    

    # Display the binary forms of a and b
    print(f"b = {b} = {b_binary}\n")

    # Print the header for the table
    header = f"│ {'i':<6} │ {'2^i':<10} │ {'a*2^i':<10} │ {'b bit':<6} │ {'Accumulator':<12} │ {'Operation':<24} │"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    # Iterate over each bit in the binary representation of b
    for i, bit in enumerate(b_binary[::-1]):
        step = i
        if step > 0:
            operations = ["Double a"]
            addition_count += 1
        else:
            operations = []
        two_i = 2 ** step
        a_doubled = a * two_i

        # If the bit is 1, add 'a' to the accumulator and increment the addition count
        if bit == '1':
            accumulator += a_doubled
            addition_count += 1  # One for doubling 'a', one for addition to accumulator
            operations += ["Add to Accum"]

        # Print the current step details
        print(f"│ {step:<6} │ {two_i:<10} | {a_doubled:<10} │ {bit:<6} │ {accumulator:<12} │ {', '.join(operations):<24} │")

    # Print the closing line of the table
    print('└' + '─' * (len(header) - 2) + '┘')

    # Print the final result and the count of addition operations
    assert accumulator == a * b
    print(f"\nResult: {accumulator}")
    print(f"Total addition operations: {addition_count}")
    dedent()
    return accumulator


def square_and_multiply(base, exponent):
    print(f"Computing {base} ^ {exponent} using square and multiply algorithm")
    indent()

    # Initialize the accumulator and the count of multiplication operations
    accumulator = 1
    multiplication_count = 0

    # Convert the exponent to binary representation
    exponent_binary = bin(exponent)[2:]

    # Display the binary form of the exponent
    print(f"exponent = {exponent} = {exponent_binary}\n")

    # Print the header for the table
    header = f"│ {'i':<6} │ {'2^i':<10} │ {'Base^2^i':<12} │ {'Exp bit':<8} │ {'Accumulator':<12} │ {'Operation':<24} │"
    print('┌' + '─' * (len(header) - 2) + '┐')
    print(header)
    print('├' + '─' * (len(header) - 2) + '┤')

    # Iterate over each bit in the binary representation of the exponent
    base_squared = base
    for i, bit in enumerate(exponent_binary[::-1]):
        step = i

        if step > 0:
            base_squared = base_squared ** 2
            operations = ["Square base"]
            multiplication_count += 1
        else:
            operations = []

        # If the bit is 1, multiply the accumulator with the base
        if bit == '1':
            accumulator *= base_squared
            multiplication_count += 1
            operations += ["Multiply with Accum"]

        # Print the current step details
        print(f"│ {step:<6} │ {2 ** step:<10} │ {base_squared:<12} │ {bit:<8} │ {accumulator:<12} │ {', '.join(operations):<24} │")

    # Print the closing line of the table
    print('└' + '─' * (len(header) - 2) + '┘')

    # Print the final result and the count of multiplication operations
    assert accumulator == base ** exponent
    print(f"\nResult: {accumulator}")
    print(f"Total multiplication operations: {multiplication_count}")
    dedent()
    return accumulator

# for tt in range(t.n):
#     if t.encrypt(tt, pk[0]) == 94755:
#         print(tt)
# mod_inverse(11, 17)