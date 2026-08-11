class Solution {
public:
    bool isAnagram(string s, string t) {
        if (size(s)!=size(t)) return false;
        else {
            int chars[26] = {};
            for (int i=0; i<size(s); i++) {
                chars[(int)s[i] - 97] += 1;
                chars[(int)t[i] - 97] -= 1;
            }
            for (int i=0; i<26; i++) {
                if (chars[i]!=0) return false;
            }
            return true;
        }
    }
};
