class Solution {
    public boolean isMatch(String s, String p) {
        // creates the memoization tabe (a cache)
        HashMap<String, Boolean> memo = new HashMap<>();
        return backTrack(s, p, 0 ,0, memo);
    }

    // 'i' is pointer for String s
    // 'j' is pointer for String p
    private boolean backTrack(String s, String p, int i, int j, HashMap<String, Boolean> memo){

        // temp key to add to hashtable.
        String key = i + "" + j;

        // return answer if it is in memoization table
        if (memo.containsKey(key)) return memo.get(key);

        // boolean that will be used to store in memo table
        Boolean result;

        // Base cases. If both pointers are out of bounds,
        // it is matched perfectly and returns true. If only the
        // j pointer is out of bounds, it returns false
        if (i >= s.length() && j >= p.length()) return true;
        if (j >= p.length()) return false;

        // returns true if p matches either s or '.'
        boolean match = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.');

        // handles logic for when a '*' is met in the pattern
        if (j+1 < p.length() && p.charAt(j+1) == '*'){
            result = (backTrack(s, p, i, j+2, memo) || // <---------- does not use *
                    (match && backTrack(s, p, i+1, j, memo)));//<--- does use *

            memo.put(key, result); // stores result in memoization table
            return result;
        }

        // handles when s and p match with no '*'' present
        result = match && backTrack(s, p, i+1, j+1, memo);
        memo.put(key, result);
        return result;
    }
}