#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

# Example: Shows how images can be accessed through ALVideoDevice

import qi
import argparse
import sys
import time
import vision_definitions

def main(session):
    # Get the service ALVideoDevice

    video_service = session.service("ALVideoDevice")

    # Register a Generic Video Module
    resolution = vision_definitions.kQQVGA
    colorSpace = vision_definitions.kYUVColorSpace
    fps = 20

    nameId = video_service.suscribe("python_GVM", resolution, colorSpace, fps)

    print "Getting images in remote"

    for in in range(20):
        print "getting image " + str(i)
        video_service.getImageRemote(nameId)
        time.sleep(0.05)

    video_service.unsuscribe(nameId)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # --ip = ip du robot
    # --port = port de conection du robot

    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")

    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
        
    main(session)