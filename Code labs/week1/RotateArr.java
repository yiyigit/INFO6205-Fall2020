public class RotateArr {
  private static void ratateArray(int[] nums, int k) {
    if (nums.length <= 1) {
      return;
    }
    k = k % nums.length;
    int[] tmp = new int[k];
    for (int i = 0; i < k; i++) {
      tmp[i] = nums[nums.length - k + 1];
    }
    for (int i = nums.length - k - 1; i >= 0; i--) {
      nums[i + k] = nums[i];
    }
    for(int i=0;i<k;i++){
      nums[i] = tmp[i];
    }

  }
}
