void checkPrime with int n thus
	ok = 0.
	d = 2.
	while d <= n/2 && ok == 0 then
		if n % d == 0 then
			ok = 1.,
		d += 1.
	if ok == 0 then
		print "n is a prime number".
	else
		print "n is NOT a prime number"..