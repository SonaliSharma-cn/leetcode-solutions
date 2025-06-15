class Solution {
public:
    string generateTag(string caption) {
        stringstream ss(caption);
        string word;
        string result = "#";
        bool firstWord = true;

        while (ss >> word) {
            string cleaned = "";
            // Remove non-letter characters from word
            for (char c : word) {
                if (isalpha(c)) {
                    cleaned += c;
                }
            }
            if (cleaned.empty()) continue;

            // Handle first word: lowercase
            if (firstWord) {
                for (char& c : cleaned) {
                    result += tolower(c);
                }
                firstWord = false;
            } else {
                // Capitalize first letter, rest lowercase
                result += toupper(cleaned[0]);
                for (int i = 1; i < cleaned.size(); i++) {
                    result += tolower(cleaned[i]);
                }
            }
        }
        // Truncate to 100 characters
        if (result.size() > 100)
            result = result.substr(0, 100);

        return result;
    }
};
