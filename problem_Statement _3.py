Write a code that checks if two given strings are anagrams
Sample Input: Mary Army
Output: Yes
  
  def areAnagram(str1, str2):
    str1 = sorted(str1.upper())
    str2 = sorted(str2.upper())
    
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return 0
        
    else:
        return 0
    
    return 1

str1 = "Mary"
str2 = "Army"

if areAnagram(str1, str2):
    print(" Yes")
else:
    print ("No")
