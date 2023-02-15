def solution(S):
    # write your code in Python 3.8.10

    result = list(S)
    for i in range(len(S)):
        l = i
        r = len(S)-1-i
        if l>=r:
            if l==r and S[l]=='?':
                result[l]='a'
            return ''.join(result)
        if S[l]!='?' and S[r]!='?' and S[l]!=S[r]:
            return 'NO'
        if S[l]=='?' and S[r]=='?':
            result[l], result[r] = 'a', 'a'
        elif S[l]=='?':
            result[l] = result[r]
        elif S[r]=='?':
            result[r] = result[l]



print(solution("?ab??a"))