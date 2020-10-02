package week2;

import java.util.*;

public class validParenthesis {
  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    HashMap<Character, Character> parenthesis_dict = new HashMap<>();
    parenthesis_dict.put('(', ')');
    parenthesis_dict.put('[', ']');
    parenthesis_dict.put('{', '}');
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (parenthesis_dict.containsKey(c)) {
        char topEle = stack.empty() ? '#' : stack.pop();
        if (topEle != parenthesis_dict.get(c)) {
          return false;
        } else {
          stack.push(c);
        }
      }
    }
    return stack.isEmpty();
  }
}
