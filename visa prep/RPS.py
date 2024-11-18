vignesh, charan = input().split()
if vignesh == charan:
    print("NULL")
elif (vignesh == "R" and charan == "S") or (vignesh == "S" and charan == "P") or (vignesh == "P" and charan == "R"):
    print("Vignesh")
else:
    print("Charan") 
