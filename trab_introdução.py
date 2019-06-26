import cv2
img = cv2.imread("eduardo_desenho.jpg", cv2.IMREAD_COLOR)
stylization = cv2.stylization(img)
cv2.imshow('eduardo', stylization)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("eduardo_result.png", stylization)
