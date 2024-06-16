nama = ["Yogi Ario Pratama", '2313020004', "1J", "Merge"]
for i in nama:
    print(i)

def cekncombine(arkiri, arkanan):
    if not len(arkiri) or not len(arkanan):
        return arkiri or arkanan

    result = []
    i, j =0, 0
    while (len(result) < len(arkiri) + len(arkanan)):
        if arkiri[i] < arkanan[j]:
            result.append(arkiri[i])
            i+=1
        else:
            result.append(arkanan[j])
            j+=1

        if j == len(arkanan):
            result.extend(arkiri[i:])
            
        if i == len(arkiri):
            result.extend(arkanan[j:])

    return result

def mergeshort(ar):
    if len(ar) <2:
        return ar
    
    m = int(len(ar)/2)
    left = mergeshort (ar[:m])
    right = mergeshort (ar[m:])

    return cekncombine(left, right)

ar = [33, 31, 40, 8, 12, 17, 25, 42]
print("Array Belum Urut : ")
print(ar);
print("\n")
print("Array Terurut : ")
print(mergeshort(ar))