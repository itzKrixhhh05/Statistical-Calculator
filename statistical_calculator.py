import sys
import numpy as np
import math as m
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
#                        MEAN
# ==========================================================

def mean_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        result=sum(data)/a
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def mean_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        result=sum(list(map(lambda x,y: x*y,x,freq)))/sum(freq)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def mean_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        result=sum(list(map(lambda x,y: x*y,mid,freq)))/sum(freq)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def MEAN():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        mean_indi()
    if n==2:
        mean_disc()
    if n==3:
        mean_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                        MEDIAN
# ==========================================================

def median_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        data.sort()
        if a%2==0:
            result=(data[a//2 -1]+data[a//2])/2
        else:
            result=data[a//2]
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def median_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        pairs=sorted(zip(x,freq),key=lambda p:p[0])
        x=[p[0] for p in pairs]
        freq=[p[1] for p in pairs]

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        half=n/2
        result=None
        for i in range(len(cf)):
            if cf[i]>=half:
                result=x[i]
                break
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def median_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        half=n/2

        idx=None
        for i in range(len(cf)):
            if cf[i]>=half:
                idx=i
                break

        L=xl[idx]
        h=xu[idx]-xl[idx]
        f_med=freq[idx]
        cf_before=cf[idx-1] if idx>0 else 0

        result=L+((half-cf_before)/f_med)*h
        print(result)

        # ---- Ogive graph (cumulative frequency curve) ----
        plt.plot(xu,cf,marker='o')
        plt.axhline(half,color='red',linestyle='--',label='N/2')
        plt.axvline(result,color='green',linestyle='--',label='Median')
        plt.title("Ogive - Cumulative Frequency Curve")
        plt.xlabel("Upper Class Boundary")
        plt.ylabel("Cumulative Frequency")
        plt.legend()
        plt.show()

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def MEDIAN():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        median_indi()
    if n==2:
        median_disc()
    if n==3:
        median_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                        QUARTILES
# ==========================================================

def quartiles_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        data.sort()
        n=a
        result={}
        for k,label in [(1,"Q1"),(2,"Q2"),(3,"Q3")]:
            pos=k*(n+1)/4
            lower=int(m.floor(pos))
            frac=pos-lower
            if lower<1:
                val=data[0]
            elif lower>=n:
                val=data[-1]
            else:
                val=data[lower-1]+frac*(data[lower]-data[lower-1])
            result[label]=val
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def quartiles_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        pairs=sorted(zip(x,freq),key=lambda p:p[0])
        x=[p[0] for p in pairs]
        freq=[p[1] for p in pairs]

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        result={}
        for k,label in [(1,"Q1"),(2,"Q2"),(3,"Q3")]:
            pos=k*n/4
            val=None
            for i in range(len(cf)):
                if cf[i]>=pos:
                    val=x[i]
                    break
            result[label]=val
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def quartiles_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        result={}
        for k,label in [(1,"Q1"),(2,"Q2"),(3,"Q3")]:
            pos=k*n/4
            idx=None
            for i in range(len(cf)):
                if cf[i]>=pos:
                    idx=i
                    break
            L=xl[idx]
            h=xu[idx]-xl[idx]
            f_q=freq[idx]
            cf_before=cf[idx-1] if idx>0 else 0
            val=L+((pos-cf_before)/f_q)*h
            result[label]=val
        print(result)

        plt.plot(xu,cf,marker='o')
        for label,val in result.items():
            plt.axvline(val,linestyle='--',label=label)
        plt.title("Ogive - Quartiles")
        plt.xlabel("Upper Class Boundary")
        plt.ylabel("Cumulative Frequency")
        plt.legend()
        plt.show()

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def QUARTILES():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        quartiles_indi()
    if n==2:
        quartiles_disc()
    if n==3:
        quartiles_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                        MODE
# ==========================================================

def mode_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        result=pd.Series(data).mode().tolist()
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def mode_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))

        maxf=max(freq)
        result=[x[i] for i in range(len(x)) if freq[i]==maxf]
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def mode_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))

        maxf=max(freq)
        idx=freq.index(maxf)

        L=xl[idx]
        h=xu[idx]-xl[idx]
        f1=freq[idx]
        f0=freq[idx-1] if idx>0 else 0
        f2=freq[idx+1] if idx<len(freq)-1 else 0

        result=L+((f1-f0)/((2*f1)-f0-f2))*h
        print(result)

        plt.bar(rang,freq,color='skyblue',edgecolor='black')
        plt.axvline(rang[idx],color='red',linestyle='--',label='Modal Class')
        plt.title("Histogram - Mode")
        plt.xlabel("Class Interval")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def MODE():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        mode_indi()
    if n==2:
        mode_disc()
    if n==3:
        mode_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                    GEOMETRIC MEAN
