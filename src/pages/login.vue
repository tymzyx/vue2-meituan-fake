<template>
  <div>
    <div class="shade" v-show="isOther">
    </div>
    <div class="login-head">
      <i class="iconfont icon-close" @click="cancel"></i>
      <h3>登录美团</h3>
      <span>注册</span>
    </div>
    <div class="login-body">
      <div class="login-body-main">
        <p>推荐登录方式</p>
        <button class="weiChat"><i class="iconfont icon-weixin"></i> 微信登录</button>
        <p>或</p>
        <button class="phone">使用手机号登录注册</button>
        <a @click="selectOtherLogin">使用其他方式登录</a>
      </div>
    </div>
    <div class="login-foot">
      <span>登录代表你已同意<a>《美团网用户协议》</a></span>
    </div>
    <div class="other-login" v-show="isOther">
      <div class="other-login-main">
        <div v-for="item in otherLoginMethods" class="other-login-item" @click="toOtherLogin(item.name)">
          <i :class="item.icon" :style="{color: item.color}"></i>
          <span>{{item.name}}</span>
        </div>
      </div>
      <div class="other-login-cancel" @click="isOther = false;">取消</div>
    </div>

    <div class="login-account" v-show="isAccount">
      <div class="login-head-account">
        <i class="iconfont icon-left" @click="isAccount = false;"></i>
        <h3>登录美团</h3>
        <span></span>
      </div>
      <div class="login-body-account">
        <div>
          <input type="text" placeholder="请输入美团账号" />
          <input type="password" placeholder="请输入密码" />
          <button>登录</button>
          <span>忘记密码</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  let otherLoginMethods = [
    {name: '微博', icon:'iconfont icon-weibo', color: 'red'},
    {name: 'QQ', icon:'iconfont icon-qq', color: 'blue'},
    {name: '账号密码', icon:'iconfont icon-lock', color: '#388E8E'}
  ];

  export default {
    data() {
      return {
        otherLoginMethods: otherLoginMethods,
        isOther: false,
        isAccount: false
      }
    },
    methods: {
      cancel() {
        this.$router.push('/user');
      },
      selectOtherLogin() {
        this.isOther = true;
      },
      toOtherLogin(way) {
        if (way === '账号密码') {
          this.isOther = false;
          this.isAccount = true;
        }
      }
    }
  }
</script>

<style scoped>
  .login-head, .login-head-account {
    height: 112px;
    border-bottom: 1px solid #bbb;
    display: flex;
    background: #eee;
    position: absolute;
    left: 0;
    right: 0;
    line-height: 112px;
    padding: 0 20px;
    text-align: center;
    justify-content: space-between;
  }
  .login-head i, .login-head span {
    width: 100px;
    color: #3CB371;
  }
  .login-head h3, .login-head-account h3 {
    width: 200px;
    margin: 0;
    font-size: 36px;
    letter-spacing: 0.05em;
  }
  .login-head-account i, .login-head-account span {
    width: 80px;
    color: #3CB371;
    font-size: 40px;
  }
  .login-body-account {
    background-color: #fff;
    position: absolute;
    left: 0;
    right: 0;
    top: 112px;
    bottom: 0;
  }
  .login-body-account div {
    position: absolute;
    left: 0;
    right: 0;
    top: 100px;
    text-align: center;
    padding: 0 70px;
    display: flex;
    flex-direction: column;
  }
  .login-body-account input {
    display: block;
    background-color: #fff;
    border: none;
    border-bottom: 1px solid #bbb;
    height: 70px;
    width: 610px;
    font-size: 34px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    margin: 0 0 20px 0;
  }
  .login-body-account button {
    display: block;
    margin-top: 30px;
    width: 600px;
    height: 76px;
    text-align: center;
    cursor: pointer;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    border-radius: 8px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
    color: #999;
  }
  .login-body-account span {
    display: block;
    position: relative;
    left: 200px;
    top: 20px;
    color: #388E8E;
  }
  .login-account {
    z-index: 20;
  }
  .login-body {
    position: absolute;
    top: 112px;
    bottom: 80px;
    width: 100%;
  }
  .login-body-main {
    position: absolute;
    top: 38%;
    left: 50%;
    text-align: center;
    transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%);
    -moz-transform: translate(-50%,-50%);
    -o-transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
  }
  .login-body-main p {
    font-size: 28px;
    color: #aaa;
  }
  .login-body-main a {
    display: block;
    margin-top: 80px;
    font-size: 28px;
    color: #3CB371;
  }
  .login-body-main button {
    width: 600px;
    height: 90px;
    text-align: center;
    cursor: pointer;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    border-radius: 8px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
  }
  .weiChat {
    color: #fff;
    background: green;
    font-size: 40px;
    letter-spacing: 0.1em;
  }
  .phone {
    color: #888;
    background: white;
    font-size: 40px;
    letter-spacing: 0.06em;
  }
  .login-foot {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 80px;
    line-height: 80px;
    text-align: center;
    font-size: 26px;
  }
  .login-foot a {
    text-decoration: underline;
    color: #3CB371;
  }
  .other-login {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 260px;
    text-align: center;
    background: #fff;
    z-index: 10;
  }
  .other-login-main {
    display: flex;
    height: 180px;
    border-bottom: 1px solid #ddd;
  }
  .other-login-item {
    width: 33%;
  }
  .other-login-item i {
    display: block;
    font-size: 70px;
    padding: 10% 0 10px 0;
  }
  .other-login-item span {
    font-size: 26px;
    color: #444;
  }
  .other-login-cancel {
    line-height: 80px;
    color: #444;
  }
  .shade {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(10, 10, 10, 0.2);
    z-index: 5;
  }
</style>
