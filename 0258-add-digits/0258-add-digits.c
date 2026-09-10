int addDigits(int num) {
    int tem=0;
    tem = num;
     int sum=0;
    while (tem>9){
        int r = num%10;
         num = num/10;
         
         sum = num+r;
         tem = sum;
         num = sum;
    }
    return tem;
}