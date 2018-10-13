def binSearch(A,n):
	if len(A) == 1:
		return A[0] == n
	mid = len(A)//2
	if A[mid] == n:
		return True
	if A[mid] > n:
		return binSearch(A[ : mid],n)
	return binSearch(A[mid : ], n)
