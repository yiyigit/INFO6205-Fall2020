import java.util.HashSet;

public class IsUnique {
  public boolean allUnique(int[] arr) {
    if (arr == null || arr.length <= 1) {
      return true;
    }
    HashSet<Integer> set = new HashSet<>();
    for (int num : arr) {
      if (set.contains(num)) {
        return false;
      }
      set.add(num);
    }
    return true;
  }
}
