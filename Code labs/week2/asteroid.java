package week2;

import java.util.*;

public class asteroid {
  public int[] asteroidCollision(int[] a) {
    LinkedList<Integer> s = new LinkedList<>(); // use LinkedList to simulate stack so that we don't need to reverse at
                                                // end.
    for (int i = 0; i < a.length; i++) {
      if (a[i] > 0 || s.isEmpty() || s.getLast() < 0)
        s.add(a[i]);
      else if (s.getLast() <= -a[i])
        if (s.pollLast() < -a[i])
          i--;
    }
    return s.stream().mapToInt(i -> i).toArray();
  }
}
