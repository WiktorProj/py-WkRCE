# WkRCE encoding
# Library

def WkRCEen(string):
    if string == "":
        return
    new = []
    k = 1
    ltring = [char for char in string]
    for i in range(len(ltring)):
        if i != len(ltring) - 1:
            if ltring[i] == ltring[i+1]:
                k += 1
            else:
                if k != 1:
                    new.append("[")
                    new.append(str(k))
                new.append(ltring[i])
                if k != 1:
                    new.append("]")
                k = 1
    new.append(ltring[len(ltring) - 1])
    t = ""
    for i in new: 
        t += i
    return t