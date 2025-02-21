package Year2020.Day11;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day11 {
    public static class Seat {
        public static final int FLOOR = 0;
        public static final int EMPTY = 1;
        public static final int OCCUPIED = 2;
        
        private int state;
        private int nextState;
        private int row;
        private int col;

        public Seat(int state, int row, int col) {
            this.state = state;
            this.row = row;
            this.col = col;
        }

        public void setNext(int state) {
            nextState = state;
        }

        public void update() {
            state = nextState;
        }

        public int getState() {
            return state;
        }

        public int getNext() {
            return nextState;
        }

        public String toString() {
            switch (state) {
                case Seat.FLOOR:
                    return ".";
                case Seat.EMPTY:
                    return "L";                
                case Seat.OCCUPIED:
                    return "#";
                default:
                    throw new IllegalStateException("Current state is invalid: " + getState());    
            }
        }

        public int countOccupiedAdjacent(List<ArrayList<Seat>> layout) {
            int occupiedAdjacent = 0;
            ArrayList<Seat> sameRow = layout.get(row);
            if (col < sameRow.size()-1)
                if (sameRow.get(col+1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
    
            if (col > 0)
                if (sameRow.get(col-1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
             
            if (row < layout.size()-1) {
                ArrayList<Seat> belowRow = layout.get(row+1);
                if (belowRow.get(col).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}   
                if (col < sameRow.size()-1 && belowRow.get(col+1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
                if (col > 0 && belowRow.get(col-1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
            }
    
            if (row > 0) {
                ArrayList<Seat> aboveRow = layout.get(row-1);
                if (aboveRow.get(col).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}   
                if (col < sameRow.size()-1 && aboveRow.get(col+1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
                if (col > 0 && aboveRow.get(col-1).getState() == Seat.OCCUPIED) {occupiedAdjacent++;}
            }
            return occupiedAdjacent;
        }

        public int countOccupiedFirstVisible(List<ArrayList<Seat>> layout) {
            int occupiedFirstVisible = 0;
            ArrayList<Seat> sameRow = layout.get(row);
            if (col < sameRow.size()-1) {
                for (int i = 1; col+i < sameRow.size(); i++) {
                    if (sameRow.get(col+i).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; break;}
                    if (sameRow.get(col+i).getState() == Seat.EMPTY) {break;}
                }
            }
    
            if (col > 0) {
                for (int i = 1; col-i >= 0; i++) {
                    if (sameRow.get(col-i).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; break;}
                    if (sameRow.get(col-i).getState() == Seat.EMPTY) {break;}
                }
            }
             
            if (row < layout.size()-1) {
                boolean foundDown = false;
                boolean foundDownLeftDia = false;
                boolean foundDownRightDia = false;
                for (int i = 1, j = 1; row+i < layout.size(); i++, j++) {
                    ArrayList<Seat> belowRow = layout.get(row+i);
                    // Look down
                    if (!foundDown) {
                        if (belowRow.get(col).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundDown = true;}
                        if (belowRow.get(col).getState() == Seat.EMPTY) {foundDown = true;}

                    }
                    // Look down right
                    if (!foundDownRightDia) {
                        if (col+j < sameRow.size() && belowRow.get(col+j).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundDownRightDia = true;}
                        if (col+j < sameRow.size() && belowRow.get(col+j).getState() == Seat.EMPTY) {foundDownRightDia = true;}
                    }

                    // Look down left
                    if (!foundDownLeftDia) {
                        if (col-j >= 0 && belowRow.get(col-j).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundDownLeftDia = true;}
                        if (col-j >= 0 && belowRow.get(col-j).getState() == Seat.EMPTY) {foundDownLeftDia = true;}
                    }

                }
            }
    
            if (row > 0) {
                boolean foundUp = false;
                boolean foundUpLeftDia = false;
                boolean foundUpRightDia = false;
                for (int i = 1, j = 1; row-i >= 0; i++, j++) {
                    ArrayList<Seat> aboveRow = layout.get(row-i);
                    // Look up
                    if (!foundUp) {
                        if (aboveRow.get(col).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundUp = true;}
                        if (aboveRow.get(col).getState() == Seat.EMPTY) {foundUp = true;}

                    }
                    // Look up right
                    if (!foundUpRightDia) {
                        if (col+j < sameRow.size() && aboveRow.get(col+j).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundUpRightDia = true;}
                        if (col+j < sameRow.size() && aboveRow.get(col+j).getState() == Seat.EMPTY) {foundUpRightDia = true;}
                    }

                    // Look up left
                    if (!foundUpLeftDia) {
                        if (col-j >= 0 && aboveRow.get(col-j).getState() == Seat.OCCUPIED) {occupiedFirstVisible++; foundUpLeftDia = true;}
                        if (col-j >= 0 && aboveRow.get(col-j).getState() == Seat.EMPTY) {foundUpLeftDia = true;}
                    }

                }
            }
            return occupiedFirstVisible;
        }

    }

    public static void printLayout(List<ArrayList<Seat>> layout) {
        for (ArrayList<Seat> row : layout) {
            StringBuilder sb = new StringBuilder();
            for (Seat s : row) {
                sb.append(s);    
            }
            System.out.println(sb);
        }
    }

    public static void updateSeats(List<ArrayList<Seat>> layout) {
        for (ArrayList<Seat> row : layout) {
            for (Seat s : row) {
                s.update();
            }
        }
    }

    public static void applyRulesP1(List<ArrayList<Seat>> layout) {
        for (ArrayList<Seat> row : layout) {
            for (Seat s : row) {
                if (s.getState() == Seat.EMPTY && s.countOccupiedAdjacent(layout) == 0) {s.setNext(Seat.OCCUPIED);}
                else if (s.getState() == Seat.OCCUPIED && s.countOccupiedAdjacent(layout) >= 4) {s.setNext(Seat.EMPTY);}
            }
        }
    }

    public static void applyRulesP2(List<ArrayList<Seat>> layout) {
        for (ArrayList<Seat> row : layout) {
            for (Seat s : row) {
                if (s.getState() == Seat.EMPTY && s.countOccupiedFirstVisible(layout) == 0) {s.setNext(Seat.OCCUPIED);}
                else if (s.getState() == Seat.OCCUPIED && s.countOccupiedFirstVisible(layout) >= 5) {s.setNext(Seat.EMPTY);}
            }
        }
    }

    public static boolean stoppedMoving(List<ArrayList<Seat>> layout) {
        for (ArrayList<Seat> row : layout) {
            for (Seat s : row) {
                if (s.getState() != s.getNext())
                    return false;
            }
        }
        return true;
    }

    public static int occupiedSeats(List<ArrayList<Seat>> layout) {
        int occupied = 0;
        for (ArrayList<Seat> row : layout) {
            for (Seat s : row) {
                if (s.getState() == Seat.OCCUPIED)
                    occupied++;
            }
        }
        return occupied;
    }

    public static int solve(int part, String input) throws IOException {
        Scanner in = new Scanner(new File("src/Year2020/Day11/" + input + ".txt"));
        
        ArrayList<ArrayList<Seat>> seats = new ArrayList<>();
        while (in.hasNextLine()) {
            String rowString = in.nextLine();
            ArrayList<Seat> rowList = new ArrayList<>();
            for (char c : rowString.toCharArray()) {
                switch (c) {
                    case 'L':
                        rowList.add(new Seat(Seat.EMPTY, seats.size(), rowList.size()));
                        break;
                    case '.':
                        rowList.add(new Seat(Seat.FLOOR, seats.size(), rowList.size()));
                        break;
                    default:
                        throw new IllegalArgumentException("Char " + c + " not accepted.");
                }
            }
            seats.add(rowList);
        }

        while (true) {
            switch (part) {
                case 1:
                    applyRulesP1(seats);
                    break;
                case 2:
                    applyRulesP2(seats);
                    break;
                default:
                    System.out.println("You're silly!");
            }
            if (stoppedMoving(seats))
                break;
            updateSeats(seats);
        }

        in.close();
        return occupiedSeats(seats);
    }


    public static void main(String[] args) throws IOException {
            System.out.println("Part 1: " + solve(1, "input"));
            System.out.println("Part 2: " + solve(2, "input"));
        }
}
