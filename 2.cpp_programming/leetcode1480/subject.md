
## Leetcode 1480. Running Sum of 1D Array

### Subject
- given an array `nums`, define a new array as `runningSum`
```
runningSum[i] = nums[0] + nums[1] + ... + nums[i]
``` 

- constraints: 
 - the number of elemnts in the array is in range [1, 1000]
 - each element of the array is in rage[-10⁶, 10⁶
]


### example
```
Input: nums = [3,1,2,10,1]
Output:       [3,4,6,16,17]
```

### concept

#### complexity
- time complexity = O(n)
 - why? we loop through the array once, from index `0` to `n-1`. For each element we perform a single addition. So the time complexity is O(n), where `n` is the length of the input array.

- space complexity = O(n) 
 - why? the new array `runningSum` has the same length as the input array `nums`. Thus we use additional memory that grows linearly with the input size.
 - caution! if we modify the input array `num` in-place without creating a new one. We could reduce the space complexity to `O(1)`. But in this problem, we return a new array, then extra space is required.

