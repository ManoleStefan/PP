def cereVarsta(varsta):
    try:
        assert int(varsta) > 18
    except ValueError:
        return "Interzis minorilor"
    else:
        return "Haaatz Johnuleeee"


def cereVarstaa(varsta):
    if int(varsta) > 18:
        return "Haaatz Johnuleeee"
    else:
        raise ZeroDivisionError


print(cereVarsta("ciaia bai"))
print(cereVarsta(60))
print(cereVarsta(6))

try:
    print(cereVarstaa("ciaia bai"))
    print(cereVarstaa(60))
    print(cereVarstaa(6))
except ZeroDivisionError:
    print("Prea mic ! ")
