
R.<x,y> = PolynomialRing(ZZ, 'x,y')
F.<a> = GF(2 ^ 8)

def test(F):
    """
    None of my stuff has malfunctioned yet!
    Can we celebrate that?

    sage: F.<a> = GF(2 ^ 8)
    sage: if test(F):
    ....:      print("")

    sage:
    

    """

    return len([F.from_integer(i ^^ 0xAA) for i in [0x00..0xFF]]) == 255

test(F)

def numbers():
    11231e123   +   12312e232
    123131233l  -   12331lr
    0x1123312   *   0x123123r
    0o1123132   /   0o123312r
    0b1010001   //  0b0101011r
    12_2312.0   %   12_2312.0r
    12_21e23    ^   0_0e0_0r

    return 1r ^^ 2r & ~1231r | 223r
