#!/bin/bash

set -e  # 遇到错误时停止脚本

trap 'echo "Error occurred at line $LINENO."; exit 1' ERR

# 定义构建名称和构建号
BUILD_NAME="test-jfrog-cil-sh"
BUILD_NUMBER="0.0.1"

# 定义 text.json 文件的路径
SPEC_PATH="/home/zhanghuimin/JFrogArtifactory/JFrogArtifactoryCLI/test_jfrog_upload.json"

echo '上传制品到JFrog...'
jf rt u --spec=$SPEC_PATH --build-name=$BUILD_NAME --build-number=$BUILD_NUMBER

echo '收集环境变量...'
jf rt bce $BUILD_NAME $BUILD_NUMBER

echo '收集Git信息...'
jf rt bag $BUILD_NAME $BUILD_NUMBER

echo '添加依赖项...'
jf rt bad $BUILD_NAME $BUILD_NUMBER /home/zhanghuimin/JFrogArtifactory/dependence/

echo '发布构建信息...'
jf rt bp $BUILD_NAME $BUILD_NUMBER
