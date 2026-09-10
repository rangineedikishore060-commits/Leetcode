/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 int min(int* arr,int numsSize){
    int minid=0;
    for(int i=0;i<numsSize;i++){
        if(arr[i]<arr[minid]){
            minid = i;
        }
    }
    return minid;
 }
int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
    int* arr = (int*)malloc(numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        arr[i] = nums[i];
    }
    for(int i=0;i<k;i++){
        int minid = min(arr,numsSize);
         arr[minid] = arr[minid]*multiplier;
    }
    *returnSize = numsSize;
    return arr;
} 