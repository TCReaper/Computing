k = int(input("Enter the number of pairs: "))

def brackets(out, open, close, pairs):
	try:
		a = out[k*2-1]
		print(out)
	except:
		if open <= pairs + k + 1:
			brackets(out + '(', open + 1, close, pairs)
		if close <= open + k + 1:
			brackets(out + ')', open, close + 1, pairs)

brackets('',0,0,k)
        
