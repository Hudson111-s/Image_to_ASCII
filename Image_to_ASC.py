import PIL.Image as PILI
# Test image path's: (test_images\Bob.jpg), (test_images\Lisa.jpg)

# ASCII in descending value of "darkness"
ASCII = ["@", "#", "%", "?", "!", "+", "*", ";", ":", ",", "."]

# Checks every pixel's color value and divides it by 25 to give it the index value for ASCII
def PtoA(image) -> list:
    pixels = image.getdata()
    ASC = "".join(ASCII[p//25] for p in pixels)
    return(ASC)

def main():

    # Gets path to image 
    while True:
        path = input("Path: ")
        try: 
            image = PILI.open(path).convert("L")
        except:
            print("Not a valid path")
        else:
            break

    # W = Width        
    W = image.size[0]

    # Converts every pix to ASCII
    ASC = PtoA(image)
    
    # Finds total amount of pixels 
    total_pix = len(ASC)
    
    # Joins each line of ASCII with a new line 
    final_image = "\n".join(ASC[i:(i+W)] for i in range(0, total_pix, W))

    # Writes results in results
    with open("results/ASCII.txt", "w") as file:
        file.write(final_image)
main()
