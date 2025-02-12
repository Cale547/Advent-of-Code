public class testing {
    public static void main(String[] args) {
        int a = -1;
        for (int i = 0; i < 5; i++) {
            a = (a+2) % 8;
            System.out.println(a);
        }

    }
}
