class Solution {
    public boolean hasDuplicate(int[] nums) {
        // return true if contains duplicate

        // version 1
        HashSet<Integer> uniqueValues = new HashSet();
        for (int num: nums){
            uniqueValues.add(num);
        }
        System.out.println(uniqueValues.size() + " " +  nums.length);
        if (uniqueValues.size() == nums.length){
            return false;
        }
        return true;
    }
}