def longestPalindrome(self, s):

	 temp=0
	 dups=[]
	 for ltr in s:
	 	if ltr not in dups:
			dups.append(ltr)
		elif ltr in dups:
            dups.append(ltr)
            g=dups[::-1]
				if g==dups:
                l=len(g)
		else:
        	dups=[1:]
        	g=dups[::-1]
				if g==dups:
					l=len(g)
        if l > temp:
            temp = l
            longest_palindrome=dups
            return ("".join(longest_palindrome))
                
        
		