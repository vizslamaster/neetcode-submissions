def concatenate(s1: str, s2: str) -> str:
    
    concatenatedString = s1 + s2
    
    if(len(concatenatedString) > 10):
        return "Too long!"
    else:
        return concatenatedString




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
