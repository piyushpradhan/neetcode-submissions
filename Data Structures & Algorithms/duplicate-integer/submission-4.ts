class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const numMap: Map<number, boolean> = new Map<number, boolean>();
        let flag: boolean = false;
        nums.forEach(num => {
            if (numMap.get(num)) {
                flag = true;
            }
            numMap.set(num, true);
        });

        return flag;
    }
}
