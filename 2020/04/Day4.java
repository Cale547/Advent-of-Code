package Year2020.Day04;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URL;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day4 {


    public static boolean isValid(String passport, int part) {
        boolean valid = true;
        //System.out.println("Validating " + passport);

        if (part == 1) {
            String[] mandatoryFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}; //"cid"};
            for (String s : mandatoryFields) {
                if (passport.indexOf(s) == -1) {
                    valid = false;
                    break;
                }
            }
        }

        if (part == 2) {
            //String[] validFields = {"byr:(?:19[2-9]\\d|200[0-2])$", "iyr:20(?:1\\d|20)$", "eyr:20(?:2\\d|30)$",
            //"hgt:(?:1(?:[5-8]\\d|9[0-3])cm|(?:59|6\\d|7[0-6])in)$", "hcl:#[0-9a-f]{6}(?: |\n)$", "ecl:(?:amb|blu|brn|gry|grn|hzl|oth)$", "pid:\\d{9}$"};
            
            String[] validFields = {"byr:(?:19[2-9]\\d|200[0-2])(?:$| )","iyr:20(?:1\\d|20)(?:$| )","eyr:20(?:2\\d|30)(?:$| )",
            "hgt:(?:1(?:[5-8]\\d|9[0-3])cm|(?:59|6\\d|7[0-6])in)(?:$| )","hcl:#[0-9a-f]{6}(?:$| )","ecl:(?:amb|blu|brn|gry|grn|hzl|oth)(?:$| )","pid:\\d{9}(?:$| )"};

            
            for (String s : validFields) {
                Pattern p = Pattern.compile(s);
                Matcher m = p.matcher(passport);
                if (!m.find()) {
                    //System.out.println(s.substring(0,3) + " not valid in " + passport);
                    valid = false;
                    break;
                }//"hcl:#[0-9a-f]{6}(?: |\n)""hcl:#[0-9a-f]{6}(?: |\n)"
            }
        }

        if (part == 2) {
            System.out.println(passport + " is valid.");
        }
        return valid;
    }



    public static int solve(int part) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter("debug.txt", true));
        Scanner in = new Scanner(new File("src/Year2020/Day04/input.txt"));        
        int totalPassports = 0;
        int validPassports = 0;
        String current = "";
        while (in.hasNextLine()) {
            current = in.nextLine();
            totalPassports ++;
            while (!current.isEmpty() && in.hasNextLine()) {
                String nextLine = in.nextLine(); 
                if (!nextLine.isEmpty()) {
                    current += " " + nextLine;
                    continue;
                }

                if (isValid(current, part)) {
                    bw.append("\n"+current);
                    validPassports++;
                }
                current = "";
            }
            
        }
        if (isValid(current, part)) {
            bw.append("\n"+current);
            validPassports++;
        }

        System.out.println("Part " + part + ": " + validPassports + " out of " + totalPassports + " are valid.");
        in.close();
        return validPassports;
    }
    
    public static void main(String[] args) throws IOException {
        File debug = new File("src/Year2020/Day04/debug.txt");
        
        solve(1);
        solve(2);
        //System.out.println("Part 1: " + solve(1));
        //System.out.println("Part 2: " + solve(2));
    }
}
//159 too high
//136 too low