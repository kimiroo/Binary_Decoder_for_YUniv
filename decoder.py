print("Binary Decoder for Y_Univ Version 1.2 (by kimiroo)\n\nBinary code to alphabet converter for my univ homework\n~~designed to simplify(?) the decoding process~~")

# Initialize
isList = "f"
done = "f"
out = ""
lett = ""
outLett = ""
lst = ""
loopNo = -1
lstLen = 0
lstTipPnt = 0

while done == "f":
    buffer = 0
    lett = ""
    loopNo = loopNo + 1
    
    print("")
    
    print("Loop: ",str(loopNo))
    
    if isList == "f":
        inp = input("Enter: ")
    
    # Check if it is list
    if inp[0] == "l":
        print("List detected!")
        isList = "t"
        inp = inp.replace("l", "")
        print("Converted:",inp)
        #lst = list(inp)
        #print(lst)
        lst = list(inp.split(","))
        #print(lst)
        lstLen = len(lst)
        lstTipPnt = lstLen - 1
        print("OriLST: ",lst)
        print("len: ", str(len(lst)))
    
    if isList == "t":
        inp = str(lst[loopNo])
    
    if inp == "e":
        done = "t"
        inp = str(11110)
    elif loopNo == lstTipPnt:
        done = "t"
    
    var = "0b" + inp
    
    buffer = int(var, 2)
    if int(buffer) >= 1:
        if int(buffer) <= 26:
            lett = chr(ord('`')+buffer)
            print("Buffer: " + str(buffer),"/",lett)
        else:
            lett = "."
            print("Buffer: " + str(buffer),"/",lett)
    else:
        lett = " "
        print("Buffer: " + str(buffer),"/",lett)
    
    out = out + str(buffer)
    outLett = outLett + str(lett)
    print("Output: " + out,"/",outLett)
    
    # Break loop when 30
    if lett == ".":
        print("BREAK!")
        break
