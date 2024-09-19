
def create_shell_script(build_name, build_number, spec_path, dependencies_path):
    """生成一个 .sh 文件来执行 JFrog CLI 操作"""
    with open("run_jfrog_operations.sh", "w") as f:
        f.write("#!/bin/bash\n\n")
        f.write("set -e  # 遇到错误时停止脚本\n\n")

        # 捕获错误的 trap 命令
        f.write("trap 'echo \"Error occurred at line $LINENO.\"; exit 1' ERR\n\n")

        f.write("# 定义构建名称和构建号\n")
        f.write(f"BUILD_NAME=\"{build_name}\"\n")
        f.write(f"BUILD_NUMBER=\"{build_number}\"\n\n")

        f.write("# 定义 text.json 文件的路径\n")
        f.write(f"SPEC_PATH=\"{spec_path}\"\n\n")

        f.write("echo '上传制品到JFrog...'\n")
        f.write("jf rt u --spec=$SPEC_PATH --build-name=$BUILD_NAME --build-number=$BUILD_NUMBER\n\n")

        f.write("echo '收集环境变量...'\n")
        f.write("jf rt bce $BUILD_NAME $BUILD_NUMBER\n\n")

        f.write("echo '收集Git信息...'\n")
        f.write("jf rt bag $BUILD_NAME $BUILD_NUMBER\n\n")

        f.write("echo '添加依赖项...'\n")
        f.write(f"jf rt bad $BUILD_NAME $BUILD_NUMBER {dependencies_path}\n\n")

        f.write("echo '发布构建信息...'\n")
        f.write("jf rt bp $BUILD_NAME $BUILD_NUMBER\n")

    # 给生成的 .sh 文件可执行权限
    import os
    os.chmod("run_jfrog_operations.sh", 0o755)
    print("生成的Shell脚本已保存为 run_jfrog_operations.sh 并已设置可执行权限。")


if __name__ == "__main__":
    # 替换为您的实际值
    build_name = "test-jfrog-cil-sh"
    build_number = "0.0.1"
    spec_path = "/home/zhanghuimin/JFrogArtifactory/JFrogArtifactoryCLI/test_jfrog_upload.json"
    dependencies_path = "/home/zhanghuimin/JFrogArtifactory/dependence/"

    # 创建Shell脚本
    create_shell_script(build_name, build_number, spec_path, dependencies_path)
