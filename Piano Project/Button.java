import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class PianoButton here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Button  extends Actor
{
    private GreenfootImage[] images = new GreenfootImage[3];    

    //private GreenfootImage imageUnclicked;
    //private GreenfootImage imageclicked;
    private Piano myPiano;

    public Button(Piano piano){
        images[0] = new GreenfootImage("PianoButton.png");
        images[1] = new GreenfootImage("BassoonButton.png");
        images[2] = new GreenfootImage("MyNotesButton.png");
        setImage(images[0]);
        myPiano = piano;
    }

    public void act() 
    {
        // The Cruise button will engage when being pressed
        if(Greenfoot.mouseClicked(this)){
            if (getImage() == images[0]){
                setImage(images[1]); // change to Bassoon
                // 0: piano
                myPiano.changeSoundFilesForKeys(1);

            }else if (getImage() == images[1]){
                setImage(images[2]); // change to Bassoon
                // 0: piano
                myPiano.changeSoundFilesForKeys(2);

            }
            else {
                setImage(images[0]); // change to CS Courses
                myPiano.changeSoundFilesForKeys(0);
            }
        }
    }       
}
