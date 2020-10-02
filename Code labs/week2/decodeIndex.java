package week2;

import java.util.*;

public class decodeIndex {
  public String decodeAtIndex(String S, int K) {
    long total = 0;
    String res = "";
    Stack<long[]> stack = new Stack<>();
    for (int i = 0; i < S.length(); i++) {
      char c = S.charAt(i);
      if (Character.isDigit(c)) {
        int T = Integer.parseInt(c + "");
        total *= T;
        stack.push(new long[] { i, total, T });
      } else
        total++;
    }
    if (stack.size() == 0)
      return S.charAt(K - 1) + "";
    if (stack.peek()[1] != total)
      stack.push(new long[] { S.length(), total, 1 });
    while (stack.size() != 0) {
      long pair[] = stack.pop();
      int index = (int) (pair[0]);
      long cnt = pair[1];
      long group = cnt / pair[2];
      K %= group;
      if (K == 0)
        K = (int) group;
      if (stack.size() == 0) {
        return S.charAt(K - 1) + "";
      } else if (stack.size() != 0 && K > stack.peek()[1]) {
        res = "" + S.charAt((int) (stack.peek()[0] + (K - stack.peek()[1])));
        break;
      }
    }
    return res;
  }
}
