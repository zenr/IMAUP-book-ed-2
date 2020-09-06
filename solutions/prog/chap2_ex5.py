import os
import openpyxl
import cv2

book = openpyxl.load_workbook('images.xlsx')
# get all active sheets
sheet = book.active

# get the 9 cells in the first sheet
cells = sheet['A1': 'A9']

# get content of each cell (i.e.,) the file name and create 
# full path by adding the folder name
for c in cells:
    fname = c[0].value # the content of a cell
    fname_path = os.path.join('figure', c[0].value)
    print(fname_path)
    
    # read the content of the file using cv2 and print shape
    im = cv2.imread(fname_path)
    print(im.shape)