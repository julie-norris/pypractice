def remove_dups(arr):
	"""removes duplicates from an array and prints the resulting array

	>>> remove_dups([1,2,5,1,7,2,4,2])
	[1 2 5 7 4]
	"""
	L=[]
	store={x:0 for x in arr}
	for el in arr:
		if store[el]==0:
			L.append(el)
			store[el]=1
	print('[' + " ".join(map(str, L)) +']')
		
if __name__ == "__main__":
    import doctest
    doctest.testmod()