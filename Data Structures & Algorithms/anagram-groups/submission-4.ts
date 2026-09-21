class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let result: string[][] = [];

        const strMap: { [key: string]: string[] } = {};

        strs.forEach((str: string) => {
            const alphabet: number[] = new Array(26).fill(0);
            str.split("").forEach((ch) => {
                alphabet[ch.charCodeAt(0) - "a".charCodeAt(0)]++;
            });
            if (strMap[alphabet.toString()]) {
                (strMap[alphabet.toString()] ?? []).push(str);
            } else {
                strMap[alphabet.toString()] = [str];
            }
        });

        return Object.values(strMap);
    }
}
