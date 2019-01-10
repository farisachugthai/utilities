def gcdIter(a, b):
    orig_b = b
    orig_a = a
    if a > b:
        while(b > 0):
            if a % b == 0 and orig_b % b == 0:
                return b
            b -= 1
    else:
        while(a > 0):
            if b % a == 0 and orig_a % a == 0:
                return a
            a -= 1

# alright you fucked this up. 
# let's think about gcd(9, 12). It returned 6. 
# a decrements and then when it gets to 6, 12 % 6 == 0. So it works.
# You need to save the original values of both variables in tmp vars
# and then when you run the if a % b == 0, you need to do that in the form of
# if a % b and original_b % b == 0 then you're good.
# honestly it took more typing to write these comments but i don't feel
# like rewriting this code i wanna move forward.
