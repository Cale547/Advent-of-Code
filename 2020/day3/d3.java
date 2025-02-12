package day3;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class d3 {
    public static long solve(int part) throws IOException {
        Scanner in = new Scanner(new File("day3/input.txt"));
        
        ArrayList<String> treeMap = new ArrayList<>();
        while (in.hasNextLine()) {
            treeMap.add(in.nextLine());
        }

        int x = 0;
        int treesEncountered = 0;
        if (part == 1) {
            for (int y = 1; y < treeMap.size(); y++) {
                x = (x+3) % treeMap.get(0).length();
                if (treeMap.get(y).charAt(x) == '#')
                    treesEncountered++;
            }
            return treesEncountered;
        }

        if (part == 2) {
            ArrayList<Integer> encounters = new ArrayList<>();
            for (int xSpeed = 1; xSpeed < 8; xSpeed += 2) {
                for (int y = 1; y < treeMap.size(); y++) {
                    x = (x+xSpeed) % treeMap.get(0).length();
                    if (treeMap.get(y).charAt(x) == '#')
                        treesEncountered++;
                }
                encounters.add(treesEncountered);
                treesEncountered = 0;
                x = 0;
            }
            int xSpeed = 1;
            for (int y = 2; y < treeMap.size(); y += 2) {
                x = (x+xSpeed) % treeMap.get(0).length();
                if (treeMap.get(y).charAt(x) == '#')
                    treesEncountered++;
            }
            encounters.add(treesEncountered);
            long encounterProduct = 1;
            for (int i : encounters) {
                encounterProduct *= i;
            }
            System.out.println(encounters);
            return encounterProduct;
        }
        return 0;    
    }
    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
        System.out.println("Part 2: " + solve(2));

        
    }
}
