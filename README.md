# vue2-meituan（美团移动版）

> 用vue全家桶仿照美团APP实现移动端客户端。
>
> 计划实现外卖相关的所有功能，碍于本人水平有限，相关功能及页面的实现可能都比较简陋。

## 说明

工具&技能：

前端：vue2 + vuex + vue-router + axios

后端：nodejs + express + mongoDB

后端还调用了一些腾讯MAP的API：http://lbs.qq.com/webservice_v1/index.html

开发环境：

win10 x64  Chrome 64  nodejs 8.9.3 

## 使用

```
git clone https://github.com/tymzyx/vue2-meituan-fake.git

cd vue2-meituan-fake

npm install

npm run dev  // 开发环境

npm run build  // 打包 
```

## 目标功能

- [x] 登录及注册
- [ ] 修改密码
- [ ] 个人中心
- [ ] 上传与修改头像
- [ ] 增加、删除、修改地址
- [x] 定位功能
- [x] 选择城市
- [x] 搜索地址
- [ ] 搜索商家
- [ ] 根据评分、销量、距离等排序筛选
- [ ] 店铺详情页
- [ ] 商品详情页
- [ ] 购物车
- [ ] 下单功能
- [ ] 订单列表及详情
- [ ] 外卖功能之外的各种页面（仅UI)

## 项目结构

```
|—— build					// webpack配置文件
|—— config					// 项目打包配置
|—— dist					// 打包生成目录
|—— pyscript				// python爬虫脚本，爬取与存储数据
|—— src
|   |—— assets				// 静态文件
|   |—— components			// 组件
|   |—— pages				// 路由页面
|   |—— router				// 路由配置
|   |—— store				// vuex状态管理
|   |—— App.vue				// SPA页面入口
|   |—— main.js				// 程序入口
|—— index.html           	// 入口html
```

