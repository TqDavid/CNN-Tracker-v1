#Code by Timo Mueller @ EMM! Solutions GmbH - and other contributors, see: https://github.com/njoye/CNN-Tracker-v1

#In this file the region of interest will be selected 
#inside the regions of interest, the CNN will search for 
#objects and give their coordinates to the tracker, so that
#the tracker is then able to follow those objects.
#It is possible to set multiple regions of interest

# Import the required modules
import cv2
import argparse



def run(im):

    im_disp = im.copy()
    im_draw = im.copy()
    window_name = "Select Region(s) of Interest"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, im_draw)

    # List containing top-left and bottom-right to crop the image.
    pts_1 = []
    pts_2 = []

    rects = []
    run.mouse_down = False

    def callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            run.mouse_down = True
            pts_1.append((x, y))
        elif event == cv2.EVENT_LBUTTONUP and run.mouse_down == True:
            run.mouse_down = False
            pts_2.append((x, y))
            print "ROI selected at [{}, {}]".format(pts_1[-1], pts_2[-1])
        elif event == cv2.EVENT_MOUSEMOVE and run.mouse_down == True:
            im_draw = im.copy()
            cv2.rectangle(im_draw, pts_1[-1], (x, y), (0,255,0), 2) #green rectangle for ROI
            cv2.imshow(window_name, im_draw)

    print("\n-------------")
    print("ROI SELECTION")
    print("-------------\n")

    print "Press, drag and release your mouse to select your Regions of Interest"
    cv2.setMouseCallback(window_name, callback)

    print "Press key `p` to continue with the selected ROIs."
    print "Press key `d` to discard the last object selected."
    print "Press key `q` to quit the program."

    while True:
        # Draw the rectangular boxes on the image
        window_name_2 = "Current ROI Selection"
        for pt1, pt2 in zip(pts_1, pts_2):
            rects.append([pt1[0],pt2[0], pt1[1], pt2[1]])
            cv2.rectangle(im_disp, pt1, pt2, (0, 255, 0), 2)
        # Display the cropped images
        cv2.namedWindow(window_name_2, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name_2, im_disp)
        key = cv2.waitKey(30)
        if key == ord('p'):
            # Press key `s` to return the selected points
            cv2.destroyAllWindows()
            point= [(tl + br) for tl, br in zip(pts_1, pts_2)]
            corrected_point=check_point(point)
            return corrected_point
        elif key == ord('q'):
            # Press key `q` to quit the program
            print "Quitting without saving."
            exit()
        elif key == ord('d'):
            # Press ket `d` to delete the last rectangular region
            if run.mouse_down == False and pts_1:
                print "ROI deleted at  [{}, {}]".format(pts_1[-1], pts_2[-1])
                pts_1.pop()
                pts_2.pop()
                im_disp = im.copy()
            else:
                print "No ROI to delete."
    cv2.destroyAllWindows()
    point= [(tl + br) for tl, br in zip(pts_1, pts_2)]
    corrected_point=check_point(point)
    return corrected_point

def check_point(points): #checks if the points are set correctly and are in bounds of the image
    out=[]
    for point in points:
        #to find min and max x coordinates
        if point[0]<point[2]:
            minx=point[0]
            maxx=point[2]
        else:
            minx=point[2]
            maxx=point[0]
        #to find min and max y coordinates
        if point[1]<point[3]:
            miny=point[1]
            maxy=point[3]
        else:
            miny=point[3]
            maxy=point[1]
        out.append((minx,miny,maxx,maxy))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--imagepath", required=True, help="Path to image")

    args = vars(ap.parse_args())

    try:
        im = cv2.imread(args["imagepath"])
    except:
        print("Cannot read image and exiting.")
        exit()
    points = run(im)
    print("Rectangular Regions of Interest selected are -> ", points)
