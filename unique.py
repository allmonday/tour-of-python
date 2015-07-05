def foo():
    a = [1,3,5,6,7,8,9,[1,2,3,4,1,2,3,2,3],[4,2,1]]
    result = set()

    for aa in a:
        if type(aa) is list:
            for aaa in aa:
                result.add(aaa)
        else:
            result.add(aa);
    return result

