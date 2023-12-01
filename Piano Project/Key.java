import greenfoot.*;  // (World, Actor, GreenfootImage, and Greenfoot)

public class Key extends Actor
{
    private boolean isDown;
    private String key;
    private String sound;
    /**
     * Create a new key.
     */
    public Key(String keyName, String soundFile)
    {
        isDown = false;
        key = keyName;
        sound = soundFile;
    }

    /**
     * Do the action for this key.
     */
    public void act()
    {
        if (!isDown && Greenfoot.isKeyDown(key)){
            setImage("white-key-down.png");
            isDown = true;
            getWorld().showText(sound, 700, 300);
            play();
        }
        
        if (isDown && !Greenfoot.isKeyDown(key)){
            setImage("white-key.png");
            isDown = false;
            getWorld().showText("               ", 700, 300);
        }
        
    }
    
    public void changeSoundFile(String soundFile){
        sound = soundFile;    
    }
    
    public void play()
    {
        Greenfoot.playSound(sound);
    }

}