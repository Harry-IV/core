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
    
    def add_thruster_status(self, frame, enabled):
        if enabled:
            status_text = "Enabled"
        else:
            status_text = "Disabled"
        text = f"Thrusters: {status_text}"
        font_size = 1.0
        position = (self.left_align, 2 * self.height_increment)
        shadow_position = (self.left_align+2, 2 * self.height_increment+2)
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
        return frame
    
    def add_timer(self, frame, time):
        seconds = f"{time%60:02}"
        minutes = f"{int((time-int(seconds))/60):02}"
        font_size = 1.0
        text = f"{minutes}:{seconds}"
        position = (self.left_align, self.height_increment * 3)
        shadow_position = (self.left_align + 2, self.height_increment * 3 + 2)
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
        return frame
    
    def add_sensitivities(self, frame, sensitivities):
        # Add the header
        font_size = 1.0
        position = (self.left_align, 4 * self.height_increment)
        shadow_position = (self.left_align + 2, 4 * self.height_increment + 2)
        text = "Sensitivity"
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)

        # Add the individual sensitivities:
        font_size = 0.8
        counter = 4.85
        for key in sensitivities:
            position = (self.left_align + 20, int(counter * self.height_increment))
            shadow_position = (self.left_align + 22, int(counter * self.height_increment) + 2)
            text = f"{key}: {sensitivities[key]}"
            frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
            frame = cv2.putText(frame, text, position, self.font, font_size, self.text_color, self.thickness, self.line_type)
            counter += 0.8
        
        return frame
    
    def add_leak_warning(self, frame):
        font_size = 3
        text = "LEAK DETECTED"
        text_color = (0,0,255)
        text_size = cv2.getTextSize(text, self.font, font_size, self.thickness)[0]
        text_width = text_size[0]
        text_height = text_size[1]
        x_pos = int((self.width-text_width)/2)
        y_pos = int((self.height+text_height)/2)
        position = (x_pos,y_pos)
        x_pos += 2
        y_pos += 2
        shadow_position = (x_pos, y_pos)
        frame = cv2.putText(frame, text, shadow_position, self.font, font_size, self.shadow_color, self.thickness, self.line_type)
        frame = cv2.putText(frame, text, position, self.font, font_size, text_color, self.thickness, self.line_type)
        return frame



