import greenfoot.*;  // (World, Actor, GreenfootImage, and Greenfoot)

/**
 * A piano that can be played with the computer keyboard.
 * 
 * @author: M. Kolling
 * @version: 0.1
 */
public class Piano extends World
{
    private Key[] keys = new Key[12];

    private String[] whiteKeys = {"a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\\"};

    private String[] whiteNotes = {"2c", "2d", "2e", "2f", "2g", "3a", "3b", "3c", "3d", "3e", "3f", "3g"};

    private String[] prefix = {"Piano\\", "Bassoon\\", "MyNotes\\"}; // Windows
    // private String[] prefix = {"Piano\\", "Bassoon\\"}; // Mac and Linux
    private String postfix = ".wav";

    /**
     * Make the piano.
     */
    public Piano() 
    {
        super(800, 400, 1);

        makeKeys();

        addObject(new Button(this), 400, 340);
    }

    public void makeKeys(){
        int i = 0;
        while (i < 12){
            Key key = new Key(whiteKeys[i], prefix[0] + whiteNotes[i] + postfix);
            addObject(key, 54+i*63, 140);
            keys[i] = key;
            i++;
        }
    }

    // instrument: 0 -- Piano
    //             1 -- Bassoon
    public void changeSoundFilesForKeys(int instrument){
        if (instrument == 0){// 0: Piano
            int i = 0;
            while (i < 12){
                keys[i].changeSoundFile(prefix[0] + whiteNotes[i] + postfix);
                i++;
            }
        }else if(instrument == 1){ // 1: Bassoon
            int i = 0;
            while (i < 12){
                keys[i].changeSoundFile(prefix[1] + whiteNotes[i] + postfix);
                i++;
            }

        }
        else { // 2: MyNotes
            int i = 0;
            while (i < 12){
                keys[i].changeSoundFile(prefix[2] + whiteNotes[i] + postfix);
                i++;
            }
        }

    }
}