package Year2020.Day04;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Day4 {


    public static boolean isValid(String passport) {
        String[] mandatoryFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}; //"cid"};
        boolean valid = true;
        for (String s : mandatoryFields) {
            if (passport.indexOf(s) == -1) {
                valid = false;
                break;
            }
        }
        return valid;
    }

    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("Day04/input.txt"));        
        int totalPassports = 0;
        int validPassports = 0;
        while (in.hasNextLine()) {
            String current = in.nextLine();
            totalPassports ++;
            while (!current.isEmpty() && in.hasNextLine()) {
                String nextLine = in.nextLine(); 
                if (!nextLine.isEmpty()) {
                    current += nextLine;
                    continue;
                }

                if (isValid(current))
                    validPassports++;
                current = "";
            }
            if (isValid(current))
                validPassports++;
        }
        
        //System.out.println(validPassports + " out of " + totalPassports + " are valid.");
        in.close();
        return validPassports;
    }
    
    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
    }
}
//249 too low