def buchstaben_zählen(wort):
    count = 0
    
    for buchstabe in wort:
        if buchstabe.isalpha():
            count += 1
            
    return count

print(buchstaben_zählen("Hallo, Berlin!"))        
