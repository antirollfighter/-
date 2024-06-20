#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

struct WeiboData {
    std::string user_name;
    std::string content;
};

bool parseCSV(const std::string& filename, std::vector<WeiboData>& data) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return false;
    }

    std::string line;
    // 跳过标题
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::istringstream sline(line);
        std::string field;
        WeiboData entry;

        // 跳过无关列
        std::getline(sline, field, ',');  // mid
        std::getline(sline, field, ',');  // publish_time
        std::getline(sline, entry.user_name, ',');  // user_name
        std::getline(sline, field, ',');  // user_link
        std::getline(sline, entry.content, ',');  // content

        data.push_back(entry);
    }

    file.close();
    return true;
}

int main() {
    const std::string csv_filename = "5036730032586929.csv";
    const std::string output_filename = "output1.txt";
    std::vector<WeiboData> data;

    if (!parseCSV(csv_filename, data)) {
        return 1;
    }

    std::ofstream outfile(output_filename);
    if (!outfile.is_open()) {
        std::cerr << "Unable to open file: " << output_filename << std::endl;
        return 1;
    }

    int n = 2;

    // 第二行开始读
    for (size_t i = 0; i < data.size(); ++i) {
        const std::string& content = data[i].content;
        size_t pos = content.find("//@");

        if (pos == std::string::npos) {
            outfile << "1-" << n << std::endl;
            n += 1;
        }
        else {
            size_t start = pos + 3;  
            size_t end = content.find(':', start);
            if (end != std::string::npos) {
                std::string temp_user = content.substr(start, end - start);
                int temp_linecount = 2;
                bool found = false;

                for (size_t j = 0; j < i; ++j) {
                    if (data[j].user_name == temp_user) {
                        outfile << temp_linecount << "-" << n << std::endl;
                        n += 1;
                        found = true;
                        break;
                    }
                    temp_linecount++;
                }

                if (!found) {
                    n += 1;  
                    outfile << "1-"<<n << std::endl;
                }
            }
        }
    }

    outfile.close();
    return 0;
}