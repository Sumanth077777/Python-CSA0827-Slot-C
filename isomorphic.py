def isIsomorphic(str1, str2):    
    char_map = {}  
    if len(str1) != len(str2):  
        return False  
    for i in range(len(str1)):    
        if str1[i] not in char_map:  
  
            if str2[i] in char_map.values():  
                return False  
            char_map[str1[i]] = str2[i]  
        else:  
            if char_map[str1[i]] != str2[i]:  
                return False
    return True
str1 = input("Enter the first str1 :")
str2 = input("Enter the second str2 :") 
if isIsomorphic(str1, str2):  
    print(" True ")  
else:  
    print(" False ")  
