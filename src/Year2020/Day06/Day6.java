package Year2020.Day06;

import java.io.IOException;
import java.io.File;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class Day6 {
    
    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day06/input.txt"));
        HashMap<Integer,HashMap<Character,Integer>> yesCounts = new HashMap<>();
        yesCounts.put(0, new HashMap<>());
        
        int yes = 0;
        int group = 0;
        int groupMembers = 0;
        while (in.hasNextLine()) {
            String currentLine = in.nextLine();
            if (currentLine.isEmpty()) {
                if (part == 2) {
                    HashMap<Character,Integer> hm = yesCounts.get(group);
                    for (Map.Entry<Character,Integer> m : hm.entrySet()) {
                        if (m.getValue() == groupMembers) {
                            yes++;
                        }
                    }

                }

                group++;
                groupMembers = 0;
                yesCounts.put(group, new HashMap<>());
                continue;
            }
            groupMembers++;

            for (char c : currentLine.toCharArray()) {
                //In part 1, we add only unique questions to the map
                if (part == 1 && !yesCounts.get(group).containsKey(c)) {
                    yesCounts.get(group).put(c,1);
                }
                //In part 2, we add all questions and increase their occurrence
                if (part == 2) {
                    HashMap<Character,Integer> temp = yesCounts.get(group);
                    if (temp.containsKey(c))
                        yesCounts.get(group).put(c, temp.get(c)+1);
                    else
                        yesCounts.get(group).put(c, 1);
                }
            }

        }
        if (part == 2) {
            HashMap<Character,Integer> hm = yesCounts.get(group);
            for (Map.Entry<Character,Integer> m : hm.entrySet()) {
                if (m.getValue() == groupMembers) {
                    yes++;
                }
            }

        }

        if (part == 1) {
            for (HashMap<Character,Integer> e : yesCounts.values()) {
                yes += e.size();
            }
        }

        in.close();
        return yes;
    }
    
    
    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
        System.out.println("Part 2: " + solve(2));
    }   
}
