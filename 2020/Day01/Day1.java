package Day01;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day1 {
    public static int part1() throws IOException {
        Scanner in = new Scanner(new File("day1/input.txt"));
        ArrayList<Integer> nums = new ArrayList<>();

        while (in.hasNextLine()) {
            nums.add(Integer.parseInt(in.nextLine()));
        }

        for (int a : nums) {
            for (int b : nums) {
                if (a+b == 2020) {
                    in.close();
                    return a*b;
                }
            }
        }
        in.close();
        return 0;
    }

    public static int part2() throws IOException {
        Scanner in = new Scanner(new File("day1/input.txt"));
        ArrayList<Integer> nums = new ArrayList<>();

        while (in.hasNextLine()) {
            nums.add(Integer.parseInt(in.nextLine()));
        }

        for (int a : nums) {
            for (int b : nums) {
                for (int c : nums) {
                    if (a+b+c == 2020) {
                        in.close();
                        return a*b*c;
                    }
                }
            }
        }
        in.close();
        return 0;
    }

    public static void main() throws IOException {
        System.out.println("Part 1: " + part1());
        System.out.println("Part 2: " + part2());
    }
}