
---

# Eye Mouse Controller

## License
This repository is licensed to the rightful owner, HARSHSINGH0. This license indicates that you do not have permission from the creator to use, modify, or share this software. While you may be able to view or fork the code via GitHub, this does not grant you the right to use, alter, or redistribute the software for any purpose.

## About
The Eye Mouse Controller project enables users to control the cursor on a computer using eye movement. By calculating the mean position between both eyes (eye landmarks), the application uses OpenCV to detect eye movements, allowing for hands-free cursor control.

## Interface
The Eye Mouse Controller interface allows users to:
1. Select the appropriate camera.
2. Set up the camera’s aspect ratio.
3. Adjust camera flipping.
4. Manage illumination for various lighting conditions.

### Setup Steps
1. **Camera Selection**: Enter the camera number. For example, enter "1" for a built-in laptop camera or "2" for an external camera. Press "Enter" to confirm.

   ![Camera Number Input](cameranumber.png.png)
   
2. **Aspect Ratio**: If the aspect ratio of your webcam is 16:9, select the checkbox. Otherwise, the default 4:3 ratio will be used.

   ![Aspect Ratio Selection](aspectratio.png.png)

3. **Flip Camera**: If the video feed is mirrored, use the "Inverse Camera" button to correct the orientation.

   ![Inverse Camera](inversecamera.png.png)

4. **Illumination Adjustment**: Use the illumination slider to adjust the lighting. The slider has three settings (1, 2, and 3). The default value is 1, and increasing it will adjust the gamma to improve visibility in low-light conditions.

   ![Illumination Slider](illmuniationslider.png.png)

After configuring the settings, press "Enter" to launch the program. The last used camera number will be saved to streamline setup for future sessions.

![Full Interface](instruction.png)

## OpenCV Video Capture
After configuration, pressing "Enter" will launch the OpenCV window. This window:
- Displays the video feed.
- Recognizes the user’s face and calculates the distance from the camera.
- Controls cursor speed based on the user’s face position relative to the screen center.

**Cursor Speed Zones**:
- When the face is in the central circle, the cursor remains stationary.
- As the face moves into the outer circles, the cursor speed increases.

To close the OpenCV window, press the ‘Q’ key. To fully exit the application, close the interface window as well.

## Dependencies
Install the following dependencies before running the project:
- **Anaconda Python**: Recommended for managing virtual environments.
- **opencv-python**: For video capture and image processing.
- **numpy**: For mathematical operations.
- **pynput**: To control the mouse.
- **cmake**: Required for installing dlib.
- **Visual C++**: Necessary for dlib installation.
- **dlib**: For facial landmark detection.
- **pywin32**: To get the screen size.
- **pyqt5**: For building the interface.
- **pyqt5-tools**: For designing the interface with PyQt Designer.

To install these dependencies, use the following command:
```bash
pip install opencv-python numpy pynput cmake dlib pywin32 pyqt5 pyqt5-tools
```

## Usage
After installing dependencies and configuring the interface settings, you’re ready to start the application and control the cursor with your eyes!

--- 
