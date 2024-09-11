# 供nixos环境下使用
# 用法：
# 1. 命令行切换到当前目录
# 2. nix-shell，进入开发环境
# 3. jupyter server，启动jupyter服务器
# 4. 在vscode里面连接该服务器
#
# TODO：调查为什么直接从vscode里面启动服务器会出错。

let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.numpy
      python-pkgs.pygame
      python-pkgs.matplotlib
      python-pkgs.jupyter
      python-pkgs.notebook
      python-pkgs.polars
    ]))
  ];
}
