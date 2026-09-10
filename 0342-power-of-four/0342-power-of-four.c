bool isPowerOfFour(int n) {
    if(n<=0) return false;
    else if(n==1) return true;
    else{
        while(n>1){
            if(n%4==0)
            n=n/4;
            else
            return false;
        }
        return true;
    }
}