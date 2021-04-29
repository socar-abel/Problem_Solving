#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 다음에 누를 키패드가 2,5,8,0일 때, 현재 키패드와 다음에 누를 키패드와의 거리를 return 하는 함수
int distance(string current, string next) {
    int d = 0;

    cout << "current : " << current << ", next : " << next << endl;

    if (next == "2") {
        if (current=="1"||current=="3"||current=="5") {
            d = 1;
        }
        else if (current == "4" || current == "6"|| current == "8") {
            d = 2;
        }
        else if (current == "7" || current == "9"|| current == "0") {
            d = 3;
        }
        else if (current == "*" || current == "#") {
            d = 4;
        }
    }
    else if (next == "5") {
        if (current == "1" || current == "3" || current == "0") {
            d = 2;
        }
        else if (current == "4" || current == "6" || current == "2" || current == "8") {
            d = 1;
        }
        else if (current == "7" || current == "9") {
            d = 2;
        }
        else if (current == "*" || current == "#") {
            d = 4;
        }
    }
    else if (next == "8") {
        if (current == "1" || current == "3") {
            d = 3;
        }
        else if (current == "4" || current == "6" || current == "2") {
            d = 2;
        }
        else if (current == "7" || current == "9" || current == "5" || current == "0") {
            d = 1;
        }
        else if (current == "*" || current == "#") {
            d = 2;
        }
    }
    else if (next == "0") {
        if (current == "1" || current == "3") {
            d = 4;
        }
        else if (current == "4" || current == "6" || current == "2") {
            d = 3;
        }
        else if (current == "7" || current == "9" || current == "5") {
            d = 2;
        }
        else if (current == "*" || current == "#" || current == "8") {
            d = 1;
        }
    }
    cout << "d : " << d << endl;
    return d;
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    // 왼손, 오른손의 현재 위치. 시작은 각각 *, #이다.
    string leftHand = "*";
    string rightHand = "#";

    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
            leftHand = to_string(numbers[i]);
            answer += "L";
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
            rightHand = to_string(numbers[i]);
            answer += "R";
        }
        else if (numbers[i] == 2 || numbers[i] == 5 || numbers[i] == 8 || numbers[i] == 0) {
            if (distance(leftHand, to_string(numbers[i]))> distance(rightHand, to_string(numbers[i]))) {
                cout << "left distance : " << distance(leftHand, to_string(numbers[i])) << endl;
                cout << "right distance : " << distance(rightHand, to_string(numbers[i])) << endl;
                rightHand = to_string(numbers[i]);
                answer += "R";
            }
            else if (distance(leftHand, to_string(numbers[i])) < distance(rightHand, to_string(numbers[i]))) {
                cout << "left distance : " << distance(leftHand, to_string(numbers[i])) << endl;
                cout << "right distance : " << distance(rightHand, to_string(numbers[i])) << endl;
                leftHand = to_string(numbers[i]);
                answer += "L";
            }
            else
            {
                cout << "left distance : " << distance(leftHand, to_string(numbers[i])) << endl;
                cout << "right distance : " << distance(rightHand, to_string(numbers[i])) << endl;
                if (hand == "right") {
                    rightHand = to_string(numbers[i]);
                    answer += "R";
                }
                else {
                    leftHand = to_string(numbers[i]);
                    answer += "L";
                }

            }
        }
    }

    cout << endl << "결과 : "<<answer<<endl;
    

    return answer;
}

int main() {
    vector<int> numbers = { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
    string hand = "right";

    solution(numbers, hand);

    return 0;
}
