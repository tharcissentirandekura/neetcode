class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sChar = new int[26];
        int[] tChar = new int[26];

        // populate the s
        int base = (int) 'a';
        for (int i = 0;i<s.length();i++){
            // get the ascii code
            char c = s.charAt(i);
            int ascii = (int) c;
            int index = ascii - base;
            sChar[index] += 1;
        }

        // populate the t
        for (int i = 0;i<t.length();i++){
            // get the ascii code
            int ascii = (int) t.charAt(i);
            int index = ascii - base;
            tChar[index] += 1;
        }
        // for (int i = 0;i < sChar.length;i++){
        //     System.out.println(sChar[i] + " here" + tChar[i]);
        // }
        return Arrays.equals(sChar,tChar);
    }
}
