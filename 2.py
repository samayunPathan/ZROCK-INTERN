def isSubstring(s1, s2):
	return s1.index(s2) if s2 in s1 else False
	 
	

s1 = input('enter string which test : ')
s2 = input('enter string which found :')
res = isSubstring(s1, s2)
if res:
	print(f"Present at index {str(res)}")
else:
	print("Not Found!")
	


