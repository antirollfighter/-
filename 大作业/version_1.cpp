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
        cerr << "�޷����ļ�: " << csvFilePath << std::endl;
        return 1;
    }

    // ����CSV�ļ�������
    while (std::getline(csvFile, line)) {
        lineCount++;
    }
    csvFile.close();
    new_lineCount = lineCount + 1;

    //std::cout << new_lineCount;

    // ����һ��ת���߹�ϵд��
    ofstream txtFile(txtFilePath, ios::out);
    if (!txtFile.is_open()) {
        std::cerr << "�޷������ļ�: " << txtFilePath << std::endl;
        return 1;
    }
    for (int i = 2; i <= lineCount; ++i) {
        txtFile << "1-" << i << endl;
    }

    // ���´�CSV�ļ�����ȡcontent��
    csvFile.open(csvFilePath);

    if (!csvFile.is_open()) {
        cerr << "�޷����ļ�: " << csvFilePath << std::endl;
        return 1;
    }


    // ����������
    getline(csvFile, line);
    lineCount = 1;

    while (std::getline(csvFile, line)) {
        lineCount++;
        istringstream iss(line);
        string content;
        // ��ȡcontent��
        getline(iss, content, ','); // ����mid
        getline(iss, content, ','); // ����publish_time
        getline(iss, content, ','); // ����user_name
        getline(iss, content, ','); // ����user_link
        getline(iss, content, ','); // ��ȡcontent

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

    cout << "���ļ��Ѹ��¡�" << std::endl;

    return 0;
}*/