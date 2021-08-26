from __future__ import print_function
import cv2 as cv
import argparse

def createImagePyramid(imgName):
    print("""
    Demonstration of magnification ([i]) and reduction([0])
    ------------------
    * [m] -> Magnification
    * [r] -> Reduction
    * [ESC] -> Close our program
    """)
    
    filename = imgName
    
    src = cv.imread(cv.samples.findFile(filename))

    
    if src is None:
        print ('Error while opening image!')
        return -1
    
    while True:
        rows, cols, _channels = map(int, src.shape)
        
        cv.imshow('Kurs: image pyramid.', src)
        
        
        k = cv.waitKey(0)
        if k == 27:
            break
        
        elif chr(k) == 'm':
            src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))
            print ('Magnification: Image x 2')
        
        elif chr(k) == 'r':
            src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))
            print ('Reduction: Image / 2')
            
    cv.destroyAllWindows()
    return 0

parser = argparse.ArgumentParser(description='Kurs: Haar detection.')
parser.add_argument('--camera', help='Camera number:', type=int, default=0)

args = parser.parse_args()
cameraDevice = args.camera

cap = cv.VideoCapture(cameraDevice)

if not cap.isOpened:
    print('Error while opening video!')
    exit(0)

imgCounter = 0
while True:
    ret, frame = cap.read()
    if frame is None:
        print('No captured frame!')
        break

    k = cv.waitKey(10)
    if k == 27:
        break
    
    elif k == 32:       
        imgName = "facedetect{}.png".format(imgCounter)
        cv.imwrite(imgName, frame)
        print("{} written!".format(imgName))
        createImagePyramid(imgName)
        imgCounter += 1
