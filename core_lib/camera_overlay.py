import cv2

class Overlay:
    def __init__(self,resolution):
        self.width = resolution[0]
        self.height = resolution[1]
        self.line_type = cv2.LINE_AA
        self.left_align = 25
        self.height_increment = int(self.height/20)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.text_color = (255,255,255)
        self.shadow_color = (0,0,0)
        self.thickness = 1

    def add_camera_status(self, frame, camera):
        text = f"{camera} Camera"
        font_size = 1.2
        position = (self.left_align, self.height_increment)
        shadow_position = (self.left_align+2, self.height_increment+2)
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
        return frame
    
    def add_timer(self, frame, time):
        seconds = f"{time%60:02}"
        minutes = f"{(time-int(seconds))/60:02}"
        font_size = 1.0
        text = f"{minutes}:{seconds}"
        position = (self.left_align, self.height_increment * 2)
        shadow_position = (self.left_align + 2, self.height_increment * 2 + 2)
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
        return frame
    
    def add_sensitivities(self, frame, sensitivities):
        # Add the header
        font_size = 0.6
        position = (self.left_align, 3 * self.height_increment)
        shadow_position = (self.left_align + 5, 3 * self.height_increment + 5)
        text = "Sensitivity"
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)

        # Add the individual sensitivities:
        font_size = 0.5
        counter = 3.66
        for key in sensitivities:
            position = (self.left_align + 20, int(counter * self.height_increment))
            shadow_position = (self.left_align + 25, int(counter * self.height_increment) + 5)
            text = f"{key}: {sensitivities[key]}"
            frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
            frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
            counter += 0.66
        
        return frame
    
    def add_leak_warning(self, frame):
        font_size = 1
        text = "LEAK DETECTED"
        text_color = (0,0,255)
        text_width = cv2.getTextSize(text, self.font, font_size, self.thickness)[0]
        text_height = cv2.getTextSize(text, self.font, font_size, self.thickness)[1]
        position = (int((self.width - text_width)/2),int((self.height - text_height)))
        shadow_position = (int((self.width - text_width)/2)+5,int((self.height - text_height))+5)
        cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        cv2.putText(frame, text, position, self.font, font_size, text_color, self.thickness, self.line_type)


