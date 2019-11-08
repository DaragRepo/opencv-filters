import numpy as np
import cv2
#
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('/home/mohamed/Videos/Videos/my videos/films/my movies/Babys.Day.Out.1994.720p.WEB-DL.900MB.ShAaNiG.mkv')
# # #
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     # gray = cv2.cvtColor(frame, cv2.IMREAD_UNCHANGED)
#     # blur = cv2.blur(frame, (5,5))
#     median = cv2.medianBlur(frame, 7)
#     canny = cv2.Canny(frame, 100, 200)
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     cv2.imshow('median',median)
#     cv2.imshow('cannny',canny)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# #
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
# cap.read() returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
# ----------------------------------------- write a video ----------------------------------------------------------------------------

#The image is flipped according to the value of flipCode as follows:

# flipcode = 0: flip vertically
# flipcode > 0: flip horizontally
# flipcode < 0: flip vertically and horizontally
#
cap = cv2.VideoCapture(0)
#
# # Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 100.0, (640,480))
#
while(cap.isOpened()):
    print(cap.read()[0])
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
# ----------------------------------------- write a video ----------------------------------------------------------------------------





