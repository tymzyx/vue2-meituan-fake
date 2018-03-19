<template>
  <div>
    <div class="head-wrapper">
      <span>订单</span>
    </div>
    <div class="body-wrapper">

      <div class="not-login" v-if="true">
        <div class="not-login-img"></div>
        <div class="not-login-text">
          <span>登录后可查看订单、收藏记录</span>
          <button @click="$router.push('/login')">登录</button>
        </div>
      </div>
    </div>
    <common-foot activeKey="3"></common-foot>
  </div>
</template>

<script>
  import CommonFoot from '../../components/CommonFoot'

  export default {
    components: {CommonFoot}
  }
</script>

<style scoped>
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
  }
  .body-wrapper {
    position: relative;
    top: 90px;
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
</style>
