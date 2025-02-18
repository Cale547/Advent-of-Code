package Year2020.Day09;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day9 {
    public static long solve(int part, boolean example) throws IOException {
        Scanner in;
        int preamble;
        if (example) {
            in = new Scanner(new File("src/Year2020/Day09/ex.txt"));
            preamble = 5;
        } else {
            in = new Scanner(new File("src/Year2020/Day09/input.txt"));
            preamble = 25;
        }
        
        
        ArrayList<Long> nums = new ArrayList<>();
        while (in.hasNextLine()) {
            nums.add(Long.parseLong(in.nextLine()));
        }

        Long[] numbers = new Long[nums.size()];
        nums.toArray(numbers);
    
        long sum = 0;
        int indexOfSum = -1;
        for (int i = preamble; i < numbers.length; i++) {
            sum = numbers[i];
            boolean valid = false;
            for (int j = i-preamble; j < i && !valid; j++) {
                for (int k = j+1; k < i && !valid; k++) {
                    if (numbers[j] + numbers[k] == sum)
                        valid = true;
                }
            }
            if (!valid) {
                //System.out.println(sum + " cannot be made with the " + preamble + " numbers preceeding it.");
                indexOfSum = i;
                if (part == 1)
                    return sum;
                break;
            }
        }
        long invalidNumber = sum; //217430975

        int sumChainLength;
        for (int startIndex = 0; startIndex < numbers.length; startIndex++) {
            if (startIndex == indexOfSum)
                continue;
            sum = 0;
            sumChainLength = 0;
            for (int i = startIndex; i < numbers.length && sum <= invalidNumber; i++) {
                sumChainLength++;
                sum += numbers[i];
                if (sum == invalidNumber) {
                    long max = Long.MIN_VALUE; 
                    long min = Long.MAX_VALUE;
                    for (int j = 0; j < sumChainLength; j++) {
                        max = Math.max(max, numbers[startIndex+j]);
                        min = Math.min(min, numbers[startIndex+j]);
                    }
                    return max + min;
                }
            }
        }
        return 0;
    }


    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1, false));
        System.out.println("Part 2: " + solve(2, false));
    }
}