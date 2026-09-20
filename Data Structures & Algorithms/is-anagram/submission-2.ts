class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        
        const sorted_s = s.split('').sort();
        const sorted_t = t.split('').sort();
        let flag: boolean = true;

        if (sorted_s.length !== sorted_t.length) return false;

        sorted_s.forEach((s_element, index) => {
            if (s_element !== sorted_t[index]) {
                flag = false;
            }
        });

        return flag
    }
}
