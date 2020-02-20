class nfibo():
      def SumOfList(self,list1):
            sol = 0
            for i in list1:
                  sol = sol+i
            return sol

      def __init__(self,n,m):
            self.n=n
            self.m=m
            


            list1 = []
            for i in range(n):
                  list1.append(0)
                  if i == n-1:
                        list1.append(1)



            list1.remove(list1[0])

            for i in range(m-n):
                  list1.append(self.SumOfList(list1[i:n+i+1]))
            print(list1)
s
try:
      [n,m]=input('give num').split(' ')
      n,m = int(n),int(m)
except:
      print(0)
num = nfibo(n,m)
