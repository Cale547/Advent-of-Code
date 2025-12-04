package Year2020.Day05;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Day5 {
    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day05/input.txt"));
        HashMap<Integer,String> seats = new HashMap<>(); 
        int maxID = -1;
        while (in.hasNextLine()) {
            String boardingPass = in.nextLine();
            int minRow = 0;
            int maxRow = 127;
            for (int i = 0; i < 7; i++) {
                if (boardingPass.charAt(i) == 'F') {
                    maxRow -= (maxRow-minRow+1) /2;
                }

                else if (boardingPass.charAt(i) == 'B') {
                    minRow += (maxRow-minRow+1) /2;
                }
            }
            //minRow should now equal maxRow
            
            int minCol = 0;
            int maxCol = 7;
            for (int i = 7; i < boardingPass.length(); i++) {
                if (boardingPass.charAt(i) == 'L') {
                    maxCol -= (maxCol-minCol+1) /2;
                }

                else if (boardingPass.charAt(i) == 'R') {
                    minCol += (maxCol-minCol+1) /2;
                }
            }
            //minCol should now equal maxCol
            int seatID = minRow * 8 + minCol;
            if (part == 1)
                maxID = Math.max(seatID, maxID);

            if (part == 2) {
                seats.put(seatID, minRow+","+minCol);
            }
        }

        if (part == 1)
            return maxID;

        
        if (part == 2) {
            for (int id = 0; id < 1024; id++) {
                if (!seats.containsKey(id) && seats.containsKey(id-1) && seats.containsKey(id+1))
                    return id;
            }
        }
        return 0;
    }





    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
        System.out.println("Part 2: " + solve(2));
    }
}
