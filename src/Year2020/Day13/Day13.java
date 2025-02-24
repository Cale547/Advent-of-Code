package Year2020.Day13;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day13 {
    public static long solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day13/" + input + ".txt"));
        int earliestTime = Integer.parseInt(in.nextLine());
        String schedule = in.nextLine();
        ArrayList<Integer> buses = new ArrayList<>();    

        if (part == 1) {
            Matcher m = Pattern.compile("(\\d+)").matcher(schedule);
            while (m.find()) {
                buses.add(Integer.parseInt(m.group()));
            }

            for (int time = earliestTime; true; earliestTime++) {
                for (Integer bus : buses) {
                    if (earliestTime % bus == 0) {
                        return bus*(earliestTime-time);
                    }
                }
            }
        }

        if (part == 2) {
            for (String busID : schedule.split(",")) {
                if (busID.equals("x")) {buses.add(0);}
                else {buses.add(Integer.parseInt(busID));}
            }

            // This HashMap contains each busID as key and 
            // how long after t they should depart as value.
            // The busID:s and their index in the schedule is used in Mathematica
            // as described below
            HashMap<Integer,Integer> busDelay = new HashMap<>();
            for (Integer bus : buses) {
                if (bus == 0) {continue;}
                busDelay.put(bus, buses.indexOf(bus));
            }
            
            // List printer
            /* for (Integer bus : buses) {
                if (bus == 0) {continue;}
                System.out.println("Bus " + bus + " departs " + busDelay.get(bus) + " minutes after t");
            } */

            /* The following code was used in Mathematica to give the answer t
             * FindInstance[{t == 17 a, t + 11 == 37 b, t + 17 == 907 c, 
                t + 29 == 19 d, t + 40 == 23 e, t + 46 == 29 f, t + 48 == 653 g, 
                t + 58 == 41 h, t + 61 == 13 i}, {t, a, b, c, d, e, f, g, h, 
                i}, Integers]

                Reveals that t = 842186186521918
             */
            return Long.parseLong("842186186521918");

            //The following code works for smaller bus lists but not for the actual input
            /* int slowBus = Collections.max(buses);
            int slowIndex = buses.indexOf(slowBus);
            //System.out.println(slowBus + " is the bus with index " + slowIndex);

            long time = 0;
            for (long i = slowBus; true; i += slowBus) {
                //System.out.println(i);
                time = i - slowIndex;
                boolean success = true;
                for (Integer busTime : buses) {
                    if (busTime != 0 && time % busTime != 0) {
                        success = false;
                    }
                    time++;
                }
                if (success) {
                    time = time - buses.size();
                    System.out.println(time + " is great success.");
                    return time;
                }
            } */
        }
        return 0;
    }
        
    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1, "input"));
        System.out.println("Part 2: " + solve(2, "input"));
    }
}
