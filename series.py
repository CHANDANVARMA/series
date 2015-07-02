import os
import math

#How to run first two case and last case?
#For first two case u should comment the ob.smalest_str()
#For last case u should comment the ob.do()
class Series():
    
    dict_glb={}
    def do(self, word):
        series_dict=self.find_dict(word)
        sum_ch=0
        for ch in word:
            sum_ch=sum_ch+self.find_val(ch)
        
        #It will return value for corresponding letter and sum if input is string    
        print sum_ch

    def find_dict(self,word):
        j=[i for i in word]
        j.sort()
        series_dict={'A':1}
        inc=2
        for char in list(map(chr, range(ord('A'), ord(j[-1])))):
            
            value=series_dict[char]*2+inc
            series_dict[chr(ord(char)+1)]=value
            inc=inc+1
        return series_dict

    def smalest_str(self,num):
        s_str=''
        b=num
        while (b!=0):
            d=self.postion(b,1,26)
            x=self.find_val(chr(64+d))
            r=b/x
            s_str=s_str+chr(64+d)*r
            b=b%x
        print s_str
        

    def find_val(self,char):
        #print Series().x
        #IF part created for if we found repeated charecter in string other we need to do
        #the calculation again which is time consuming only thats why using data structure.
        if char in Series().dict_glb:
            return Series().dict_glb[char]
        else:
            char_val= ord(char)-64
            char_sum=0
            for i in range(char_val):
                cal=(char_val-i)*2**i
                char_sum=char_sum+cal
            Series().dict_glb[char]=char_sum
            return char_sum
    def mid(self, first, last):
        t=(first+last)/2
        return t
    def postion(self,num,first,last):
        mid=self.mid(first, last)
        char = chr(64+mid)
        val=self.find_val(char)
        #print num,val,mid,first,last
        if num>=val:
            if num==val:
                return mid
            elif first==mid:
                return mid
            else:
                x=self.postion(num,mid,last)
        else:
            if first==mid:
                return mid
            else:
                x=self.postion(num,first,mid)
        return x
        
if __name__ == '__main__':
    ob=Series()
    #ob.smalest_str(13)
    ob.do('ABZ')
