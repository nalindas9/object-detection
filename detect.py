"""
# To-Do
"""
from email.mime import image

from numpy import size
from configuration_parser import ConfigurationParser
import cv2

class Detect:
    """
    Detect class
    """
    def __init__(self):
        """
        Detect class constructor
        """
        self._path = 'config/config.yaml'
        self._config_parser = ConfigurationParser(path=self._path,
                                                 module_name='detect')
        self._classes = self._config_parser.getConfigValue('classes')
        self._minimum_confidence = self._config_parser.getMinConfidence()

    def initializeModel(self):
        """
        """
        # Load the model
        model_path = self._config_parser.getModelPath()
        model_config_path = self._config_parser.getModelConfigPath()
        network = cv2.dnn.readNetFromCaffe(model_config_path, model_path)
        print('Model loaded successfully')
        return network

    def detect(self, network):
        """
        """
        # Define video capture object
        video = cv2.VideoCapture(0)

        while True:
            # Read the frame
            ret, frame = video.read()

            # Get the blob from the frame
            blob = cv2.dnn.blobFromImage(image=frame,
                                         scalefactor=1.0,
                                         size=(300, 300))

            #print('blob shape: ', blob.shape)
            # Set the blob as input to the network
            network.setInput(blob)

            # Run the forward pass
            detections = network.forward()
            #print('detections shape: ', detections.shapes

            # Loop over the detections
            for i in range(0, detections.shape[2]):
                # Get the confidence of the prediction
                confidence = detections[0, 0, i, 2]
                # Filter out weak detections
                if confidence > self._minimum_confidence:
                    #print('confidence: ', confidence)
                    # Extract the class label
                    class_label = int(detections[0, 0, i, 1])
                    #print('class label: ', class_label)
                    # Extract the class
                    class_name = self._classes[class_label]
                    print('class name: ', class_name)

            # Display the frame
            cv2.imshow('Detect', frame)

            # Exit on ESC
            if cv2.waitKey(1) == 27:
                break
        
        # Release the video capture object
        video.release()
        # Destroy all windows
        cv2.destroyAllWindows()