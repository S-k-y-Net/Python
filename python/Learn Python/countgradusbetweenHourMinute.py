def hm(h,m):

	smin = 6
	hmin = 0.5
	grad = 30
	f = abs(h*30 + m*0.5 - m*6)
	print(f)


def timec(h1,m1,h2,m2):
	h = h1 +h2
	m = m1 + m2
	if m == 60:
		m = 0
		h += 1
	if h > 12:
		h = h % 12
	return h,m
 
hm(timec(14,30,4,0)[0],timec(14,30,4,0)[1])
