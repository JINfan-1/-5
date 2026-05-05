# ai-usage

如果你没有使用 AI，可以写：

> 本次没有使用 AI。

如果你使用了 AI，可以简单记录：

- 我问了什么：pytest报错（附加报错响应，以便ai快速了解面对的问题）
- ai建议：
    - 方案 1：直接修改测试文件：
        ```# 把这两行加在文件最顶部
        import sys
        from pathlib import Path

        #把项目根目录加入Python导入路径
        sys.path.insert(0, str(Path(__file__).parent.parent))

        #原来的导入语句
        from protocol import handle_message

        #下面写你的测试用例
        def test_handle_message():
            # 示例测试，根据你的业务逻辑修改
            assert handle_message(b"test") is not None
        ```
    - 方案 2：用python -m pytest命令运行
    - 方案 3：永久配置项目
        - 在 ** 项目根目录（任务五文件夹）** 新建一个文件，命名为pytest.ini，写入以下内容：
        ```
        [pytest]
        pythonpath = .
        ```
- 我有没有采纳：我采纳了方案二（不影响原代码，不会打乱现有思路）
- 我是怎么验证的：通过终端对指令的响应自行判断结合ai对响应的分析。
