a = [1,3, [1,2,3], [4,2,1]]

result = set()

for aa in a:
    if type(aa) is list:
        for aaa in aa:
            result.add(aaa)
    else:
        result.add(aa);

print result
