/*#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int main()
{
    string csvFilePath = "5036730032586929.csv"; 
    ifstream csvFile(csvFilePath);
    string txtFilePath = "output.txt";
    string line;
    int lineCount = 0;
    int new_lineCount;

    if (!csvFile.is_open()) {
        cerr << "无法打开文件: " << csvFilePath << std::endl;
        return 1;
    }

    // 计算CSV文件的行数
    while (std::getline(csvFile, line)) {
        lineCount++;
    }
    csvFile.close();
    new_lineCount = lineCount + 1;

    //std::cout << new_lineCount;

    // 将第一次转发边关系写入
    ofstream txtFile(txtFilePath, ios::out);
    if (!txtFile.is_open()) {
        std::cerr << "无法创建文件: " << txtFilePath << std::endl;
        return 1;
    }
    for (int i = 2; i <= lineCount; ++i) {
        txtFile << "1-" << i << endl;
    }

    // 重新打开CSV文件并读取content列
    csvFile.open(csvFilePath);

    if (!csvFile.is_open()) {
        cerr << "无法打开文件: " << csvFilePath << std::endl;
        return 1;
    }


    // 跳过标题行
    getline(csvFile, line);
    lineCount = 1;

    while (std::getline(csvFile, line)) {
        lineCount++;
        istringstream iss(line);
        string content;
        // 读取content列
        getline(iss, content, ','); // 跳过mid
        getline(iss, content, ','); // 跳过publish_time
        getline(iss, content, ','); // 跳过user_name
        getline(iss, content, ','); // 跳过user_link
        getline(iss, content, ','); // 读取content

        int atCount = 0;
        for (char ch : content) {
            if (ch == '@') {
                atCount++;
            }
        }

        for (int i = 0; i < atCount; ++i) {
            txtFile << lineCount << "-" << new_lineCount << std::endl;
            new_lineCount += 1;
        }

    }

    csvFile.close();
    txtFile.close();

    cout << "新文件已更新。" << std::endl;

    return 0;
}*/