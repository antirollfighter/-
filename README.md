# 微博爬虫项目

## 项目介绍

本项目是一个微博爬虫工具，具备以下功能：

1. **爬取文字**：从微博页面抓取微博文本内容。
2. **爬取图片**：下载微博中的图片资源。
3. **爬取转发关系**：获取微博转发信息并建立转发关系。
4. **将转发关系规范成边关系并导入neo4j图数据库进行可视化**：将抓取的转发关系按边关系格式整理，导入neo4j图数据库，进行关系可视化展示。

## 前置需求

在运行本项目之前，请确保满足以下环境与依赖要求：

1. **Python 解释器**：请使用 3.6 版本的 Python。
2. **开发工具**：建议使用 PyCharm IDE，并根据提示安装相应的库。
3. **Neo4j 运行环境**：请提前自行准备好 Neo4j 图数据库的运行环境。

### 安装步骤

1. **安装 Python 3.6**：
    - 请前往 [Python 官方网站](https://www.python.org/downloads/release/python-360/) 下载并安装 Python 3.6。

2. **配置 PyCharm**：
    - 下载并安装 [PyCharm](https://www.jetbrains.com/pycharm/download/)，并根据项目需要安装相应的 Python 库。例如，您可以从 `requirements.txt` 文件中安装所有依赖库：
      ```bash
      pip install -r requirements.txt
      ```

3. **准备 Neo4j 环境**：
    - 请前往 [Neo4j 官方网站](https://neo4j.com/download/) 下载并安装 Neo4j，并确保其正常运行。

## 使用说明

1. **克隆项目**：
    ```bash
    git clone https://github.com/yourusername/weibo-crawler.git
    cd weibo-crawler
    ```

2. **运行爬虫**：
    - 根据项目代码中的说明，启动爬虫以抓取微博数据。

3. **导入 Neo4j**：
    - 运行相关脚本，将转发关系数据导入 Neo4j 图数据库，并进行可视化操作。

## 贡献

欢迎提交 issue 或 pull request 来改善本项目。如有任何问题，请联系项目维护者。

---

感谢使用本项目！希望它能对您的工作有所帮助。
