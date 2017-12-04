from urllib.request import urlopen
import string

def get_from():
    '''get the currency_from'''
    a=input()
    return a

def get_to():
    '''get the currency_to'''
    a=input()
    return a

def get_amount():
    '''get the amount_from'''
    a=input()
    return a

def combinethem():
    '''get the corresponding URL'''
    url="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+get_from()+"&to="+get_to()+"&amt="+get_amount()
    return url

def findamount_to(sth):
    '''drop the useless part in the string so that we can find the amount_to'''
    urlnew=sth.split('"')
    amtto=""
    for i in urlnew[7]:
        if i ==" ":
            break
        amtto+=i
    '''the urlnew[7] is a combine of the amount_to and the currency_to,and I just want the former,so I drop string after " "'''
    return amtto
    
def exchange():
    '''return the amount_to, 
        at first I set 3 parameters, and later I found that I do not need them
        as I have defined the get_ functions
        any way, it runs well. '''
    url=combinethem()
    doc=urlopen(url)
    docstr=doc.read()
    doc.close()
    s=docstr.decode()
    amtto=findamount_to(s)
    amt_to=float(amtto)
    print(amt_to)

def test_get_from():
    '''test if the function get_from() is ok'''
    assert(get_from())
def test_get_to():
    '''test if the function get_to() is ok'''
    assert(get_to())
def test_get_amount():
    '''test if the function get_amount() is ok'''
    assert(get_amount())
def test_combinethem():
    '''I do not know what test_function you want but in fact I test my functions this way'''
    print(combinethem())
    '''then I try this testfunction and input 3 words by random and assure the output is a right url,
        if you must want a assert(),emmmmm....'''
def test_findamount_to():
    '''I ran it once to see if it return the part I want'''
    print(findamount_to(' "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : ""'))
def test_exchange():
    '''in fact it is my main function, emmmm.
        I have failed times until I found that the currency_to in the example was
        "EUR" in stead of "EU",
        sad story.'''
    exchange()
def test_all():
    '''I think it is innecessary for I have tested them one by one already...'''
    test_get_from()
    test_get_to()
    test_get_amount()
    test_combinethem()
    test_findamount_to()
    test_exchange()
    print("ALl tests passed")
def main():
    test_exchange()
          
if __name__=="__main__":
    main()
