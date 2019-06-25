#用户名设置

git config --global user.name "[name]"

#邮件地址设置

git config --global user.email "[email address]"

#主题设置

git config --global color.ui auto

#列出所有要提交的新文件或修改的文件

git status

#显示尚未暂存的文件差异

git diff

#快照文件以准备版本控制 

git add [file]

#取消对文件的排序，但保留其内容 

git reset [file]



#显示尚未暂存的文件差异

git diff


#显示临时文件版本和最后一个文件版本之间的文件差异 

git diff --staged


#在版本历史记录中永久记录文件快照

git commit -m "[descriptive message]"


