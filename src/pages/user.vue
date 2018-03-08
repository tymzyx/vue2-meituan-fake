<template>
  <div class="user-wrapper">
    <div class="user-top">
      <i class="iconfont icon-set icon0"></i>
      <i class="iconfont icon-palette icon1"></i>
      <i class="iconfont icon-sey-letter-a icon2"></i>
    </div>
    <div class="user-head">
      <div class="user-profile">
        <div class="user-img"></div>
        <span>请点击登录</span>
      </div>
      <div class="user-head-top"></div>
      <div class="user-head-bottom">
        <div class="user-head-info">
          <div v-for="item in headInfo" class="head-item">
            <i :class="item.icon" :style="{color: item.color}"></i>
            <span>{{item.name}}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="user-body">
      <div class="wallet">
        <p>美团钱包</p>
        <div class="wallet-main">
          <div v-for="item in walletInfo" class="service-item">
            <i :class="item.icon"></i>
            <span>{{item.name}}</span>
          </div>
        </div>
      </div>
      <div class="service">
        <p>美团服务</p>
        <div class="service-main">
          <div v-for="item in serviceInfo" class="wallet-item">
            <i :class="item.icon" :style="{color: item.color}"></i>
            <span>{{item.name}}</span>
          </div>
        </div>
      </div>
      <div class="blank"></div>
    </div>
    <common-foot activeKey="4"></common-foot>
  </div>
</template>

<script>
  import CommonFoot from '../components/CommonFoot'

  let headInfo = [
    {name: '收藏', icon: 'iconfont icon-shoucang', color: '#EE6A50'},
    {name: '评价', icon: 'iconfont icon-pingjia', color: '#63B8FF'},
    {name: '足迹', icon: 'iconfont icon-shizhong', color: '#48D1CC'}
  ]

  let walletInfo = [
    {name: '我的钱包', icon: 'iconfont icon-wallet'},
    {name: '红包/卡券', icon: 'iconfont icon-hongbao'},
    {name: '银行卡', icon: 'iconfont icon-card'},
    {name: '闪付', icon: 'iconfont icon-card-o'},
    {name: '美团信用卡', icon: 'iconfont icon-pokercard'},
    {name: '信用卡还款', icon: 'iconfont icon-yinhangka'},
    {name: '银联二维码', icon: 'iconfont icon-erweima'}
  ]

  let serviceInfo = [
    {name: '会员中心', icon: 'iconfont icon-icon_vip_fill', color: '#FF8C00'},
    {name: '手机充值', icon: 'iconfont icon-chongzhi', color: '#FF8C00'},
    {name: '客服中心', icon: 'iconfont icon-custom-service', color: '#48D1CC'},
    {name: '好友去哪', icon: 'iconfont icon-dingwei1', color: '#48D1CC'},
    {name: '免流用美团', icon: 'iconfont icon-sd-card', color: '#48D1CC'},
    {name: '发票助手', icon: 'iconfont icon-fapiaoguanli', color: '#48D1CC'},
    {name: '我要合作', icon: 'iconfont icon-lianjie-tianchong', color: '#48D1CC'},
    {name: '关于美团', icon: 'iconfont icon-guanyuwomen', color: '#48D1CC'}
  ]

  export default {
    data() {
      return {
        walletInfo: walletInfo,
        headInfo: headInfo,
        serviceInfo: serviceInfo
      }
    },
    components: {CommonFoot}
  }
</script>

<style scoped>
  .user-wrapper {
    height: 100%;
    box-sizing: border-box;
    padding-top: 500px;
  }
  .user-top {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    height: 100px;
    background-color: rgba(56, 142, 142, 0.3);
    z-index: 2;
  }
  .user-top i {
    font-size: 50px;
    color: #fff;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
  }
  .icon0 {
    left: 40px;
  }
  .icon1 {
    right: 150px;
  }
  .icon2 {
    right: 40px;
  }
  .user-head {
    position: relative;
    margin: -500px 0 0;
  }
  .user-profile {
    position: absolute;
    left: 296px;
    top: 130px;
    z-index: 1;
    text-align: center;
    font-size: 34px;
    letter-spacing: 0.03em;
    font-weight: bold;
  }
  .user-img {
    width: 100px;
    height: 100px;
    margin: auto;
    border-radius: 50px;
    background: url('../assets/t1.png');
    background-size: contain;
  }
  .user-head-top{
    height: 240px;
    background: #388E8E;
  }
  .user-head-bottom {
    height: 300px;
    border-top-left-radius: 50% 40px;
    border-top-right-radius: 50% 40px;
    position: relative;
    bottom: 40px;
    background: #fff;
  }
  .user-head-info {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 200px;
    display: flex;
  }
  .head-item {
    width: 33%;
    position: relative;
    text-align: center;
  }
  .head-item i {
    display: block;
    font-size: 50px;
    padding: 10% 0 10px 0;
  }
  .head-item span {
    font-size: 28px;
    color: black;
  }
  .user-body {
    height: 100%;
    position: relative;
    top: -40px;
    padding: 0 30px;
  }
  .wallet, .service {
    height: 50%;
    border-top: 1px solid #ccc;
    position: relative;
  }
  .wallet p, .service p {
    margin: 30px 0;
    font-size: 28px;
    font-weight: bold;
  }
  .wallet-main, .service-main {
    display: flex;
    flex-wrap: wrap;
    position: absolute;
    left: 0;
    right: 0;
    top: 88px;
    bottom: 0;
  }
  .wallet-item, .service-item {
    width: 25%;
    position: relative;
    text-align: center;
    color: #FF8C00;
  }
  .wallet-item i, .service-item i {
    display: block;
    font-size: 50px;
    padding: 10% 0 10px 0;
  }
  .wallet-item span, .service-item span {
    font-size: 28px;
    color: black;
  }
  .blank {
    height: 100px;
  }
</style>
