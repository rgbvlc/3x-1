def make_plot(number):
    import pylab
    y=[]
    x=[]
    step=0
    while number!=1:
        if number%2==0:
            number//=2
        else:
            number=number*3+1
        step+=1
        x.append(step)
        y.append(number)
    pylab.plot(x,y)
    pylab.title("Collatz problem plot")
    pylab.xlabel("Step")
    pylab.ylabel("Value")
    pylab.show()




