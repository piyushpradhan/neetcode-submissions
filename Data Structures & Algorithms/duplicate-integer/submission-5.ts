class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const unique: Set<number> = new Set(nums);
        return unique.size !== nums.length;
    }
}
