class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> memo(n, 0);
        int result = 0;
        
        for (int i = 0; i < n; i++)
            result = max(result, dfs(arr, d, i, memo));
        
        return result;
    }
    
private:
    int dfs(vector<int>& arr, int d, int i, vector<int>& memo) {
        if (memo[i]) return memo[i];
        
        int n = arr.size();
        memo[i] = 1; // at minimum, visit current index
        
        for (int j = i + 1; j <= min(i + d, n - 1); j++) {
            if (arr[j] >= arr[i]) break;  // blocked by equal or taller bar
            memo[i] = max(memo[i], 1 + dfs(arr, d, j, memo));
        }
        
        for (int j = i - 1; j >= max(i - d, 0); j--) {
            if (arr[j] >= arr[i]) break;  // blocked by equal or taller bar
            memo[i] = max(memo[i], 1 + dfs(arr, d, j, memo));
        }
        
        return memo[i];
    }
};