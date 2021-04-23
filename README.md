# AJ-PinXixi
## 西电软件项目管理

上传时请先传至开发版（develop），等到某一系列工作完成，有一定程度的变更后再合并到release分支

![img](https://images2015.cnblogs.com/blog/718344/201609/718344-20160913141526648-581574208.png)
## 后端部分
目前暂时用的是flask，需要后端组各位慢慢转移成java的那套实现
主要关注两个文件夹
flaskProject/app/api（几个接口的实现）
flaskProject/app/models（数据库部分的类）
![image](https://user-images.githubusercontent.com/49947867/115844963-f46d2800-a452-11eb-894a-517b3da56141.png)
目前的后端接口设计还需要解决几个问题
1. 商品修改信息并上架的功能有了，但是没和users联系起来，还需要在good和user之间建立联系（可能多建一个归属的表会好点）
2. 需要有一个购买接口接受三个参数（userID1，userID2，goodID），并且返回一个含有成功信息的json
3. 需求分析的时候提出了一个购物车的需求，如何实现也需要后端组再考虑一下（而且需要考虑到，可能有多个用户同时拉进购物车）
4. release2有一个需求是留言板的功能，也需要后端组的讨论并实现
