package Year2020.Day13;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day13 {
    public static int solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day13/" + input + ".txt"));
        int earliestTime = Integer.parseInt(in.nextLine());
        ArrayList<Integer> buses = new ArrayList<>();
        Matcher m = Pattern.compile("(\\d+)").matcher(in.nextLine());
        while (m.find()) {
            buses.add(Integer.parseInt(m.group()));
        }
        System.out.println(buses);

        for (int time = earliestTime; true; earliestTime++) {
            for (Integer bus : buses) {
                if (earliestTime % bus == 0) {
                    return bus*(earliestTime-time);
                }
            }
        }

        //part 2 will return a long!
        
    }
        
    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1, "input"));
        //System.out.println("Part 2: " + solve(2, "input"));
    }
}
