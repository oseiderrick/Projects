package prob2again;

import java.util.HashMap;
import java.util.ArrayList;

public class NonPerishableItem extends Item {
   
    private static HashMap<Integer, NonPerishableItem> itemMap = new HashMap<>();
    private static ArrayList<NonPerishableItem> itemList = new ArrayList<>();

    public NonPerishableItem(int id, String name) {
        super(id, name);
        itemMap.put(id, this);
        itemList.add(this);
    }

    @Override
    public boolean isPerishable() {
        return false;
    }

    public static NonPerishableItem getItemById(int id) {
        return itemMap.get(id);
    }

    public static ArrayList<NonPerishableItem> getAllItems() {
        return itemList;
    }
}