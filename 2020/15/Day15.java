package Year2020.Day15;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Day15 {
    public static int startNumberInit(ArrayList<Integer> numbers, HashMap<Integer,Integer> lastTurnOfNumberMap, Integer[] startingNumbers) {
        for (int i = 0; i < startingNumbers.length; i++) {
            int currentStartingNumber = startingNumbers[i];
            numbers.add(currentStartingNumber);

            if (lastTurnOfNumberMap.get(currentStartingNumber) == null) {
                lastTurnOfNumberMap.put(currentStartingNumber, i+1); //The first starting number is said during turn 1, not 0, and so on.
            } 
        }
        return startingNumbers.length+1; //Returns the number of the turn after the starting numbers.
    }

    public static long solve(int part, String input) throws IOException {
        int targetIndex = 2020;
        if (part == 2)
            targetIndex = 30000000;
        //Scanner in = new Scanner(new File("src/Year2020/Day15/" + input + ".txt"));
        ArrayList<Integer> numbers = new ArrayList<>();
        HashMap<Integer, Integer> lastTurnOfNumberMap = new HashMap<>();
        numbers.add(-1);

        int currentTurn = 0;
        switch (input) {
            case "ex": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{0,3,6}); break; //Expected output = 436
            case "ex2": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{1,3,2}); break; //Expected output = 1
            case "ex3": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{2,1,3}); break; //Expected output = is 10
            case "ex4": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{1,2,3}); break; //Expected output = is 27
            case "ex5": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{2,3,1}); break; //Expected output = is 78
            case "ex6": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{3,2,1}); break; //Expected output = is 438
            case "ex7": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{3,1,2}); break; //Expected output = is 1836
            case "input": currentTurn = startNumberInit(numbers, lastTurnOfNumberMap, new Integer[]{9,6,0,10,18,2,1}); break;
            default: System.out.println("Oops! :D"); break;
        }



        while (currentTurn <= targetIndex) {
            //if (currentTurn % 100000 == 0)
            //    System.out.println(currentTurn);
            int previousNumber = numbers.get(currentTurn-1);
        
            Integer lastTurnOfPreviousNumber = lastTurnOfNumberMap.get(previousNumber);
            if (lastTurnOfPreviousNumber == null) {
                lastTurnOfNumberMap.put(previousNumber, currentTurn-1);
                numbers.add(0);
            } else {
                int turnDistance = (currentTurn-1) - lastTurnOfPreviousNumber;
                lastTurnOfNumberMap.put(previousNumber, currentTurn-1);
                numbers.add(turnDistance);
            }
            currentTurn++;
        }
        return numbers.get(targetIndex);
    }

    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1, "input"));
        System.out.println("Part 2: " + solve(2, "input"));
    }
}
