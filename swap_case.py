def swap_case(s):
    result = ""
    for char in s:
        if char >= 'a' and char <= 'z':
            result += char.upper()
        elif char >= 'A' and char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result