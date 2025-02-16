package Year2020.Day08;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day8 {
    public static int runCode(ArrayList<String> instructions, int part) {
        boolean[] performed = new boolean[instructions.size()];
        int index = 0;
        int acc = 0;

        while (!performed[index]) {
            performed[index] = true;
            String instruction = instructions.get(index);
            String type = instruction.substring(0,3);
            //parseInt tar in + och -, nu har jag lärt mig nåt nytt :)
            int number = Integer.parseInt(instruction.substring(4));
            if (type.equals("acc"))
                acc += number;
            if (type.equals("jmp"))
                index += number-1;
            index++;

            if (part == 2) {
                if (index < 0) {
                    //System.out.println("Negative index, acc="+ acc + ". Returning 0");
                    return 0;
                }

                if (index >= instructions.size()) {
                    //System.out.println("Index is " + index + " but last instruction has index " + (instructions.size()-1));
                    //System.out.println("Returning acc, currently at " + acc);
                    return acc;
                }
            }
        }
        if (part == 1) {
            //Returns value in acc when an instruction tries to run for the second time
            return acc;
        }

        return 0;
    }
    
    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day08/input.txt"));
        ArrayList<String> instructions = new ArrayList<>();
        while (in.hasNextLine())
            instructions.add(in.nextLine());
        in.close();

        if (part == 1) {
            return runCode(instructions, 1);
        }

        
        if (part == 2) {
            for (int modIndex = 0; modIndex < instructions.size(); modIndex++) {
                String oldInstruction = instructions.get(modIndex);
                String type = oldInstruction.substring(0, 3);
                if (type.equals("acc"))
                    continue;
                String newInstruction = "";
                if (type.equals("nop")) {
                    newInstruction = oldInstruction.replace(type, "jmp");
                    //instructions.remove(oldInstruction);
                    instructions.remove(modIndex);
                    instructions.add(modIndex, newInstruction);
                }
                else if (type.equals("jmp")) {
                    newInstruction = oldInstruction.replace(type, "nop");
                    //instructions.remove(oldInstruction);
                    instructions.remove(modIndex);
                    instructions.add(modIndex, newInstruction);
                }

                //After this comment, one instruction is modified and we run the program like normal
                //modIndex = line-1 in textfile.
                //e.g. modIndex 3 = line 4
                //System.out.println("Running code with modIndex="+modIndex);
                int thisAcc = runCode(instructions, 2);
                if (thisAcc != 0) {
                    //System.out.println("Part 2 success with modIndex: " + modIndex);
                    return thisAcc;
                }

                //instructions.remove(newInstruction);
                instructions.remove(modIndex);
                instructions.add(modIndex, oldInstruction);
            }

            System.out.println("Part 2 failed again, suck.");
            return -69;
        }

        
        //System.out.println("Instruction with index " + index + " tried to execute twice.");
        //System.out.println("acc = " + acc);
        return 0;
    }


    public static void main(String[] args) throws IOException {
            System.out.println("Part 1: " + solve(1));
            System.out.println("Part 2: " + solve(2));
    }
}


//124 too low
//165 too low
/* The problem, which I anticipated rather early without doing anything about it,
was that the remove() when modifying a single instruction removed an identical instruction
at another index. The fix was to use remove(modIndex) instead of remove(oldInstruction).
Oh well, it works now :)
 */
