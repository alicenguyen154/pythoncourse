#nhap vao thang cua 1 nam, cho biet thang thuoc quy may cua nam
#input: a = thang cua nam (1->12)
#output: quy cua nam (I, II, III, IV)

def thangquy(a):
    if a<3:
        print 'quy I'
    else:
        if a<6:
            print 'quy II'
        else:
            if a<9:
                print 'quy III'
            else:
                print 'quy IV'

thangquy(3)
