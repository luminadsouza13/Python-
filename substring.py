def find(str,ch):
    i=0
    lengthstr=len(str)
    lengthchar=len(ch)
    count=0
    while i < lengthstr :
        j=0
        if str[i]==ch[j] :
                while j < lengthchar :
                    if ch[j] == str[j+i] :
                        count=count+1
                        if count == lengthchar :                           
                            return "substring exists"
                    else :
                        break
                    j=j+1
        i=i+1
    return "substring does not exists"

stringval=raw_input("Enter string\n")
substr=raw_input("Enter substring\n")

print find(stringval,substr)    

    
