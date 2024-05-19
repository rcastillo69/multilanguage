#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

int getHours(const string& hh) {
    try {
        return stoi(hh);
    } catch (const invalid_argument&) {
        cerr << "Invalid input for hours: " << hh << endl;
        return -1;
    } catch (const out_of_range&) {
        cerr << "Hours value out of range: " << hh << endl;
        return -1;
    }
}

string getTime(const string& input) {
    if (input.size() < 2) {
        cerr << "Invalid input size" << endl;
        return "";
    }
    return input.substr(0, input.size() - 2);
}

vector<string> getPartsTime(const string& input) {
    string timePart = getTime(input);
    vector<string> parts;
    istringstream iss(timePart);
    string part;
    while (getline(iss, part, ':')) {
        parts.push_back(part);
    }
    return parts;
}

string getMeridian(const string& input) {
    if (input.size() < 2) {
        cerr << "Invalid input size for meridian" << endl;
        return "";
    }
    return input.substr(input.size() - 2);
}

string getMilitarTime(const vector<string>& partsTime) {
    if (partsTime.size() != 3) {
        cerr << "Invalid time parts size" << endl;
        return "";
    }
    ostringstream oss;
    oss << setw(2) << setfill('0') << partsTime[0] << ":"
        << setw(2) << setfill('0') << partsTime[1] << ":"
        << setw(2) << setfill('0') << partsTime[2];
    return oss.str();
}

string timeConversion(const string& input) {
    string meridian = getMeridian(input);
    transform(meridian.begin(), meridian.end(), meridian.begin(), ::toupper);
    vector<string> partsTime = getPartsTime(input);

    if (partsTime.empty() || partsTime.size() != 3) {
        cerr << "Invalid time format" << endl;
        return "";
    }

    int hours = getHours(partsTime[0]);
    if (hours == -1) {
        return "";
    }

    if (meridian == "PM" && hours < 12) {
        partsTime[0] = to_string(hours + 12);
    } else if (meridian == "AM" && hours == 12) {
        partsTime[0] = "00";
    } else {
        partsTime[0] = (hours < 10 ? "0" + to_string(hours) : to_string(hours));
    }

    return getMilitarTime(partsTime);
}

int main() {
    string input;
    cin >> input;

    string result = timeConversion(input);
    if (!result.empty()) {
        cout << result << endl;
    }

    return 0;
}
