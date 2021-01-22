import wget
print("ClassiCube SkinFetch")

name = str(input("insert player name (make sure your lowercase and uppercase is correct)> "))
url = "http://classicube.s3.amazonaws.com/skin/" +name +".png"
wget.download(url)
print("\nSkin downloaded!")