<template>
  <div>
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
        <a>使用其他方式登录</a>
      </div>
    </div>
    <div class="login-foot">
      <span>登录代表你已同意<a>《美团网用户协议》</a></span>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
      cancel() {
        this.$router.push('/user')
      }
    }
  }
</script>

<style scoped>
  .login-head {
    height: 112px;
    border-bottom: 1px solid #bbb;
    display: flex;
    background: #eee;
    position: relative;
    line-height: 112px;
    padding: 0 20px;
    text-align: center;
    justify-content: space-between;
  }
  .login-head i, .login-head span {
    width: 100px;
    color: #3CB371;
  }
  .login-head h3 {
    width: 200px;
    margin: 0;
    font-size: 36px;
    letter-spacing: 0.05em;
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
</style>
