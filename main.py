def roman_to_int(s: str) -> int:
    """
    Given a roman numeral as a string return its integer value
    >>> roman_to_int("III")
    3
    >>> roman_to_int("LVIII")
    58
    >>> roman_to_int("MCMXCIV")
    1994
    >>> roman_to_int("")
    0
    >>> roman_to_int("MCMXCI")
    1991
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            val -= roman[s[i]]
        else:
            val += roman[s[i]]
    return val


if __name__ == "__main__":
    import doctest
    doctest.testmod()
