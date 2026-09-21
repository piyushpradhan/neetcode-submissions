class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const freq: {
            [id: number]: number;
        } = {};
        nums.forEach((value) => {
            if (freq[value]) {
                freq[value]++;
            } else {
                freq[value] = 1;
            }
        });

        const sorted = Object.entries(freq).sort(
            (a: [string, number], b: [string, number]) => b[1] - a[1],
        );

        return sorted.slice(0, k).map(s => Number(s[0]));
    }
}
