# this is test for git pull request
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


def f():
    print('test from master2')

print(solution("?ab??a"))
print('done')

def f2():
   print('from feature22')

# test git pull --rebase
# change in main
