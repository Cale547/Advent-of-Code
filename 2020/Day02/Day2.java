package Day02;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day2 {
    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("day2/input.txt"));
        Pattern p = Pattern.compile("(\\d+)-(\\d+) (.): (\\w+)");
        int validPasswords = 0;

        while (in.hasNextLine()) {
            String line = in.nextLine();
            Matcher m = p.matcher(line);
            m.matches();

            int min = Integer.parseInt(m.group(1));
            int max = Integer.parseInt(m.group(2));
            String letter = m.group(3);
            String password = m.group(4);

            //Count occurences
            if (part == 1) {
                int count = 0;
                int index = 0;
                while (index != -1) {
                    index = password.indexOf(letter, index);
                    if (index != -1) {
                        count++;
                        index++;
                    }
                }
                
                if (min <= count && count <= max) {
                    validPasswords++;
                }
            }

            if (part == 2) {
                char c = letter.toCharArray()[0];
                char cMin = password.charAt(min-1);
                char cMax = password.charAt(max-1);
                if (cMin != cMax && (cMin == c || cMax == c))
                    validPasswords++;
            }
        }


        in.close();
        return validPasswords;
    }



    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
        System.out.println("Part 2: " + solve(2));
    }

}



/* Poopy way to get all stuff
String[] line = in.nextLine().split(" ");
String[] bounds = line[0].split("-");
int min = Integer.parseInt(bounds[0]);
int max = Integer.parseInt(bounds[1]);
String letter = line[1].substring(0, 1);
String password = line[2]; */