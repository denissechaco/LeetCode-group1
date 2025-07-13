function lengthOfLongestSubstring(s: string): any {
    let left:number=0;
    let longest:number=0;
    let subString:Set<string> = new Set();
    for(let right=0;right< s.length;right++){
        while(subString.has(s.charAt(right))){
            subString.delete(s.charAt(left));
            left++;
        }

        let ventana = (right - left) + 1;
        longest = Math.max(longest,ventana);
        subString.add(s.charAt(right));
    }
    return longest;
};
