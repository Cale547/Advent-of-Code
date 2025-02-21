package Year2020.Day10;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;



public class Day10 {

    public static long solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day10/" + input + ".txt"));
        ArrayList<Integer> list = new ArrayList<>();
        while (in.hasNextLine()) {
          list.add(Integer.parseInt(in.nextLine()));
        }    
        // List now has all adapters
        
        
        int currentAdapter = 0;
        if (part == 1) {
            int[] diffs = {-1, 0, 0, 0};
            while (list.size() > 1) {
                for (int i = 1; i < 4; i++) {
                    if (list.contains(currentAdapter + i)) {
                        diffs[i]++;
                        list.remove((Object) currentAdapter);
                        currentAdapter = currentAdapter + i;
                        break;
                    }
                }
            }
            diffs[3]++; // diff between last adapter and airplane device
            in.close();
            return diffs[1]*diffs[3];
        }
        
        if (part == 2) {
            // First sort the list of adapters to ascending order
            Collections.sort(list);
            
            List<Integer> essAdapters = new ArrayList<>();
            for (Integer i : list) {
                if (!list.contains(i+1) && !list.contains(i+2) && list.contains(i+3)) {
                    essAdapters.add(i);
                    essAdapters.add(i+3);
                }
            }
            int last = list.get(list.size()-1);
            if (!essAdapters.contains(last))
                essAdapters.add(last); // Highest joltage adapter is the only one that can connect to the final device, making it essential.

            // gap since last essential adapter
            int gap = 0;
            HashMap<Integer,Integer> gapOccurrences = new HashMap<>();
            for (Integer current : list) {
                gap++;
                if (essAdapters.contains(current)) {
                    if (gap > 1) {
                        //System.out.println("Reaching adapter " + current + ", gap is " + gap);
                        if (gapOccurrences.containsKey(gap))
                            gapOccurrences.put(gap, gapOccurrences.get(gap)+1);
                        else {gapOccurrences.put(gap, 1);}
                    }
                    gap = 0;
                }
            }
            
            // The following code reveals the fact that only gap sizes of 2, 3, and 4 occur.
            /* for (Map.Entry<Integer,Integer> entry : gapOccurrences.entrySet()) {
                System.out.println("Gap size " + entry.getKey() + " occurs " + entry.getValue() + " times.");
            } */

            // Gap size of 2 means there is 1 non-essential adapter. It can assume 2 combinations. (0, 1)
            // Gap size of 3 means there are 2 non-essential adapters.They can assume 4 combinations. (00, 01, 10, 11)
            // Gap size of 4 means there are 3 non-essential adapters. They can assume 7 combinations. (001, 010, 100, 011, 101, 110, 111). 000 is impossible since it would create a non-bridgable gap.
            // The picture aoc10.2.png shows some of the thinking behind this solution. It does contain an "error", not labelling
            // 39 as an essential adapter, although this is corrected by (2^1)-1 :P 
            long arrangements = 1;
            if (gapOccurrences.containsKey(2))
                arrangements *= Math.pow(2,gapOccurrences.get(2));
            if (gapOccurrences.containsKey(3))
                arrangements *= Math.pow(4,gapOccurrences.get(3));
            if (gapOccurrences.containsKey(4))
                arrangements *= Math.pow(7,gapOccurrences.get(4));
            
            in.close();
            return arrangements;
        }

        in.close();
        return 0;
    }


    public static void main(String[] args) throws IOException {
            System.out.println("Part 1: " + solve(1, "input"));
            System.out.println("Part 2: " + solve(2, "input"));
        }
}