from PIL import Image
import numpy as np

def compute_offset(img1_path, img2_path):
    # Try to import cv2, if not available, we can do a simple search or just print
    try:
        import cv2
        im1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
        
        # We only want to compare the static parts.
        # The collar/chest area is from Y=500 to Y=700, X=300 to X=700
        crop1 = im1[500:700, 300:700]
        crop2 = im2[500:700, 300:700]
        
        res = cv2.matchTemplate(crop2, crop1[50:150, 50:350], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # crop1 center in crop1 is (50, 50) relative offset.
        # max_loc gives top-left of the match in crop2.
        dx = max_loc[0] - 50
        dy = max_loc[1] - 50
        print(f"Calculated Offset: dx={dx}, dy={dy}")
        
    except ImportError:
        print("cv2 not found, cannot auto-align. Please ask user.")

compute_offset('ikemen.png', 'ikemen_blink.png')
