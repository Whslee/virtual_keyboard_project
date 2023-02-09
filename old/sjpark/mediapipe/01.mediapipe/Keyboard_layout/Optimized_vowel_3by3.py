import cv2
import time

def Click_effect(fingertip, keyboardImage):

    #PlaySound(TEXT("WavFiles/mouseclick.wav"), NULL, SND_ASYNC)
    #winsound.PlaySound('WavFiles/mouseclick.wav', winsound.SND_FILENAME)
    
    if(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (200, 60), (280, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (280, 60), (360, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (360, 60), (440, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (200, 110), (280, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (280, 110), (360, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (360, 110), (440, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (200, 160), (280, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (280, 160), (360, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (360, 160), (440, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (200, 210), (280, 260), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (280, 210), (360, 260), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (360, 210), (440, 260), (255, 255, 255), -1, 8, 0)
    else:
        curr_click = 12
    
    return keyboardImage

def Select_alphabet(curr_click, layer_select):

    key_str_layer1 = ['F', 'M', 'R', 'N', 'T', 'D', 'G', 'S', 'H', ' ', '', '']
    key_str_layer2 = ['J', 'B', 'P', 'Q', 'L', 'V', 'Z', 'C', 'W', ' ', '', '']
    key_str_layer3 = ['O', 'A', 'X', 'U', 'Y', 'E', 'I', 'K', '', ' ', '', '']
    key_str_layer4 = ['A', 'E', 'I', 'O', 'U']
    
    if (layer_select == 1):
        curr_str = key_str_layer1[curr_click]
    elif (layer_select == 2):
        curr_str = key_str_layer2[curr_click]
    elif (layer_select == 3):
        curr_str = key_str_layer3[curr_click]
    elif (layer_select == 4):
        curr_str = key_str_layer4[curr_click]
    
    return curr_str

def Virtualkeyboard_3by3_select(fingertip, tipClose):
    
    dell_click = 0
    reset_click = 0
    curr_click = 12
    
    # If (right_clickSignal == 1)
    if(tipClose == 1):
        if(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 0
        elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 1
        elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 2
        elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 3
        elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 4
        elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 5
        elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 6
        elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 7
        elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 8
        elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            curr_click = 9 #Space
        elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            dell_click = 1 #Delete
            curr_click = 10
        elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            reset_click = 1 #Reset
            curr_click = 11
        else:
            curr_click = 12
    
    return curr_click

def Virtualkeyboard_vowel_select(layer, tipClose):

    dell_click = 0
    reset_click = 0
    curr_click = 12

    if(tipClose == 2):
        if layer == 'letter-a':
            curr_click = 0
        elif layer == 'letter-e':
            curr_click = 1
        elif layer == 'letter-i':
            curr_click = 2
        elif layer == 'letter-o':
            curr_click = 3
        elif layer == 'letter-u':
            curr_click = 4
        else:
            curr_click = 12
    return curr_click

def Virtualkeyboard_3by3_draw_layer(keyboardImage, display_str, layer_select):
    
    # 왼쪽아래 학교표시
    cv2.rectangle(keyboardImage, (15, 430), (155, 460), (100, 0, 0), -1, 8, 0)
    cv2.rectangle(keyboardImage, (15, 430), (155, 460), (255, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, "SNU, CAPP Lab.", (20, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 255, 0), 1, cv2.LINE_AA)
    
    #4by4 keyboard 표시
    cv2.rectangle(keyboardImage, (525, 60), (600, 110), (0, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, "3by3", (535, 89), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)  
    
    #Display string
    cv2.rectangle(keyboardImage, (40, 8), (600, 52), (255, 255, 255), -1, 8, 0)
    cv2.rectangle(keyboardImage, (40, 8), (600, 52), (0, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, display_str, (50, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 50), 2, cv2.LINE_AA)
    #Keyboard layer
    cv2.rectangle(keyboardImage, (200, 60), (440, 260), (255, 255, 255), 1, 8, 0)
    cv2.line(keyboardImage, (200, 110), (440, 110), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (200, 160), (440, 160), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (200, 210), (440, 210), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (280, 60), (280, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (360, 60), (360, 260), (255, 255, 255), 1, 0, 0)
    
    #--------------------------Function Button----------------------------
    cv2.rectangle(keyboardImage, (201, 211), (279, 259), (255, 0, 0), 1, 8, 0)		# space_click button
    cv2.rectangle(keyboardImage, (281, 211), (359, 259), (0, 0, 255), 1, 8, 0)		# delete button
    cv2.rectangle(keyboardImage, (361, 211), (439, 259), (0, 0, 255), 1, 8, 0)		# reset button
    
    if (layer_select == 1):
        cv2.putText(keyboardImage, "F      M      R", (211, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "F      M      R", (211, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "N      T      D", (211, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "N      T      D", (211, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "G      S      H", (211, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "G      S      H", (211, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "J      B      P", (231, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q      L      V", (231, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z      C      W", (231, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "O      A      X", (255, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "U      Y      E", (255, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "I      K       ", (255, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, " Space    Delete    Reset", (210, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    
    if (layer_select == 2):
        cv2.putText(keyboardImage, "J      B      P", (231, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "J      B      P", (231, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q      L      V", (231, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q      L      V", (231, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z      C      W", (231, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z      C      W", (231, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "F      M      R", (211, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "N      T      D", (211, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "G      S      H", (211, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "O      A      X", (255, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "U      Y      E", (255, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "I      K       ", (255, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, " Space    Delete    Reset", (210, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    if (layer_select == 3):
        cv2.putText(keyboardImage, "O      A      X", (255, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "O      A      X", (255, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "U      Y      E", (255, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "U      Y      E", (255, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "I      K       ", (255, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "I      K       ", (255, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "F      M      R", (211, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "N      T      D", (211, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "G      S      H", (211, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "J      B      P", (231, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q      L      V", (231, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z      C      W", (231, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, " Space    Delete    Reset", (210, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    if (layer_select == 4):
        cv2.putText(keyboardImage, "J      B      X", (255, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q      Y      V", (255, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z      K       ", (255, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "O      A      R", (211, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "N      T      E", (211, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "I      S      H", (211, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "F      M      P", (231, 89), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "U      L      D", (231, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "G      C      W", (231, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, " Space    Delete    Reset", (210, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    return keyboardImage
    
if __name__=='__main__':
    videoFile = 'IMAGES/fast_snu.mp4'
    cap = cv2.VideoCapture(videoFile)
    if (cap.isOpened()==False):
        print('Can not open capture !!!')
    
    # Define the codec ) and ( create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('fast_snu_output.mp4', fourcc, 20.0, (640,480))
    
    frameNum = 0

    final_str = []
    start_time = time.time()
    curr_click = 10
    prev_click = 0
    stay_count = 0
    
    while(cap.isOpened()):
        ret, frame = cap.read()
            
        if ret is False:
            break
        
        keyboardImage = frame.copy()
        print("Frame number:", frameNum)

        #Get the index_finger coordinate and keyboard layer information, click signal generation
        if (frameNum <= 50):
            index_finger = (245, 200)
        elif (frameNum == 51) or (frameNum == 52) or (frameNum == 53) or (frameNum == 54):
            index_finger = (325, 200)
        else:
            index_finger = (440, 200)
            
        layer = [1, 2, 3]
        layer_select = layer[2]
        tipClose = 1
        
        #Select the virtual keyboard and the alphabet by index finger coordinate
        curr_click, reset_click, dell_click = Virtualkeyboard_3by3_select(index_finger, tipClose)
        print("curr_click: ", curr_click)
        print("prev_click: ", prev_click)
        
        #To see whether the index_finger coordinate moved
        if (curr_click != prev_click) and (frameNum != 0):
            move_key = 1
        else:
            move_key = 0
        print ("move_key:", move_key)
        
        if (move_key == 1):
            stay_count = 0
        else:
            stay_count += 1
        print('stay_count: ',stay_count)
        
         
        if (stay_count == 3) and (dell_click == 0) and (reset_click == 0) and (curr_click < 12):
            curr_str = Select_alphabet(curr_click, layer_select)
            final_str.append(curr_str)
            print(final_str)
        
        if (reset_click == 1):
            final_str.clear()
        
        if (dell_click == 1):
            print(final_str)
            final_str = final_str[:-1]
            print(final_str)
        
        prev_click = curr_click

        if (stay_count == 3):
            keyboardImage = Click_effect(index_finger, keyboardImage)
        #Draw the keyboard layer and monitor selected string
        display_str = ''.join(final_str)
        keyboardImage = Virtualkeyboard_3by3_draw_layer(keyboardImage, display_str, layer_select)
        print(display_str)
        #Display typing result
        cv2.imshow("keyboardImage", keyboardImage)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Save by jpg frame
        #cv2.imwrite(f"air3_output/{frameNum}.jpg", keyboardImage)
        
        # Write video
        #out.write(keyboardImage)
        
        frameNum += 1
             
    cap.release()
    cv2.destroyAllWindows()
    end_time = time.time()
    run_time = end_time - start_time
    print("Runtime:", run_time)
