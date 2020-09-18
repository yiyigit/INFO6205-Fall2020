public class SumOfStrings {
  private static int sumTwoStrings(String str1, String str2) {
    if (str1.length() == 0 || str2.length() == 0) {
      return 0;
    }

    int value = Integer.parseInt(str1) + Integer.parseInt(str2);
    return value;

  }

  public static void main(String[] args) {

    System.out.println(sumTwoStrings("110", "23"));

  }
}