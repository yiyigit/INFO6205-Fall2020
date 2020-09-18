import java.util.*;

public class TwoSum {
  private static int[] twoSumIndex(int[] arr, int target) {
    if (arr == null || arr.length == 0) {
      return new int[] { -1, -1 };
    }
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < arr.length; i++) {
      int other = target - arr[i];
      if (map.containsKey(other)) {
        return new int[] { map.get(other), i };
      }
      map.put(arr[i], i);
    }
    return new int[] { -1, -1 };
  }

  public static void main(String[] args) {
    System.out.println(twoSumIndex(new int[] { 2, 7, 11, 15 }, 9));
  }
}
