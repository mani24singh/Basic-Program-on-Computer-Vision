import cv2
img = cv2.imread("harry.png")  
cv2.imshow("HarryPotter",img) 
cv2.imwrite("HarryPotter.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
