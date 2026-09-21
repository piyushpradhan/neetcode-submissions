class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const count: {
            [key: number]: number;
        } = {};
        nums.forEach((num) => {
            count[num] = (count[num] || 0) + 1;
        });

        const heap = new MinPriorityQueue((x: [string, number]) => x[1]);
        Object.entries(count).forEach((entry: [string, number]) => {
            heap.enqueue(entry);
            if (heap.size() > k) heap.dequeue();
        });

        const result = [];
        while (!heap.isEmpty()) {
            result.push(Number(heap.dequeue()?.[0]));
        }

        return result;
    }
}
