package Year2020.Day12;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Day12 {

    public static class Ship {
        public static final int NORTH = 0;
        public static final int EAST = 90;
        public static final int SOUTH = 180;
        public static final int WEST = 270;

        private int direction = EAST;
        private int xDist = 0;
        private int yDist = 0;

        private int wpX = 10;
        private int wpY = 1;


        // Part 1
        public void move(int direction, int distance) {
            if (direction == NORTH) {yDist += distance;}
            if (direction == EAST) {xDist += distance;}
            if (direction == WEST) {xDist -= distance;}
            if (direction == SOUTH) {yDist -= distance;}
        }

        // Part 1
        public void moveForward(int distance) {
            move(this.direction, distance);
        }

        // Part 1
        public void turn(String direction, int degrees) {
            if (direction.equals("L")) {turn("R", 360-degrees); return;}
            this.direction = (this.direction + degrees) % 360;
        }

        // Part 2
        public void moveWP(int direction, int distance) {
            if (direction == NORTH) {wpY += distance;}
            if (direction == EAST) {wpX += distance;}
            if (direction == WEST) {wpX -= distance;}
            if (direction == SOUTH) {wpY -= distance;}
        }

        // Part 2
        public void moveToWaypoint(int distance) {
            move(EAST, distance*wpX);
            move(NORTH, distance*wpY);
        }

        // Part 2
        public void turnWP(String direction, int degrees) {
            if (direction.equals("L")) {turnWP("R", 360-degrees); return;}
            
            if (degrees == 90) {
                int temp = -wpX;
                wpX = wpY;
                wpY = temp;
            } else if (degrees == 180) {
                wpX = -wpX;
                wpY = -wpY;
            } else if (degrees == 270) {
                int temp = wpX;
                wpX = -wpY;
                wpY = temp;
            } else {System.out.println("what about " + degrees + " degrees?");}
        }


        public int getCurrentManhattan() {
            return Math.abs(xDist)+Math.abs(yDist);
        }

        public static int convertDirection(String dir) {
            switch (dir) {
                case "N":
                    return NORTH;
                case "E":
                    return EAST;
                case "W":
                    return WEST;
                case "S":
                    return SOUTH;
                default:
                    System.out.println("You're silly!");
                    return -1;
            }
        }
    }


    public static int solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day12/" + input + ".txt"));
        Ship s = new Ship();

        while (in.hasNextLine()) {
            String instruction = in.nextLine();
            String action = instruction.substring(0,1);

            if (part == 1) {
                if ("NEWS".contains(action)) {s.move(Ship.convertDirection(action), Integer.parseInt(instruction.substring(1)));}
                if ("LR".contains(action)) {s.turn(action, Integer.parseInt(instruction.substring(1)));}
                if (action.equals("F")) {s.moveForward(Integer.parseInt(instruction.substring(1)));}
            }

            if (part == 2) {
                if ("NEWS".contains(action)) {s.moveWP(Ship.convertDirection(action), Integer.parseInt(instruction.substring(1)));}
                if ("LR".contains(action)) {s.turnWP(action, Integer.parseInt(instruction.substring(1)));}
                if (action.equals("F")) {s.moveToWaypoint(Integer.parseInt(instruction.substring(1)));}
            }
        }

        in.close();
        return s.getCurrentManhattan();
    }



    public static void main(String[] args) throws IOException {
        //System.out.println("Part 1: " + solve(1, "input"));
        System.out.println("Part 2: " + solve(2, "input"));
    }
}

// 47023 too low