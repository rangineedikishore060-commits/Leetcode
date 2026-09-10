/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
    int cnt=0;
    int* arr=(int*)malloc(numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i] == nums[j]){
                arr[cnt] = nums[i];
                cnt++;
                break;
            }
        }
    }
    *returnSize = 2;
    return arr;
}