int minOperations(int* nums, int numsSize, int k) {
    int sum=0;
    for(int i=0;i<numsSize;i++){
        sum += nums[i];
    }
    if(sum<k) return sum;
    else if(sum%k==0) return 0;
    else{
        int res = sum%k;
        return res;
    }
}