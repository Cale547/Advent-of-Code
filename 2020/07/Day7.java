package Year2020.Day07;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Pattern;
import java.util.regex.Matcher;


public class Day7 {
    public static boolean checkThisAndInner(String outer, HashMap<String,HashMap<String,Integer>> bagMap, HashSet<String> canHold, HashSet<String> noHold) {
        if (!bagMap.containsKey(outer)) {
            noHold.add(outer);
            return false;
        }
        String myBag = "shiny gold";
        if (bagMap.get(outer).containsKey(myBag)) {
            canHold.add(outer);
            return true;
        }

        for (String inner : bagMap.get(outer).keySet()) {
            if (checkThisAndInner(inner, bagMap, canHold, noHold)) {
                canHold.add(outer);
                return true;
            }
        }

        noHold.add(outer);
        return false;
    }

    public static int howManyBagsInThisQuestionMark(String outer, HashMap<String,HashMap<String,Integer>> bagMap, int indent) {
        int bags = 0;
        //System.out.println(" ".repeat(indent) + " Outer is now " + outer);

        if (!bagMap.containsKey(outer)) {
            return 1;
        }

        for (String inner : bagMap.get(outer).keySet()) {
            int temp = bagMap.get(outer).get(inner)*howManyBagsInThisQuestionMark(inner, bagMap, indent+2);
            //System.out.println(" ".repeat(indent+2) + inner + " has " + temp + " bags");
            bags += temp;
        }

        if (outer.equals("shiny gold"))
            return bags;

        return bags+1;
    }

    public static int solve(int part) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day07/input.txt"));
        HashMap<String,HashMap<String,Integer>> bagMap = new HashMap<>();

        while (in.hasNextLine()) {
            String currentRule = in.nextLine();
            Matcher mOuter = Pattern.compile("(.+) bags contain").matcher(currentRule);
            Matcher mInner = Pattern.compile("(\\d \\w+ \\w+)").matcher(currentRule);
            

            HashMap<String,Integer> innerBags = new HashMap<>();
            while (mInner.find()) {
                String color = mInner.group().substring(2);
                int count = Integer.parseInt(mInner.group().substring(0, 1));
                innerBags.put(color, count);
            }
            //Only stores the outer bag in the bagMap if it contains any bags
            if (innerBags.size() != 0 && mOuter.find()) {
                bagMap.put(mOuter.group(1), innerBags);
            }
        }

        if (part == 1) {
            HashSet<String> canHold = new HashSet<>();
            HashSet<String> noHold = new HashSet<>();
            for (String outer : bagMap.keySet()) {
                checkThisAndInner(outer, bagMap, canHold, noHold);
            }
            //System.out.println("canHold size: " + canHold.size());
            //System.out.println("noHold size: " + noHold.size());
            return canHold.size();
        }

        if (part == 2) {
            return howManyBagsInThisQuestionMark("shiny gold", bagMap, 0);
        }
        return 0;
    }



    public static void main(String[] args) throws IOException {
        System.out.println("Part 1: " + solve(1));
        System.out.println("Part 2: " + solve(2));
    }
}