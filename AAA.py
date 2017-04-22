#encoding:utf-8

#bstring='tomorrow'
#print bstring[1:5]

#print[1,2,3]*2

#numberList=[8,1,2,3]
#for i in reversed(numberList):
#    print i,

#a=9
#b=2
#a,b=b,a
#print a,b

#astring='hello eorld'
#bstring='tomorrow'


#oneElement=(123,)
#if 123 in tuple:
 #   print 'yes'

# formDict = {}.fromkeys(('x','y'),('-1','-2'))
# print  formDict

# firstset=set([1,2,3])
# secondset=set([3,4,5])
# print firstset & secondset
# print firstset - secondset
#
#
# print [x+2 for x in range(6) if x%2]




# def power(x,n=2):
#     s = 1
#     while n>0:
#         n =-1
#         s *=x
#         return s
#
# print power(2)







def division():
    try:
        x =input('Enter the first number:')
        y =input('the second one:')
        print x/y
    except ZeroDivisionError:
        print "The second number cannot be zero!"
    finally:
        print 'whatever success or fail, this sentence will appear'

division()