# ==========================================================

def gm_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        result=m.exp(sum(list(map(lambda x:m.log(x),data)))/a)
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def gm_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        result=m.exp(sum(list(map(lambda x,y:y*m.log(x),x,freq)))/sum(freq))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def gm_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        result=m.exp(sum(list(map(lambda x,y:y*m.log(x),mid,freq)))/sum(freq))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def GM():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        gm_indi()
    if n==2:
        gm_disc()
    if n==3:
        gm_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                    HARMONIC MEAN
# ==========================================================

def hm_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        result=a/sum(list(map(lambda x:1/x,data)))
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def hm_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        result=sum(freq)/sum(list(map(lambda x,y:y/x,x,freq)))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def hm_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        result=sum(freq)/sum(list(map(lambda x,y:y/x,mid,freq)))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def HM():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        hm_indi()
    if n==2:
        hm_disc()
    if n==3:
        hm_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                        RANGE
# ==========================================================

def range_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        result=max(data)-min(data)
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def range_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        result=max(x)-min(x)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def range_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        result=max(xu)-min(xl)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def RANGE():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        range_indi()
    if n==2:
        range_disc()
    if n==3:
        range_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                  QUARTILE DEVIATION
# ==========================================================

def qd_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        data.sort()
        n=a
        qvals={}
        for k,label in [(1,"Q1"),(3,"Q3")]:
            pos=k*(n+1)/4
            lower=int(m.floor(pos))
            frac=pos-lower
            if lower<1:
                val=data[0]
            elif lower>=n:
                val=data[-1]
            else:
                val=data[lower-1]+frac*(data[lower]-data[lower-1])
            qvals[label]=val
        qd=(qvals["Q3"]-qvals["Q1"])/2
        coeff=(qvals["Q3"]-qvals["Q1"])/(qvals["Q3"]+qvals["Q1"])
        print("Q1=",qvals["Q1"],"Q3=",qvals["Q3"])
        print("result= ",qd,"  Coefficient of QD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def qd_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        pairs=sorted(zip(x,freq),key=lambda p:p[0])
        x=[p[0] for p in pairs]
        freq=[p[1] for p in pairs]

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        qvals={}
        for k,label in [(1,"Q1"),(3,"Q3")]:
            pos=k*n/4
            val=None
            for i in range(len(cf)):
                if cf[i]>=pos:
                    val=x[i]
                    break
            qvals[label]=val
        qd=(qvals["Q3"]-qvals["Q1"])/2
        coeff=(qvals["Q3"]-qvals["Q1"])/(qvals["Q3"]+qvals["Q1"])
        print("Q1=",qvals["Q1"],"Q3=",qvals["Q3"])
        print(qd,"  Coefficient of QD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def qd_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))

        cf=[]
        run=0
        for f in freq:
            run+=f
            cf.append(run)

        n=sum(freq)
        qvals={}
        for k,label in [(1,"Q1"),(3,"Q3")]:
            pos=k*n/4
            idx=None
            for i in range(len(cf)):
                if cf[i]>=pos:
                    idx=i
                    break
            L=xl[idx]
            h=xu[idx]-xl[idx]
            f_q=freq[idx]
            cf_before=cf[idx-1] if idx>0 else 0
            val=L+((pos-cf_before)/f_q)*h
            qvals[label]=val
        qd=(qvals["Q3"]-qvals["Q1"])/2
        coeff=(qvals["Q3"]-qvals["Q1"])/(qvals["Q3"]+qvals["Q1"])
        print("Q1=",qvals["Q1"],"Q3=",qvals["Q3"])
        print(qd,"  Coefficient of QD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def QD():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        qd_indi()
    if n==2:
        qd_disc()
    if n==3:
        qd_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                    MEAN DEVIATION
# ==========================================================

def md_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        mean=sum(data)/a
        result=sum(list(map(lambda x:abs(x-mean),data)))/a
        coeff=result/mean
        print("Mean= ",mean)
        print("result= ",result,"  Coefficient of MD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def md_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        mean=sum(list(map(lambda x,y:x*y,x,freq)))/sum(freq)
        result=sum(list(map(lambda x,y:y*abs(x-mean),x,freq)))/sum(freq)
        coeff=result/mean
        print("Mean= ",mean)
        print(result,"  Coefficient of MD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def md_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        mean=sum(list(map(lambda x,y:x*y,mid,freq)))/sum(freq)
        result=sum(list(map(lambda x,y:y*abs(x-mean),mid,freq)))/sum(freq)
        coeff=result/mean
        print("Mean= ",mean)
        print(result,"  Coefficient of MD= ",coeff)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def MD():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        md_indi()
    if n==2:
        md_disc()
    if n==3:
        md_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                        VARIANCE
# ==========================================================

def variance_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        mean=((sum(data))/a)**2
        sqr=(sum(list(map(lambda x:x**2,data))))/a
        result=(sqr-mean)
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def variance_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        mean=(sum(list(map(lambda x,y: x*y,x,freq)))/sum(freq))**2
        sqr=(sum(list(map(lambda x,y:x*x*y,x,freq))))/sum(freq)
        result=(sqr-mean)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def variance_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mean=(sum(list(map(lambda x,y: x*y,list(map(lambda x,y:(x+y)/2 ,xl,xu)),freq)))/sum(freq))**2
        sqr=(sum(list(map(lambda x,y:x*x*y,list(map(lambda x,y:(x+y)/2 ,xl,xu)),freq))))/sum(freq)
        result=(sqr-mean)
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def VARIANCE():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        variance_indi()
    if n==2:
        variance_disc()
    if n==3:
        variance_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                  STANDARD DEVIATION
# ==========================================================

def sd_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        mean=((sum(data))/a)**2
        sqr=(sum(list(map(lambda x:x**2,data))))/a
        result= m.sqrt((sqr-mean))
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def sd_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        mean=(sum(list(map(lambda x,y: x*y,x,freq)))/sum(freq))**2
        sqr=(sum(list(map(lambda x,y:x*x*y,x,freq))))/sum(freq)
        result=m.sqrt((sqr-mean))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def sd_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mean=(sum(list(map(lambda x,y: x*y,list(map(lambda x,y:(x+y)/2 ,xl,xu)),freq)))/sum(freq))**2
        sqr=(sum(list(map(lambda x,y:x*x*y,list(map(lambda x,y:(x+y)/2 ,xl,xu)),freq))))/sum(freq)
        result=m.sqrt((sqr-mean))
        print(result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def SD():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        sd_indi()
    if n==2:
        sd_disc()
    if n==3:
        sd_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#                COEFFICIENT OF VARIATION
# ==========================================================

def cv_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        mean=sum(data)/a
        sqr=(sum(list(map(lambda x:x**2,data))))/a
        sd=m.sqrt(sqr-mean**2)
        result=(sd/mean)*100
        print("Mean= ",mean,"  SD= ",sd)
        print("result= ",result,"%")

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def cv_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        mean=sum(list(map(lambda x,y: x*y,x,freq)))/sum(freq)
        sqr=(sum(list(map(lambda x,y:x*x*y,x,freq))))/sum(freq)
        sd=m.sqrt(sqr-mean**2)
        result=(sd/mean)*100
        print("Mean= ",mean,"  SD= ",sd)
        print(result,"%")

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def cv_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        mean=sum(list(map(lambda x,y: x*y,mid,freq)))/sum(freq)
        sqr=(sum(list(map(lambda x,y:x*x*y,mid,freq))))/sum(freq)
        sd=m.sqrt(sqr-mean**2)
        result=(sd/mean)*100
        print("Mean= ",mean,"  SD= ",sd)
        print(result,"%")

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def CV():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        cv_indi()
    if n==2:
        cv_disc()
    if n==3:
        cv_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#        FIRST FOUR MOMENTS, SKEWNESS AND KURTOSIS
# ==========================================================

def moments_indi():
    data=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input("Enter Data: "))
            data.append(b)
        print("data =",format(data))
        mean=sum(data)/a
        m1=sum(list(map(lambda x:(x-mean),data)))/a
        m2=sum(list(map(lambda x:(x-mean)**2,data)))/a
        m3=sum(list(map(lambda x:(x-mean)**3,data)))/a
        m4=sum(list(map(lambda x:(x-mean)**4,data)))/a
        beta1=(m3**2)/(m2**3)
        gamma1=m3/(m2**1.5)
        beta2=m4/(m2**2)
        gamma2=beta2-3
        print("Mean= ",mean)
        print("m1=",m1," m2=",m2," m3=",m3," m4=",m4)
        print("Skewness: beta1=",beta1," gamma1=",gamma1)
        print("Kurtosis: beta2=",beta2," gamma2=",gamma2)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def moments_disc():
    x=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter x{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            x.append(b)
            freq.append(c)

        data=pd.DataFrame(freq,index=x,columns=["fi"])
        print("data =\n",format(data))
        n=sum(freq)
        mean=sum(list(map(lambda x,y:x*y,x,freq)))/n
        m1=sum(list(map(lambda x,y:y*(x-mean),x,freq)))/n
        m2=sum(list(map(lambda x,y:y*(x-mean)**2,x,freq)))/n
        m3=sum(list(map(lambda x,y:y*(x-mean)**3,x,freq)))/n
        m4=sum(list(map(lambda x,y:y*(x-mean)**4,x,freq)))/n
        beta1=(m3**2)/(m2**3)
        gamma1=m3/(m2**1.5)
        beta2=m4/(m2**2)
        gamma2=beta2-3
        print("Mean= ",mean)
        print("m1=",m1," m2=",m2," m3=",m3," m4=",m4)
        print("Skewness: beta1=",beta1," gamma1=",gamma1)
        print("Kurtosis: beta2=",beta2," gamma2=",gamma2)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def moments_conti():
    xl=[]
    xu=[]
    freq=[]
    try:
        a=int(input("Enter Number of Terms: "))
        for i in range(a):
            b=int(input(f"Enter Lower Limit{i+1}: "))
            d=int(input(f"Enter Upper Limit{i+1}: "))
            c=int(input(f"Enter f{i+1}: "))
            xl.append(b)
            xu.append(d)
            freq.append(c)
        rang=list(map(lambda x,y:((str(x) +"-"+str(y))),xl,xu))
        data=pd.DataFrame(freq,index=rang,columns=["fi"])
        print("data =\n",format(data))
        mid=list(map(lambda x,y:(x+y)/2 ,xl,xu))
        n=sum(freq)
        mean=sum(list(map(lambda x,y:x*y,mid,freq)))/n
        m1=sum(list(map(lambda x,y:y*(x-mean),mid,freq)))/n
        m2=sum(list(map(lambda x,y:y*(x-mean)**2,mid,freq)))/n
        m3=sum(list(map(lambda x,y:y*(x-mean)**3,mid,freq)))/n
        m4=sum(list(map(lambda x,y:y*(x-mean)**4,mid,freq)))/n
        beta1=(m3**2)/(m2**3)
        gamma1=m3/(m2**1.5)
        beta2=m4/(m2**2)
        gamma2=beta2-3
        print("Mean= ",mean)
        print("m1=",m1," m2=",m2," m3=",m3," m4=",m4)
        print("Skewness: beta1=",beta1," gamma1=",gamma1)
        print("Kurtosis: beta2=",beta2," gamma2=",gamma2)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


def MOMENTS():
    print('''Select Which Type of Data you have
             1.Individual
             2.Discrete
             3.Continuous
             4.Exit'''
    )
    n=int(input("Enter 1 , 2 , 3 or 4 : "))
    if n==1:
        moments_indi()
    if n==2:
        moments_disc()
    if n==3:
        moments_conti()
    if n==4:
        print("Thank you for using")
        sys.exit()


# ==========================================================
#           COVARIANCE (paired x,y individual data)
# ==========================================================

def COVARIANCE():
    x=[]
    y=[]
    try:
        a=int(input("Enter Number of Pairs: "))
        for i in range(a):
            b=float(input(f"Enter x{i+1}: "))
            c=float(input(f"Enter y{i+1}: "))
            x.append(b)
            y.append(c)

        data=pd.DataFrame({"x":x,"y":y})
        print("data =\n",format(data))

        xbar=sum(x)/a
        ybar=sum(y)/a
        result=sum(list(map(lambda xi,yi:(xi-xbar)*(yi-ybar),x,y)))/a
        print("x_bar= ",xbar,"  y_bar= ",ybar)
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


# ==========================================================
#      KARL PEARSON'S COEFFICIENT OF CORRELATION
# ==========================================================

def CORRELATION():
    x=[]
    y=[]
    try:
        a=int(input("Enter Number of Pairs: "))
        for i in range(a):
            b=float(input(f"Enter x{i+1}: "))
            c=float(input(f"Enter y{i+1}: "))
            x.append(b)
            y.append(c)

        data=pd.DataFrame({"x":x,"y":y})
        print("data =\n",format(data))

        xbar=sum(x)/a
        ybar=sum(y)/a
        cov=sum(list(map(lambda xi,yi:(xi-xbar)*(yi-ybar),x,y)))/a
        sx=m.sqrt(sum(list(map(lambda xi:(xi-xbar)**2,x)))/a)
        sy=m.sqrt(sum(list(map(lambda yi:(yi-ybar)**2,y)))/a)
        result=cov/(sx*sy)
        print("Covariance= ",cov,"  SDx= ",sx,"  SDy= ",sy)
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


# ==========================================================
#                  RANK CORRELATION (SPEARMAN)
# ==========================================================

def RANK_CORRELATION():
    x=[]
    y=[]
    try:
        a=int(input("Enter Number of Pairs: "))
        for i in range(a):
            b=float(input(f"Enter x{i+1}: "))
            c=float(input(f"Enter y{i+1}: "))
            x.append(b)
            y.append(c)

        rx=pd.Series(x).rank(ascending=False,method='average').tolist()
        ry=pd.Series(y).rank(ascending=False,method='average').tolist()

        d=list(map(lambda p,q:p-q,rx,ry))
        d2=list(map(lambda z:z**2,d))

        data=pd.DataFrame({"x":x,"y":y,"Rx":rx,"Ry":ry,"d":d,"d^2":d2})
        print("data =\n",format(data))

        n=a
        result=1-((6*sum(d2))/(n*(n**2-1)))
        print("result= ",result)

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


# ==========================================================
#                       REGRESSION
# ==========================================================

def REGRESSION():
    x=[]
    y=[]
    try:
        a=int(input("Enter Number of Pairs: "))
        for i in range(a):
            b=float(input(f"Enter x{i+1}: "))
            c=float(input(f"Enter y{i+1}: "))
            x.append(b)
            y.append(c)

        data=pd.DataFrame({"x":x,"y":y})
        print("data =\n",format(data))

        xbar=sum(x)/a
        ybar=sum(y)/a
        cov=sum(list(map(lambda xi,yi:(xi-xbar)*(yi-ybar),x,y)))/a
        varx=sum(list(map(lambda xi:(xi-xbar)**2,x)))/a
        vary=sum(list(map(lambda yi:(yi-ybar)**2,y)))/a

        byx=cov/varx
        bxy=cov/vary
        r=cov/m.sqrt(varx*vary)

        print("x_bar= ",xbar,"  y_bar= ",ybar)
        print("Regression coefficient byx (Y on X)= ",byx)
        print("Regression coefficient bxy (X on Y)= ",bxy)
        print("Correlation coefficient r= ",r)
        print(f"Regression Line Y on X:  Y - {ybar} = {byx} (X - {xbar})")
        print(f"Regression Line X on Y:  X - {xbar} = {bxy} (Y - {ybar})")

        xs=np.linspace(min(x),max(x),100)
        y_on_x=ybar+byx*(xs-xbar)
        ys=np.linspace(min(y),max(y),100)
        x_on_y=xbar+bxy*(ys-ybar)

        plt.scatter(x,y,color='black',label='Data Points')
        plt.plot(xs,y_on_x,color='blue',label='Y on X')
        plt.plot(x_on_y,ys,color='red',label='X on Y')
        plt.title("Regression Lines")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()

    except ValueError:
        print("enter a valid number")

    finally:
        print("Thank you for using")


# ==========================================================
#                    MAIN MENU
# ==========================================================

def MAIN():
    print('''Select What You Want To Find
             1.Mean
             2.Median
             3.Quartiles
             4.Mode
             5.Geometric Mean
             6.Harmonic Mean
             7.Range
             8.Quartile Deviation
             9.Mean Deviation
             10.Standard Deviation (Variance also shown via option 17)
             11.Coefficient of Variation
             12.First Four Moments, Skewness and Kurtosis
             13.Covariance (x , y)
             14.Karl Pearson's Coefficient of Correlation
             15.Rank Correlation
             16.Regression (Y on X and X on Y)
             17.Variance
             18.Exit''')
    n=int(input("Enter your choice (1-18): "))
    if n==1:
        MEAN()
    if n==2:
        MEDIAN()
    if n==3:
        QUARTILES()
    if n==4:
        MODE()
    if n==5:
        GM()
    if n==6:
        HM()
    if n==7:
        RANGE()
    if n==8:
        QD()
    if n==9:
        MD()
    if n==10:
        SD()
    if n==11:
        CV()
    if n==12:
        MOMENTS()
    if n==13:
        COVARIANCE()
    if n==14:
        CORRELATION()
    if n==15:
        RANK_CORRELATION()
    if n==16:
        REGRESSION()
    if n==17:
        VARIANCE()
    if n==18:
        print("Thank you for using")
        sys.exit()


while True:
    MAIN()
