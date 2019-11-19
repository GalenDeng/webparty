# mysql 语句使用 (2019.11.19)

* mysql -u root   
* show databases	// 显示数据库
* use Party2020;  // 使用哪个数据库
* select * from signuprecord_partyname; // 从哪个表查询字段

* `解除安全模式`
* SET SQL_SAFE_UPDATES=0;


* `mac中可以使用 mysqlWorkbench 这个可视化software`

* `html中使用 jq 发送 json字符串给 python 后端`
* [html调用jq发送json字符串给 python 后端](https://github.com/GalenDeng/webparty/blob/master/index.html)

* `查询字段content`
* use Party2020;
* select name from signuprecord_partyname;

* `delete content`
* use Party2020;
* delete  from signuprecord_partyname where  name= "GalenDeng" ;



