class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        "convert int to string"
        flag = False
        x_char = str(x)

        "if negative int remove the sign"
        if x_char[0] == '-':
            x_char = x_char[1:]
            flag = True

        "reverse the string"
        rev = x_char[::-1]

        "add the sign if remove before"
        if flag:
            rev = '-' + rev

        "if overflow return 0"
        rev = int(rev)
        if rev > 2**31 - 1 or rev < -2**31:
            rev = 0
        return rev