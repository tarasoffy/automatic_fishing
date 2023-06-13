import cv2
import pyautogui
import keyboard
import pytesseract
import time

left = 664
top = 440
width = 360
height = 30

#coord fish name
coord_fish_name_left = 575
coord_fish_name_top = 325
coord_fish_name_width = 135
coord_fish_name_height = 30

color = 100

row_bag = 0

color_counter_row = 0

dragn_drop_fish_counter = 0 

dragn_drop_bag_counter_x = 0

start_dragn_drop_fish_coord_x = 650
start_dragn_drop_fish_coord_y = 400


end_dragn_drop_fish_coord_x = 640
end_dragn_drop_fish_coord_y = 840

start_bag_coord_x = 335
start_bag_coord_y = 970

end_bag_coord_x = 1250
end_bag_coord_y = 415


dragn_drop_fish_counter_stash = 0

end_dragn_drop_fish_in_stash_x = 1035 
end_dragn_drop_fish_in_stash_y = 640


def press_tab_space():
    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('tab')

    time.sleep(1)    
        

    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')


def dragn_drop_bag():
    global dragn_drop_bag_counter_x
    global end_bag_coord_x
    global end_bag_coord_y
    global row_bag


    if dragn_drop_bag_counter_x < 6 :
        pyautogui.moveTo(start_bag_coord_x, start_bag_coord_y, duration=0.2)  
        pyautogui.dragTo(end_bag_coord_x, end_bag_coord_y, duration=0.2)  
        end_bag_coord_x +=80
        dragn_drop_bag_counter_x+=1
        print(f'сумка: {dragn_drop_bag_counter_x + 1}')

    if dragn_drop_bag_counter_x == 5:
        dragn_drop_bag_counter_x = 0
        end_bag_coord_x = 1250
        end_bag_coord_y += 80
        row_bag += 1
        print(f'ряд: {row_bag + 1}')

    time.sleep(0.5)
    
    press_tab_space()



