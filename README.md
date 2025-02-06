<!-- markdownlint-disable MD033 MD036 MD041 -->

<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-logpile

_✨ 本地日志保存 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-logpile.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-logpile">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-logpile.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

将 nonebot 的日志记录保存到本地文件

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-logpile

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-logpile

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-logpile

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-logpile

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-logpile

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_logpile"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

|       配置项        | 必填 |  默认值  |                                                      说明                                                      |
| :-----------------: | :--: | :------: | :------------------------------------------------------------------------------------------------------------: |
|   `LOGPILE_PATH`    |  否  | `./logs` |                          日志文件保存路径，默认保存在当前工作目录下的 `logs` 文件夹中                          |
|   `LOGPILE_LEVEL`   |  否  | `ERROR`  | 日志保存等级，可以为列表或者字符串。如果是字符串，那么保存当前等级及以上所有等级的日志，否则只保存列表中的等级 |
| `LOGPILE_RETENTION` |  否  |   `14`   |                               日志文件保留时长，默认保留 14 天，自动清理过期日志                               |
