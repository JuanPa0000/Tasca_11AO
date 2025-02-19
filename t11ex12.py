with open("/home/cicles/AO/Ex12.txt","w") as f:
    f.write("Juan Pablo\nIker\nIvan\nPere\nEneko")

with open("/home/cicles/AO/Ex12.txt","a") as f:
    f.write("\nJoan\nPep\nDavid\nCarlos")

with open("/home/cicles/AO/Ex12.txt","r") as f:
    f.seek(0)
    lineas=f.readlines()
    print(lineas)
