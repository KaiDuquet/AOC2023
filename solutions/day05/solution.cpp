#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector<std::string> split(const std::string& str, const std::string& delim) 
{
    std::vector<std::string> tokens;
    size_t pos = 0;
    while (pos < str.length()) 
    {
        // Find the position of the next occurrence of the delimiter
        size_t next = str.find(delim, pos);
        if (next == std::string::npos) 
        {
            next = str.length();
        }
        // Extract the token from the string
        std::string token = str.substr(pos, next-pos);
        if (!token.empty())
        {
            tokens.push_back(token);
        }
        // Update the position to start searching from the next character
        pos = next + delim.length();
    }
    return tokens;
}


int main() {

	std::ifstream in("day05.txt");
	std::vector<std::string> lines;
	std::string line;
	while (std::getline(in, line)) {
		lines.push_back(line);
	}
	in.close();

	std::vector<uint64_t> seeds = {3489262449, 222250568, 2315397239, 327729713, 1284963, 12560465, 1219676803, 10003052, 291763704, 177898461, 136674754, 107182783, 2917625223, 260345082, 1554280164, 216251358, 3900312676, 5629667, 494259693, 397354410};
	std::cout << seeds.size() << std::endl;
	return 0;
}