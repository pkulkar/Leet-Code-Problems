
int* twoSum(int* nums, int numsSize, int target) {
   
    int Cache[numsSize];
    int CacheCnt=0;
    int i;
    int inputCnt=0;
    
    int static returnAry[2];
    
    for(inputCnt=0;inputCnt<numsSize;inputCnt++){
        int Diff = target - nums[inputCnt];
        if(inputCnt==0){
            Cache[CacheCnt]=Diff;
            CacheCnt++;
        }
        else{
            for(i=0; i< CacheCnt; i++){
                if(nums[inputCnt] == Cache[i]){
                    returnAry[0] = i;
                    returnAry[1] = inputCnt;
                    return returnAry;
                }
            }
            if(inputCnt!=0){
            Cache[CacheCnt]=Diff;
            CacheCnt++;}
        }
    }
    return returnAry;
}