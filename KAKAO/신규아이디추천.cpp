#include <iostream>
#include <string>
#include <vector>

using namespace std;

string step1(string input) {
    string result = "";

    for (int i = 0; i < input.size(); i++) {
        input[i] = tolower(input[i]);
    }

    result = input;

    cout << "step1 : " << input << endl;

    return result;
}

bool step2check(char c) {
    if (
        ('a' <= c && c <= 'z')
        || ('0' <= c && c <= '9')
        || c == '-' || c == '_' || c == '.'
        )
    {
        return true;
    }
    else return false;
}

string step2(string input) {
    string result = "";

    for (int i = 0; i < input.size(); i++) {
        if (step2check(input[i])) {
            result += input[i];
        }
    }

    cout << "step2 : " << result << endl;

    return result;
}


string step3(string input) {    //연속된 마침표 삭제
    string result = "";

    // 편한 삭제를 위해 vector에 string 담기
    vector<char> vec;
    for (int i = 0; i < input.size(); i++) {
        vec.push_back(input[i]); 
    }

    bool isPeriod = false;
    
    for (int i = 0; i < vec.size(); i++) {

        if (isPeriod == true)//이전 원소가 period 일 때
        {
            if (vec[i] == '.')//현재 원소가 period
            {
                isPeriod = true;
                vec.erase(vec.begin() + i);
                i = i - 1;  //vec를 지웠으므로 한 칸 뒤로 가야함
            }
            else {//현재 원소가 period 아님
                isPeriod = false;
            }
        }
        else {//이전 원소가 period 아닐 때
            if (vec[i] == '.')//현재 원소가 period
            {
                isPeriod = true;
            }
            else {//현재 원소가 period 아님
                isPeriod = false;
            }
        }

    }

    for (int i = 0; i < vec.size(); i++) {
        result += vec[i];
    }

    cout << "step3 : " << result << endl;

    return result;
}

string step4(string input) { // 마침표가 처음이나 끝에 위치한다면 삭제
    string result = "";

    // 편한 삭제를 위해 vector에 string 담기
    vector<char> vec;
    for (int i = 0; i < input.size(); i++) {
        vec.push_back(input[i]);
    }

    if (vec.front() == '.') {
        vec.erase(vec.begin());
    }

    if (vec.back() == '.') {
        vec.pop_back();
    }

    for (int i = 0; i < vec.size(); i++) {
        result += vec[i];
    }

    cout << "step4 : " << result << endl;

    return result;
}

string step5(string input) { // 빈 문자열이라면 'a' 추가
    string result = "";

    if (input.size() == 0) {
        result += 'a';
    }
    else {
        result = input;
    }

    cout << "step5 : " << result << endl;

    return result;
}

string step6(string input) { //길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    //만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    string result = "";

    vector<char> vec;
   
   
    if (input.size() >= 16) {
        for (int i = 0; i < 15; i++) {
            cout << i<<" : "<<input[i];
            vec.insert(vec.begin() + i, input[i]);
        }
    }
    else {
        for (int i = 0; i < input.size(); i++) {
            vec.push_back(input[i]);
        }
    }
    
    if (vec.back() == '.') {
        vec.pop_back();
    }

    for (int i = 0; i < vec.size(); i++) {
        result += vec[i];
    }

    cout << "step6 : " << result << endl;
    

    return result;
}

//길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
string step7(string input) {
    string result = "";

    if (input.size() <= 2) {
        char back = input[input.size()-1];
        while (input.size() != 3) {
            input += back;
        }
    }

    result = input;

    cout << "step7 : " << result << endl;

    return result;
}

string solution(string new_id) {
    string answer = "";
    answer = step7(step6(step5(step4(step3(step2(step1(new_id)))))));
    return answer;
}
