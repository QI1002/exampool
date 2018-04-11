
//1. Write a function to output the result (e.g. “t--es”) based on the puzzle and the guess.
//2. Assume you are given a library function scoreWithPuzzle(string guess, string& result), which scores your guess automatically. Create a game to find the puzzle by results from scoreWithPuzzle()
// minimize calls to scoreWithPuzzle()
// try to be fast
//3. if puzzle.size() = n
//avg = 1/(26^n) * (1*(1^n-0^n)+2*(2^n-1^n)+... 26*(26^n-(25)^n))

#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <math.h>
#include <time.h>

using namespace std;
void scoreWithPuzzle(string guess, string& result);

// p => puzzle
// g => guess 
// a => answer 
void scoreWithPuzzle(string &p, string &g, string &a)
{
    a = "";
    int i;
    for(i = 0; i < p.size() && i < g.size(); i++)
    { 
        if (p[i] == g[i]) a += p[i];
        else a += '-'; 
    }

    for(; i < p.size(); i++) a += '-';
}

int game(string &puzzle, string &result)
{
    const int count = 26;
    set<int> index;
    int calls = 0;
    string guess;
    result = "";
    for(int i = 0; i < puzzle.size(); i++) { result += "-"; index.insert(i); }
    
    do
    { 
        guess = result;
        for(auto it = index.begin(); it != index.end(); it++) 
        {
            if (calls >= count) 
            { cout << "can’t guess this puzzle" << endl; return -1; }
            guess[*it] = (char)('a'+ calls);  
        }

        //cout << guess << endl;
	scoreWithPuzzle(puzzle, guess, result); calls++;
        for(auto it = index.begin(); it != index.end(); ) 
	{
	    auto it2 = it; it++;	
            if (result[*it2] != '-') index.erase(it2);
	}

	int match = puzzle.size() - index.size();
	cout << calls << "(" << match << "):" << result << endl;
    }while(0 != index.size());

    return true;
}

void getAvgTimes(int n)
{
    const int count = 26;

    long long ll = 0;
    long long oldpow = 0;
    long long newpow;
    for(int i = 1; i <= count; i++)
    {
	newpow = pow(i, n);    
        ll += i * (newpow-oldpow);
	oldpow = newpow;
    }

    cout << ll << "//" << newpow << "=" << (double)ll/(double)newpow;
}

int main(int argc, char* argv[])
{
    const int count = 26;
    int n = 5;
    string puzzle = "     ";   
    srand((unsigned int)time(NULL));
    for(int i = 0; i < n; i++) puzzle[i] = (char)('a'+(rand()%count)); 

    string result;
    int r = game(puzzle, result);
    if (r > 0) 
    {
        if (result == puzzle) cout << "guess " << puzzle << " right" << endl;
        else cout << "guess " << puzzle << " wrong" << endl;
    }else
    {
        cout << "can’t guess " << puzzle << endl;
    }

    getAvgTimes(puzzle.size());
    return 0;
}
    


