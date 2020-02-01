# Roombas

## To Run:

With *pygame* installed, run the **play.py** file. 

## Explanations
* Roombas: 
    * starts in a random spot
    * health = 3
        * decreases due to getting hit by an animal
        * upon "death," it will return to it's initial spots
    * bounces from walls, roombas, and dropoffs
* Dogs:
    * will run around the room, even over furniture (like real dogs)
    * if it runs into a roomba, the roomba will lose health
* Furniture
    * roombas will run into it
    * dogs will run over them
* Dirts
    * normal dirt (tan)
        * when run over by a roomba, it will disappear
    * super dirt (dark brown on tan)
        * when run over by a roomba, the roomba will "stall" for a frame and then continue on.
* Walls
    * nothing can pass it