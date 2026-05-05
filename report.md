# 作业报告

## 基本信息
- 你的仓库地址：https://github.com/JINfan-1/-5
- 开发分支名：dev-tcp-protocol
- Pull Request 链接（如果有）：无

---

## 我做了什么
1.  阅读 `TASK.md` 和 `protocol.py`，明确了TCP文本协议服务器的任务要求。
2.  在开发分支 `dev-tcp-protocol` 中，补全了 `protocol.py` 中的 `ECHO`/`UPPER`/`ADD` 命令，并完善了空消息、无效参数、未知命令的错误处理。
3.  运行 `python -m pytest tests/ -v`，验证所有7个测试用例全部通过。
4.  启动 `server.py` 和 `client_example.py`，完成了端到端通信测试，验证所有命令响应正常。
5.  将开发分支推送到远程GitHub仓库，并按要求填写了作业报告。

---

## 我遇到的问题
1.  初始运行 `pytest` 时出现 `ImportError`，无法导入 `protocol.py`，通过使用 `python -m pytest tests/ -v` 命令解决了模块导入路径问题。
2.  原始 `protocol.py` 存在TODO未实现，测试不通过，通过补全命令逻辑和错误处理解决。

---

## 我如何验证
- 单元测试：`python -m pytest tests/ -v` 所有用例通过。
- 端到端测试：`python server.py` + `python client_example.py`，通信正常，响应符合预期。

---

## 总结
- 本次任务让我理解了TCP服务器与客户端的通信流程，掌握了文本协议的实现方法，熟悉了Git分支开发的完整流程，学会了使用pytest进行自动化测试。
- 我认为这次最难的部分在于认识TCP服务器与客户端的通信流程、如何对代码进行补充修改以及怎么认识各文件间的内在联系
