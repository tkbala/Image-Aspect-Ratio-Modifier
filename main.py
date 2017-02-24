import sys
import getopt
from PIL import ImageFilter
from PIL import Image

infile=''
outfile=''
aratio = -1
myopts, args = getopt.getopt(sys.argv[1:],"a:i:o:")



###############################
# op <- option
# ar <- argument for the option
###############################
for op, ar in myopts:
    if op == '-i':
        infile = ar
    elif op == '-o':
        outfile = ar
    elif op == '-a':
    	aratio = float(ar)
    else:
        print("How to use --> %s -a DesiredAspectRatio -i input -o output" % sys.argv[0])

# Confirmation of the input
print ("Aspect Ratio: %s | Input file : %s | output file: %s" % (aratio,infile,outfile) )

if(aratio != -1):
	im = Image.open(infile)
	#im.show()
	width, height = im.size
	orig_aratio = width*1.0/(height*1.0)
	if(orig_aratio<aratio):
		final_width = aratio*height
		final_width = int(final_width)
		im_resized = im.resize((final_width,height))
		#im_back = im_resized.filter(ImageFilter.GaussianBlur(radius=50))
		im_back = im_resized.filter(ImageFilter.SMOOTH_BLUR)
		im_back.paste(im,((final_width-width)/2,0))
		im_back.show()
	if(orig_aratio>aratio):
		final_height = (width*1.0)/(aratio*1.0)
		final_height = int(final_height)
		im_resized = im.resize((width,final_height))
		im_back = im_resized.filter(ImageFilter.BLUR)
		im_back.paste(im,(0,(final_height-height)/2))
		im_back.save(outfile)
else:
	print ("Aspect Ratio not entered. How to use --> main.py -a DesiredAspectRatio -i input -o output")


 


