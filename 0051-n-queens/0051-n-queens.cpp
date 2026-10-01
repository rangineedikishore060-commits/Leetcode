class Solution {
public:
    bool isValid(int row,int col,vector<string>&board,int n){
        //top
        int tempr = row,tempc = col;
        while(tempr>=0){
            if(board[tempr][col]=='Q') return false;
            tempr--;
        }
        tempr=row;
        while(tempr>=0 && tempc>=0){
            if(board[tempr][tempc]=='Q') return false;
            tempr--;
            tempc--;
        }
        tempr = row;
        tempc = col;
        while(tempr>=0 && tempc<n){
            if(board[tempr][tempc]=='Q') return false;
            tempr--;
            tempc++;
        }
        return true;
    }

     void solve(int row, vector<vector<string>>&possibility, vector<string>&board, int n){
        if (row == n){
            possibility.push_back(board);
            return;
        }
        for(int col = 0; col < n; col++){
            if(isValid(row,col,board,n)){
                board[row][col] = 'Q';
                solve(row + 1,possibility,board,n);
                board[row][col] = '.';
            }
        }
    }


    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>possibility;
        vector<string>board;
        for(int i = 0; i < n; i++){
            string s;
            for(int j = 0; j < n; j++){
                s += '.';
            }
            board.push_back(s);
        }

        solve(0,possibility,board,n);
        return possibility;
    }
};