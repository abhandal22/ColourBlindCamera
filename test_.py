import pytest
from PIL import Image, ImageChops

from main import convertColour

# Can be run using "py -m pytest test_.py" to see results in terminal

def testDeuteranomalyImagesAreIdentical1():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly1.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 0, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()
    
def testDeuteranomalyImagesAreIdentical2():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly2.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 1, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical3():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly3.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 2, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical4():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly4.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 3, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical5():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly5.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 4, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical6():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly6.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 5, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical7():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly7.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 6, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical8():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly8.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 7, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical9():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly9.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 8, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testDeuteranomalyImagesAreIdentical10():
    expected = Image.open("data\deuteranomalyData\expectedDeuteranomaly10.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 9, "deuteran")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical1():
    expected = Image.open("data\protanomalyData\expectedProtanomaly1.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 0, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical2():
    expected = Image.open("data\protanomalyData\expectedProtanomaly2.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 1, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical3():
    expected = Image.open("data\protanomalyData\expectedProtanomaly3.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 2, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical4():
    expected = Image.open("data\protanomalyData\expectedProtanomaly4.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 3, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical5():
    expected = Image.open("data\protanomalyData\expectedProtanomaly5.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 4, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical6():
    expected = Image.open("data\protanomalyData\expectedProtanomaly6.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 5, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()
    
def testProtanomalyImagesAreIdentical7():
    expected = Image.open("data\protanomalyData\expectedProtanomaly7.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 6, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical8():
    expected = Image.open("data\protanomalyData\expectedProtanomaly8.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 7, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical9():
    expected = Image.open("data\protanomalyData\expectedProtanomaly9.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 8, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testProtanomalyImagesAreIdentical10():
    expected = Image.open("data\protanomalyData\expectedProtanomaly10.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 9, "protan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical1():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly1.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 0, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical2():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly2.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 1, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical3():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly3.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 2, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical4():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly4.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 3, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical5():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly5.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 4, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical6():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly6.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 5, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical7():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly7.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 6, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()

def testTritanomalyImagesAreIdentical8():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly8.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 7, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()    

def testTritanomalyImagesAreIdentical9():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly9.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 8, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close()   

def testTritanomalyImagesAreIdentical10():
    expected = Image.open("data\\tritanomalyDate\expectedTritanomaly10.png").convert("RGBA")
    testImage = Image.open("data\\testImage.png")
    result = convertColour(testImage, 9, "tritan")
    # result = Image.open("new.png")
    # print(expected.read() == result.read())
    
    for x in range(0, testImage.width):
        for y in range(0, testImage.height):
            resultColor = result.getpixel((x, y))
            expectedColor = expected.getpixel((x, y))
            assert expectedColor[0] - 1 <= resultColor[0] <= expectedColor[0] + 1
            assert expectedColor[1] - 1 <= resultColor[1] <= expectedColor[1] + 1
            assert expectedColor[2] - 1 <= resultColor[2] <= expectedColor[2] + 1

    expected.close()
    result.close() 

