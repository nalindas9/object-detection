from detect import Detect

def main():
    """
    Main function
    """
    detect = Detect() # Create Detect object
    network = detect.initializeModel() # Initialize model
    detect.detect(network=network) # Detect
    

if __name__ == '__main__':
    main()