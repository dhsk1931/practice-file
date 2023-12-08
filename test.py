
def isPalindrome(s):
	return s == s[::-1]
    return s


s = "abbbaa"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