def dragn_drop_fish_all():

    global dragn_drop_fish_counter
    global end_dragn_drop_fish_coord_x 

    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('tab')

    time.sleep(2)

    screenshot = pyautogui.screenshot(region=(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, 1, 1))
    screenshot.save('slot.jpg')


    img = cv2.imread('slot.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('slot.jpg', img)

    print(img)

    if(img[0,0] > 15):

        if(dragn_drop_fish_counter < 5):
            pyautogui.moveTo(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, duration=0.2)  
            pyautogui.dragTo(end_dragn_drop_fish_coord_x, end_dragn_drop_fish_coord_y, duration=0.2)  
            end_dragn_drop_fish_coord_x +=80
            dragn_drop_fish_counter+=1
    
        if dragn_drop_fish_counter == 5:
            dragn_drop_fish_counter = 0
            end_dragn_drop_fish_coord_x = 640
            dragn_drop_bag()

        else:
            press_tab_space()
           

    else:
        press_tab_space()




def dragn_drop_fish_rich():
    global dragn_drop_fish_counter
    global end_dragn_drop_fish_coord_x
    global end_dragn_drop_fish_coord_y
    global start_dragn_drop_fish_coord_x
    global start_dragn_drop_fish_coord_y
    global coord_fish_name_left
    global coord_fish_name_top
    global coord_fish_name_width
    global coord_fish_name_height

    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('tab')

    time.sleep(2)

    screenshot = pyautogui.screenshot(region=(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, 1, 1))
    screenshot.save('slot.jpg')


    img = cv2.imread('slot.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('slot.jpg', img)

    print(img)

    if(img[0,0] > 15):

        if(dragn_drop_fish_counter < 5):
            pyautogui.moveTo(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, duration=0.2)  

            screenshot = pyautogui.screenshot(region=(coord_fish_name_left, coord_fish_name_top, coord_fish_name_width, coord_fish_name_height))
            screenshot.save('namefish.jpg')


            image = cv2.imread('namefish.jpg')

            result = pytesseract.image_to_string(image, lang='eng')

            print(result.strip())

            if result != None and result.strip() == 'Maaracnye' or result.strip() == 'Panysxwar opens' or img[0,0] == 83 or img[0,0] == 85 or result.strip() == 'Bensii toncrono6vit' or result.strip() == '| Mopcoii oKyHe:' or img[0,0] == 115:

                pyautogui.dragTo(end_dragn_drop_fish_coord_x, end_dragn_drop_fish_coord_y, duration=0.2)  
                end_dragn_drop_fish_coord_x +=80
                dragn_drop_fish_counter+=1

            else:
                time.sleep(0.5)
                pyautogui.rightClick()
                pyautogui.moveTo(787, 572, duration=0.2)
                pyautogui.click()    
    
        if dragn_drop_fish_counter == 5:
            dragn_drop_fish_counter = 0
            end_dragn_drop_fish_coord_x = 640
            dragn_drop_bag()

        else:
            press_tab_space()

    else:
        press_tab_space()



def rich_fish_stash():

    global dragn_drop_fish_counter_stash
    global coord_fish_name_left
    global coord_fish_name_top
    global coord_fish_name_width
    global coord_fish_name_height
    global end_dragn_drop_fish_in_stash_x
    global end_dragn_drop_fish_in_stash_y

    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('tab')

    time.sleep(2)

    screenshot = pyautogui.screenshot(region=(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, 1, 1))
    screenshot.save('slot.jpg')


    img = cv2.imread('slot.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('slot.jpg', img)

    if(img[0,0] > 15):
        pyautogui.moveTo(start_dragn_drop_fish_coord_x, start_dragn_drop_fish_coord_y, duration=0.2)  

        screenshot = pyautogui.screenshot(region=(coord_fish_name_left, coord_fish_name_top, coord_fish_name_width, coord_fish_name_height))
        screenshot.save('namefish.jpg')


        image = cv2.imread('namefish.jpg')

        result = pytesseract.image_to_string(image, lang='eng')

        if result != None and result.strip() == 'Maaracnye' or result.strip() == 'Panysxwar opens':

            if dragn_drop_fish_counter_stash == 6:
                dragn_drop_fish_counter_stash = 0
                end_dragn_drop_fish_in_stash_x = 1035
                end_dragn_drop_fish_in_stash_y -= 80

            if dragn_drop_fish_counter_stash < 6:
                pyautogui.dragTo(end_dragn_drop_fish_in_stash_x, end_dragn_drop_fish_in_stash_y, duration=0.2)
                dragn_drop_fish_counter_stash += 1
                end_dragn_drop_fish_in_stash_x -= 80

                

             
        else:
            time.sleep(0.5)
            pyautogui.rightClick()
            pyautogui.moveTo(787, 572, duration=0.2)
            pyautogui.click()


    press_tab_space()


def simulate_keystroke(key, index):
    if index < 10:
        keyboard.press(key)
        time.sleep(0.00001)
        keyboard.release(key)

def arr_add():

    global color_counter_row

    result = []

    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')

    time.sleep(1.5)

    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')

    time.sleep(0.5)

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save('screenshot.jpg')

    img = cv2.imread('screenshot.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('gray.jpg', img)


    for x in range(359):

        if img[11, x] > color and img[20, x + 3] > color and img[20, x + 8] > color and img[11, x - 1] < color :
            result.append('w')
        if img[11, x] > color and img[11, x + 1] > color and img[11, x + 2] > color \
            and img[11, x + 3] > color and img[11, x + 4] > color \
            and img[11, x - 1] < color and img[20, x - 1] > color \
            and img[20, x] > color and img[20, x + 1] > color \
            and img[20, x + 2] > color and img[20, x + 3] > color:
            result.append('s')
        if img[11, x] > color and img[11, x + 1] > color and img[11, x - 1] < color \
            and img[18, x] > color and img[18, x - 1] > color and img[18, x - 2] > color \
            and img[18, x + 1] > color and img[18, x + 2] > color and img[18, x + 3] > color :
            result.append('a')

    print(result)

    for index, key in enumerate(result):
        simulate_keystroke(key, index)

    result = []

    dragn_drop_fish_all() # для всей рыбы переносим в сумку

    # dragn_drop_fish_rich() # для дорогой рыбы переносим в сумки

    # rich_fish_stash() # для самой дорогой рыбы оставить у себя



def loading_displaying_saving():

    job = True

    while job:

        screenshot = pyautogui.screenshot(region=(860, 175, 3, 3))
        screenshot.save('btn.jpg')

        img = cv2.imread('btn.jpg', cv2.IMREAD_GRAYSCALE)
        if img[0, 0] > 250:
            job = False
            print('bel')
            arr_add()
            time.sleep(10)   
            job = True         

        time.sleep(0.5)

    

def on_key_press(event):
    if event.name == 'f2':
        loading_displaying_saving()
        # dragn_drop_fish_rich()
        # dragn_drop_fish()
        # rich_fish_stash()

keyboard.on_press(on_key_press)
keyboard.wait('esc')