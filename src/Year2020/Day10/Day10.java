package Year2020.Day10;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Day10 {

    public static long solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day10/" + input + ".txt"));
        ArrayList<Integer> list = new ArrayList<>();
        while (in.hasNextLine()) {
          list.add(Integer.parseInt(in.nextLine()));
        }    
        //List now has all adapters
        
        
        int currentAdapter = 0;
        if (part == 1) {
            int oneDiffs = 0;
            int threeDiffs = 0;
            while (!list.isEmpty()) {
                if (list.contains(currentAdapter+1)) {
                    oneDiffs++;
                    list.remove((Object)currentAdapter); //be mindful of potential duplicates
                    currentAdapter = currentAdapter+1;
                }
                else if (list.contains(currentAdapter+2)) {
                    list.remove((Object)currentAdapter);
                    currentAdapter = currentAdapter+2;
                }

                else if (list.contains(currentAdapter+3)) {
                    threeDiffs++;
                    list.remove((Object)currentAdapter);
                    currentAdapter = currentAdapter+3;
                }
                else {
                    threeDiffs++; //The difference between the last adapter and the device
                    break;
                }
            }
            return ((long)oneDiffs)*threeDiffs;
        }
        
        if (part == 2) {
            HashMap<Integer,Integer> adapterBranches = new HashMap<>();
            for (int i : list) {
                adapterBranches.put(i, 0);
            }

            for (Integer i : list) {
                for (int j = 1; j <= 3; j++) {
                    if (list.contains(i+j)) {
                        adapterBranches.put(i, adapterBranches.get(i)+1);
                    }
                }
            }

            //Sortera först
            int[] adapters = new int[list.size()];
            for (int i = 0; i < adapters.length; i++) {
                adapters[i] = list.get(i);
            }
            Arrays.sort(adapters);
            for (int i : adapters) {
                System.out.println(i);
            }

            int optionalAdapters = 0;
            for (int i : adapters) {
                if (adapterBranches.containsKey(i-1) && adapterBranches.get(i-1) > 1) {
                    //System.out.println(i + " is an optional adapter.");
                    optionalAdapters++;
                }

                else if (adapterBranches.containsKey(i-2) && adapterBranches.containsKey(i+1)) {
                    //System.out.println(i + " is an optional adapter.");
                    optionalAdapters++;
                }
                

            }
            return (long)Math.pow(2, optionalAdapters);
        }
        

        
        
        return 0;
    }


    public static void main(String[] args) throws IOException {
            //System.out.println("Part 1: " + solve(1, "input"));
            System.out.println("Part 2: " + solve(2, "ex2"));
        }
}

// 35184372088832 too high