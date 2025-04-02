package Year2020.Day14;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;

public class Day14 {

    public static String getBinaryString() {return "";}

    public static int solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day14/" + input + ".txt"));
        String mask = "";
        HashMap<Integer, Long> memory = new HashMap<>();

        while (in.hasNextLine()) {
            String current = in.nextLine();
            //System.out.println(current);
            if (current.split(" ")[0].equals("mask")) {
                current = current.replace("X", "0");
                mask = current.split(" ")[2];

                System.out.println("Mask: " + current.split(" ")[2]);
            } else {
                Matcher m = Pattern.compile("\\[\\d+\\]").matcher(current);
                //System.out.println(current);
                if (m.find()) {
                    int index = Integer.parseInt(m.group().substring(1, m.group().length()-1));
                    long value = Long.parseLong(current.split(" ")[2]);
                    String valString = "0"*(32-len(value)) + value;
                    
                    System.out.println("Value: " + Long.toBinaryString(value));
                    System.out.println("Mask: " + mask);

                    // System.out.println("Value: " + value);
                    // System.out.println("Index " + index);

                    memory.put(index, value);
                }
                break;


            }

        }    
    
    
    
        System.out.println("Done!");
        return 0;
    }



    public static void main(String[] args) throws IOException {
            System.out.println("Part 1: " + solve(1, "ex"));
            // System.out.println("Part 2: " + solve(2, "input"));
    }
}
