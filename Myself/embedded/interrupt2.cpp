// g++ -std=gnu++11 ./interrupt.cpp -lpthread  
#include <algorithm>
#include <iostream>
#include <utility>

#include <cstring>
#include <climits>
#include <ostream>
#include <sstream>
#include <list>
#include <string>
#include <deque>
#include <vector>
#include <memory>
#include <functional>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <unistd.h>

using namespace std;

vector<int> h;
int wp, rp, size;
// wp, rp is not ring buffer pointer, they are the count for read & write
mutex mtx, mtx2, mtx3;
condition_variable cv2, cv3;
bool run;

int getSize() {
  lock_guard<mutex> g(mtx);
  return size;
}

void incSize() {
  lock_guard<mutex> g(mtx);
  cout << "+" << ++size << endl;
}

void decSize() {
  lock_guard<mutex> g(mtx);
  cout << "-" << --size << endl;
}

void updateWP(int a) {
  lock_guard<mutex> g(mtx);
  wp = a;
}

void updateRP(int a) {
  lock_guard<mutex> g(mtx);
  rp = a;
}

void decWP() {
  lock_guard<mutex> g(mtx);
  --wp;
}

void decRP() {
  lock_guard<mutex> g(mtx);
  --rp;
}

int getWP() {
  lock_guard<mutex> g(mtx);
  return wp;
}

int getRP() {
  lock_guard<mutex> g(mtx);
  return rp;
}

void inputkey() {
  while(true) {
      while(getWP() || (getRP() && size >= getRP())) usleep(100); 
      string s;
      cout << "input: ";
      cin >> s;
      if (s == "exit") {
        run = false; 
        cv2.notify_all();
        cv3.notify_all();
        break;
      }

      int i = stoi(s);
      if (i < 0) {
         //updateRP(-i); 
         size += i; // i is negative
         cv2.notify_all();
      }else {
         updateWP(i);
      }
  }
}

void deque_() {
  unique_lock<mutex> lck3(mtx3);
  while(run) {
      while(getRP() > 0) {
          while(run && getSize() == 0) cv3.wait(lck3);  
          if (!run) break;
          decSize();
          cv2.notify_all();
          decRP();
      }
  }
}

void enque_() {
  unique_lock<mutex> lck2(mtx2);
  while(run) {
      while(getWP() > 0) {
          while(run && getSize() == 20) cv2.wait(lck2);  
          if (!run) break;
          incSize();
          cv3.notify_all();
          decWP();
      }
  }
}

int main(void) 
{
  h.resize(100);
  run = true;
  wp = rp = size = 0;
  //wp = 200; rp = 200;
  thread t(inputkey);
  //thread t1(deque_);
  thread t2(enque_);

  t.join();
  //t1.join();
  t2.join(); 
  return 0; 
} 

