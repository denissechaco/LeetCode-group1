class Solution {
    public int lengthOfLongestSubstring(String s) {
        // left tracks the starting character of the current substring
        int left = 0;
        int longest = 0;
        HashSet<Character> subString = new HashSet<>();

        // right tracks the ending character of the current substring
        for (int right = 0; right < s.length(); right++){

            // while the HashSet contains the char at the right index, remove the
            // char of the left index from the HsashSet and move the left index up one
            while(subString.contains(s.charAt(right))){
                subString.remove(s.charAt(left));
                left++;
            }

            // length of the current substring
            int window = (right - left) + 1;
            longest = Math.max(longest, window);

            // add char to substring
            subString.add(s.charAt(right));
        }
        return longest;
    }
}