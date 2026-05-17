class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap();

        // for (int num : nums){
        //     set.add(num);
        // }

        int[] res = new int[2];

        for (int i=0; i < nums.length;i++){
            int missing = target - nums[i];
            // System.out.println(i + " " + map.get(missing) + " " + target);
            if (map.containsKey(missing)){
                res[0] = map.get(missing);
                res[1] = i;
                return res;
            }else{
                //add it to map
                map.put(nums[i],i);
            }
        }

        return res;
    }
}
