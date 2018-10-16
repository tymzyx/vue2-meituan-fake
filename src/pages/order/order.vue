<template>
  <div class="wrapper">
    <div class="head-wrapper">
      <span>订单</span>
    </div>
    <div class="body-wrapper">

      <div class="not-login" v-if="false">
        <div class="not-login-img"></div>
        <div class="not-login-text">
          <span>登录后可查看订单、收藏记录</span>
          <button @click="$router.push('/login')">登录</button>
        </div>
      </div>

      <div class="login-wrapper" v-if="true">
        <div class="my-order">
          <div class="module-head">
            <div class="module-head-left">我的订单</div>
            <div class="module-head-right">
              <span>全部订单</span>
              <i class="iconfont icon-right"></i>
            </div>
          </div>
          <div class="my-order-actions">
            <div v-for="item in orderAction" class="my-order-action">
              <div>
                <i :class=item.icon :style="{color: item.color}"></i>
                <span>{{item.text}}</span>
              </div>
            </div>
          </div>
          <div class="recently-order">
            <div class="recently-order-head">
              最近订单
            </div>
            <div>
              <order-item v-for="i in 3" :key="i"></order-item>
            </div>
            <div class="recently-order-prompt">
              <span>查看全部</span>
              <i class="iconfont icon-right"></i>
            </div>
          </div>
        </div>
        <div class="gap"></div>
        <div class="my-collection">
          <div class="module-head">
            <div class="module-head-left">我的收藏</div>
          </div>
          <div class="my-collection-main">
          </div>
        </div>
        <div class="gap"></div>
        <div class="my-browse">
          <div class="module-head">
            <div class="module-head-left">最近浏览</div>
          </div>
          <div class="my-browse-main">
          </div>
        </div>
        <div class="blank"></div>
      </div>

    </div>
    <common-foot activeKey="3"></common-foot>
  </div>
</template>

<script>
  import CommonFoot from '../../components/CommonFoot'
  import OrderItem from '../../components/commons/OrderItem'

  let orderAction = [
    {icon: 'iconfont icon-card', text: '待付款', color: '#87CEFF'},
    {icon: 'iconfont icon-ticket-confirmation', text: '待使用', color: '#EEA9B8'},
    {icon: 'iconfont icon-zixundianji', text: '待评价', color: '#EEC900'},
    {icon: 'iconfont icon-paycircle', text: '退款/售后', color: '#CD96CD'}
  ];

  export default {
    data() {
      return {
        orderAction: orderAction
      }
    },
    components: {CommonFoot, OrderItem}
  }
</script>

<style scoped>
  .wrapper {
    background: #eee;
  }
  .head-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 90px;
    line-height: 90px;
    border-bottom: 1px solid #ccc;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    background: #f5f5f5;
    z-index: 100;
  }
  .body-wrapper {
    position: relative;
    top: 90px;
    background: #fff;
  }
  .not-login {
    position: absolute;
    left: 0;
    right: 0;
    top: 250px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .not-login-img {
    width: 200px;
    height: 200px;
    border-radius: 100px;
    background: #4caf50;
  }
  .not-login-text {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    align-items: center;
  }
  .not-login-text span {
    font-size: 28px;
    color: #666;
  }
  .not-login-text button {
    width: 220px;
    height: 80px;
    text-align: center;
    background: #388E8E;
    border: 1px solid #dcdfe6;
    border-radius: 6px;
    padding: 6px 13px;
    font-size: 32px;
    outline: none;
    color: #fff;
    margin-top: 10px;
  }
  .module-head {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ddd;
    height: 80px;
    line-height: 80px;
  }
  .module-head-left {
    padding-left: 30px;
    font-weight: bold;
    font-size: 30px;
  }
  .module-head-right {
    padding-right: 20px;
  }
  .module-head-right span, .module-head-right i {
    font-size: 26px;
    color: #aaa;
  }
  .my-order-actions {
    display: flex;
  }
  .my-order-action {
    width: 25%;
    height: 160px;
    display: flex;
    align-items: center;
  }
  .my-order-action div {
    text-align: center;
    flex: 1;
  }
  .my-order-action i {
    display: block;
    font-size: 50px;
  }
  .my-order-action span {
    font-size: 26px;
    color: #444;
  }
  .recently-order-head {
    background: #eee;
    height: 50px;
    line-height: 50px;
    font-size: 24px;
    color: #888;
    padding-left: 20px;
  }
  .recently-order-prompt {
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: #388E8E;
  }
  .recently-order-prompt span {
    font-size: 28px;
  }
  .recently-order-prompt i {
    font-size: 24px;
  }
  .gap {
    height: 20px;
    background: #eee;
  }
  .my-collection-main, .my-browse-main {
    height: 400px;
  }
  .blank {
    height: 100px;
  }
</style>
