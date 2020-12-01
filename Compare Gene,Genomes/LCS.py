# def read_data(file_name):
#     with open(file_name, 'r+') as file:
#         s1 = file.readline().strip()
#         s2 = file.readline().strip()
# 
#     return s1, s2

def longest_com_subseq(s1, s2):
    D = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                D[i+1][j+1] = D[i][j]+1
            else:
                D[i+1][j+1] = max(D[i+1][j], D[i][j+1])

    sub_seq = ''
    i = len(s1)
    j = len(s2)
    while (i != 0 and j != 0):
        if D[i][j] == D[i-1][j]:
            i -= 1
        elif D[i][j] == D[i][j-1]:
            j -= 1
        else:
            sub_seq = s1[i-1] + sub_seq
            i -= 1
            j -= 1

    print (sub_seq)
    return sub_seq


if __name__ == '__main__':
    s1, s2 ="CTCGAT","TACGTC"#read_data("input.txt")
    print(longest_com_subseq(s1, s2))
