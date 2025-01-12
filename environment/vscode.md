
# VSCode RMarkdown Environment Note

## Windows

1.  [安装 R 语言](https://cloud.r-project.org/)
2.  [安装 Vscode 的 R
    插件](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)
3.  [安装和配置 Radian](https://github.com/randy3k/radian)
4.  安装下列 R 包

``` shell
PS C:\Users\33695\Desktop> radian
R version 4.4.2 (2024-10-31 ucrt) -- "Pile of Leaves"
Platform: x86_64-w64-mingw32 (64-bit)

# 换源成清华源
r$> options("repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))

# 提供 VScode 中 R 语言的自动补全、代码格式化等功能
r$> install.packages("languageserver")

# 提供 RMarkdown 服务
r$> install.packages("rmarkdown")
```
