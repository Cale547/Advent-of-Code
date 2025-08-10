package Year2020.Day14;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.File;

public class Day14 {

    public static String getBinaryString() {return "";}

    public static long solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day14/" + input + ".txt"));
        String mask = "";
        HashMap<Long, Long> memory = new HashMap<>();

        if (part == 1) {
            while (in.hasNextLine()) {
                String current = in.nextLine();
                if (current.split(" ")[0].equals("mask")) {
                    mask = current.split(" ")[2];
                } else {
                    Matcher m = Pattern.compile("\\[\\d+\\]").matcher(current);
                    if (m.find()) {
                        int index = Integer.parseInt(m.group().replaceAll("[^\\d]", ""));
                        StringBuilder value = new StringBuilder(Long.toBinaryString(Long.parseLong(current.split(" ")[2])));
                        value = new StringBuilder("0".repeat(36-value.length()) + value);

                        System.out.println("Valu: " + value);
                        System.out.println("Mask: " + mask);
                        
                        assert(value.length() == mask.length()) : "Wrong lengths";
                        for (int i = 0; i < value.length(); i++) {
                            if (mask.charAt(i) != 'X') {
                                value.setCharAt(i, mask.charAt(i));
                            }
                        }
                        System.out.println("Valu: " + value);

                        memory.put((long) index, Long.parseLong(value.toString(), 2));
                        
                    }
                }
                System.out.println();

            }
        }

        if (part == 2) {
            while (in.hasNextLine()) {
                String current = in.nextLine();
                if (current.split(" ")[0].equals("mask")) {
                    mask = current.split(" ")[2];
                } else {
                    Matcher m = Pattern.compile("\\[\\d+\\]").matcher(current);
                    if (m.find()) {
                        long value = Long.parseLong(current.split(" ")[2]);

                        StringBuilder index = new StringBuilder(Integer.toBinaryString(Integer.parseInt(m.group().replaceAll("[^\\d]", ""))));
                        index = new StringBuilder("0".repeat(36-index.length()) + index);

                        
                        assert(index.length() == mask.length()) : "Wrong lengths";
                        for (int i = 0; i < index.length(); i++) {
                            if (mask.charAt(i) != '0') {
                                index.setCharAt(i, mask.charAt(i));
                            }
                        }
                        String indexString = index.toString();
                        int nFloatBits = indexString.length() - indexString.replaceAll("X", "").length();
                        int nAddresses = (int) Math.pow(2, nFloatBits);
                        
                        for (int i = 0; i < nAddresses; i++) {
                            String indexCopy = indexString;
                            String addressMod = Integer.toBinaryString(i);
                            addressMod = "0".repeat(nFloatBits-addressMod.length()) + addressMod;

                            for (char c : addressMod.toCharArray()) {
                                indexCopy = indexCopy.replaceFirst("X",""+c);
                            }
                            memory.put(Long.parseLong(indexCopy,2), value);
                        }
                    }
                
                }
            }
        }

        long sum = 0;
        for (Long l : memory.keySet()) {
            sum += memory.get(l);
        } 
    
        return sum;
    }



    public static void main(String[] args) throws IOException {
            //System.out.println("Part 1: " + solve(1, "input"));
            System.out.println("Part 2: " + solve(2, "input"));
    }
}
