
isPalindrome(int x){
    if(x == 0) {
            return true;
        }
        if(x < 0 || x%10 == 0)
            return false;
        
        int temp = 0;
        int previous = x;
        while (x > temp) {
            int pop = x%10;
            previous = x;
            x /= 10;

            temp = temp*10 + pop;
        }
        if(x == temp || previous == temp)
            return true;
        else
            return false;

}
