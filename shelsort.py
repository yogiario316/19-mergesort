nm = ["Yogi Ario Pratama", "2313020004", "1J", "Shell Short"]
for i in nm:
    print(i)

def shellshort(array, n):
    jarak = int(n/2)
    while jarak > 0:
        for i in range (jarak, n):
            temp = array[i]
            j = i
            if j >= jarak and array [j - jarak] > temp:
                array[j] = array[j - jarak]
                j -= jarak

            array[j] = temp
        jarak = int(jarak/2)
    return array

ar = [33, 31, 40, 8, 12, 17, 25, 42]
print(shellshort(ar, len(ar)))