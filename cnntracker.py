#Code by Timo Mueller @ EMM! Solutions GmbH - and other contributors, see: https://github.com/njoye/CNN-Tracker-v1

# Import the required modules
import dlib #standard dlib (pip install dlib)
import cv2 #standard cv2 (pip install cv2)
import argparse as ap #should already be preinstalled for you (otherwise: pip install argparse)
import skvideo.io #standard skvideo.io (pip install skvideo.io)

#proprietary project "modules"
import select_object #module for selecting an object to track 
import select_roi #module for selecting a Region of Interest
import select_rod #module for selecting a Region of Disinterest


#Set important variables
VIDEO_SRC="/Volumes/INTENSO/Timo/trafficvid2.mp4"
#Source of the video: https://www.youtube.com/watch?v=PNCJQkvALVc, Recorded by "DriveCamUK"

#Set the frame at which the video should start
START_FRAME=500
print("Starting video at frame: " + str(START_FRAME))

#Possible Output/Input parameters for FFmpeg Reader: https://ffmpeg.org/ffmpeg-filters.html#eq
#Set input parameters for FFmpeg
inputparameters={}
print("FFmpegReader input parameters: " + str(inputparameters))

#Set the output paramters for FFmpeg
outputparameters={}
print("FFmpegReader output parameters: " + str(outputparameters))


#TODO
#1. Select region of interest (manually) - done 08/09/2017 - 12:55:00
#2. Select region of disinterest (manually) - done 08/09/2017 - 12:55:00
#3. Include the CNN through the python wrapper into the mix
#4. Use the CNN to detect objects in the ROI and automatically mark them for tracking
#5. When objects hit the ROD, save their location data and remove them from the tracking list

#TODO at some point (after basic functionality)
#1. Select regions of (dis)interest programmatically
#2. Check if the tracker fails and stays at one point (most likely occlusion) and see if the CNN can help



#Main Function from which all the code is controlled
def main(inputparameters={}, outputparameters={}):
    reader = skvideo.io.FFmpegReader(VIDEO_SRC, inputparameters, outputparameters);
    
    current_frame=None #declare empty variable

    idx=0
    for frame in reader.nextFrame(): #break out of the loop as soon as idx hits the frame number
    	if idx==START_FRAME:
    		current_frame=frame#setting the empty variable
    		break
    	else:
    		idx+=1

    print("Current frame is: " + str(idx) + " - starting video")
    
    rois = select_roi.run(current_frame) #passing on the current picture/frame to the select_roi function
    rods = select_rod.run(current_frame) #passing on the current picture/frame to the select_rod function
    # these return something in the form of: 
    # SINGLE -> ROI:[(508, 220, 694, 300)] ROD[(220, 614, 921, 723)]
    # MULTIPLE -> ROI: [(486, 249, 566, 297), (572, 265, 694, 310)] ROD: [(288, 540, 425, 720), (457, 550, 672, 726)]
    # It doesn't make a difference which you take since they are litteraly copy & pasted (same logic)

    if not doRegionsOverlap(rois, rods):
    	# Regions do not overlap, go on

    	pass


    for frame in reader.nextFrame():
		cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
		cv2.imshow("Video", frame)
		# Continue until the user presses ESC key
		if cv2.waitKey(1) == 27: #This is necessary otherwise the video doesn't get shown correctly -> dunno \_ . _ . _/
			break





def sortRegions(region):
	regions = []
	for reg in region:
		# Constructing the roi object for "intersects()"
		tmp = {}
		tmp["bottom_left"] = {}
		tmp["top_right"] = {}
		
		tmp["bottom_left"]["x"] = reg[0]
		tmp["bottom_left"]["y"] = reg[1]
		tmp["top_right"]["x"] = reg[2]
		tmp["top_right"]["y"] = reg[3]
		regions.append(tmp)
	return regions

#Checks if the ROI and ROD are not overlapping -> that would mean no tracking is necessary ... dafuq ?
#Overlapping ROI and ROI / ROD and ROD are allowed , even though it's a little unnecessary and could waste
#precious time if used extremely bad ... but seriously, then that's your own fault
def doRegionsOverlap(rois, rods):
	for roi in rois:
		# Constructing the roi object for "intersects()"
		roiob = {}
		roiob["bottom_left"] = {}
		roiob["top_right"] = {}
		
		roiob["bottom_left"]["x"] = roi[0]
		roiob["bottom_left"]["y"] = roi[1]
		roiob["top_right"]["x"] = roi[2]
		roiob["top_right"]["y"] = roi[3]

		for rod in rods:
			rodob = {}
			rodob["bottom_left"] = {}
			rodob["top_right"] = {}

			rodob["bottom_left"]["x"] = rod[0]
			rodob["bottom_left"]["y"] = rod[1]
			rodob["top_right"]["x"] = rod[2]
			rodob["top_right"]["y"] = rod[3]

			if intersects(roiob, rodob):
				return True #they intersects, return that and let the main method take care of it
	return False #if it runs until the end -> doesn't return before, everything is fine



# Stolen from https://stackoverflow.com/users/696391/samgak -> thanks though, safed some time:)
# Checks if two rectangles are overlapping
def intersects(roi, rod):
    return not (roi["top_right"]["x"] < rod["bottom_left"]["x"] or roi["bottom_left"]["x"] > rod["top_right"]["x"] or roi["top_right"]["y"] < rod["bottom_left"]["y"] or roi["bottom_left"]["y"] > rod["top_right"]["y"])


#Run the main function
main()









