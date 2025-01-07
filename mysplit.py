def mysplit(strng):
    result = []
    j = 0 #variable to set a starting point
    new_str = ''
    for i in range(len(strng)):
        if ord(strng[i]) != 32:
            new_str += strng[i]
        elif ord(strng[i]) == 32 and len(new_str) != 0:
            result.append(new_str)
            new_str = ''
        if i == len(strng)-1 and len(new_str) != 0:
            result.append(new_str) 
    return result


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
