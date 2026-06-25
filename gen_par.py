par=[]
def p(i,par,o,n,c):
    if len(par)==2*n:
        print("".join(par))
        return
    if o<n:
    	par.append("(")
    	p(i+1,par,o+1,n,c)
    	par.pop()
    if c<o:
    	par.append(")")
    	p(i+1,par,o,n,c+1)
    	par.pop()
n=int(input())
p(0, par, 0, n, 0)  



