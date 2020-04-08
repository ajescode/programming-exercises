import java.util.*;

class GCD {
    public int generalizedGCD(int num, int[] arr) {
        ArrayList<Integer> divisors = new ArrayList<Integer>();
        for (int i=0; i<num;i++) {
            divisors.add(i);
        }

        while (divisors.size() > 1) {
            while (!divisors.get(0).equals(divisors.get(1))) {
                if (divisors.get(0) > divisors.get(1)) {
                    divisors.set(0, divisors.get(0) - divisors.get(1));
                } else {
                    divisors.set(1, divisors.get(1) - divisors.get(0));
                }
            }
            divisors.remove(1);
        }

        return divisors.get(0);
    }

    public static void main(String[] args) {

        GCD solution = new GCD();
        int[] numbers = new int[]{4,4,8,8,12};
        int n = 5;

        int result = solution.generalizedGCD(n, numbers);
        System.out.println(result);
    }
}