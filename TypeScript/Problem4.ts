function isMatch(s: string, p: string): any {
    let memo:Map<string,boolean>=new Map();
    return backTrack(s,p,0,0,memo);
    


function backTrack(s:string,p:string,i:number,j:number,memo:Map<string,boolean>):any{
    let key:string=i+""+j;
        if(memo.has(key)) return memo.get(key);
        let result:boolean;
        if (i<s.length && j>=p.length) return true;
        if (j>=p.length) return false

        let match:boolean = i <s.length && (s.charAt(i)==p.charAt(j) || p.charAt(j)==".");
        if(j+1<p.length && p.charAt(j+1) == "*"){
            result=(backTrack(s,p,i,j+2,memo) || (match && backTrack(s,p,i+1,j,memo)));
            memo.set(key,result);
            return result;
        }
        result = match && backTrack(s,p,i+1,j,memo);
        memo.set(key,result);
        return result;
}
}
