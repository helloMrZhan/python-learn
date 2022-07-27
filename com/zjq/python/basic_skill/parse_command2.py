# 使用 optparse 库配置指定命令行选项，并解析命令行
# 1. 选项 '-s' 和选项 '--server' 等价
# 2. 选项 '--host' 设置默认为 0.0.0.0
# 3. 选项 '--port' 设置默认为 80
# 4. 选项 '--ssl' 如果指定，则 option.ssl=True。
from ast import parse
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()

    # 在此添加上述要求的4个命令行参数选项配置
    parser.add_option(
        "-s", "--server",
        dest="server",
        help="server",
        metavar="SERVER"
    )

    parser.add_option(
        "-h", "--host",
        dest="host",
        help="host",
        default='0.0.0.0',
        metavar="HOST"
    )

    parser.add_option(
        '-p', "--port",
        dest="port",
        help="port",
        default='80',
        metavar="PORT"
    )

    parser.add_option(
        "--ssl",
        dest="ssl",
        help="ssl",
        action="store_true",
        metavar="SSL"
    )

    (options, args) = parser.parse_args()
    print(f"server={options.server}")
    print(f"host={options.host}")
    print(f"port={options.port}")
    print(f"ssl={options.ssl}")