     if n < 1:
            return "Argument must be an integer greater than 0."
    
    result = ""
    for i in range(1, n + 1):
        result += str(i)
        
        if i < n:
            result += " "
    
    return result
