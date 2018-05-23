<template>
  <div>
    <div v-if="true" class="login-wrapper">
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
            <input type="text" v-model="username" placeholder="请输入美团账号" />
            <input type="password" v-model="password" placeholder="请输入密码" />
            <i class="iconfont icon-close-eye eyes"></i>
            <button @click="accountLogin" :disabled="loginActive">登录</button>
            <span>忘记密码</span>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="register-wrapper">
      <my-head text="注册"></my-head>
      <div class="register-step-head">
        <div class="register-step" v-for="item in registerStep">
          <span :class="{'step-active': item.index === stepActive}">{{item.text}}</span>
          <i class="iconfont icon-right"></i>
        </div>
      </div>
      <div class="register-step-main" v-if="stepActive === 0">
        <div>
          <input type="text" placeholder="请输入您的手机号码" class="input-text" autofocus v-model="mobile">
        </div>
        <div class="register-statement">
            <input type="radio" :checked="isAgree" @change="agree">
            <span>我已审慎阅读并同意<a>《美团网用户协议》</a>、<a>《法律声明》</a>、<a>《隐私政策》</a>，
            接受免除或限制责任、诉讼管辖约定等粗体提示条款</span>
        </div>
        <div class="btn-affirm">
          <button :disabled="!btnEnable" :class="{'enabled-btn': btnEnable}" @click="step1To2">同意并注册</button>
        </div>
      </div>
      <div class="register-step-main" v-if="stepActive === 1">
        <div class="verify-tip">
          <span>验证码短信已经发送至{{encryptMobile}}</span>
        </div>
        <div class="input-verify">
          <input type="text" placeholder="请输入短信中的验证码" class="input-text" autofocus v-model="verifyCode">
        </div>
        <div class="btn-affirm">
          <button class="enabled-btn" @click="step2To3">提交验证码</button>
        </div>
      </div>
      <div class="register-step-main" v-if="stepActive === 2">
        <div class="input-password">
          <input type="password" placeholder="密码" class="input-text" autofocus v-model="registerPassword">
        </div>
        <div class="input-password">
          <input type="password" placeholder="确认密码" class="input-text" v-model="verifyPassword">
        </div>
        <div class="btn-affirm password-btn">
          <button class="enabled-btn" @click="register">确认并提交密码</button>
        </div>
      </div>
    </div>

    <dialog-box :dialog-text="dialogText" v-if="isDialog" @closeDialog="isDialog = false"></dialog-box>
  </div>
</template>

<script>
  import {setCookie, getCookie} from '../assets/js/cookie'
  import {mapMutations} from 'vuex'

  import MyHead from '../components/commons/Head'
  import DialogBox from '../components/commons/DialogBox'

  const _ = require('lodash');

  let otherLoginMethods = [
    {name: '微博', icon:'iconfont icon-weibo', color: 'red'},
    {name: 'QQ', icon:'iconfont icon-qq', color: 'blue'},
    {name: '账号密码', icon:'iconfont icon-lock', color: '#388E8E'}
  ];

  let registerStep = [
    {text: '1.输入手机号', index: 0},
    {text: '2.输入验证码', index: 1},
    {text: '3.设置密码', index: 2}
  ];

  export default {
    data() {
      return {
        username: '',
        password: '',
        otherLoginMethods: otherLoginMethods,
        isOther: false,  // 其他登录方式框
        isAccount: false,  // 账号密码登录窗口
        registerStep: registerStep,  // 注册步骤信息
        stepActive: 0,
        isAgree: false,  // 是否同意注册条款
        btnEnable: false,  // 按钮是否可操作
        mobile: '',  // 手机号
        verifyCode: '',  // 验证码
        registerPassword: '',  // 注册密码
        verifyPassword: '',  // 确认密码
        isDialog: false,  // 是否显示提示框
        dialogText: '',
      }
    },
    computed: {
      loginActive() {
        return !(this.username !== '' && this.password !== '');
      },
      encryptMobile() {
        return this.mobile.substring(0, 3) + '****' + this.mobile.substring(5);
      }
    },
    components: {MyHead, DialogBox},
    watch: {
      mobile() {
        this.checkNextStep();
      }
    },
    methods: {
      cancel() {
        window.history.back();
      },
      selectOtherLogin() {
        this.isOther = true;
      },
      toOtherLogin(way) {
        if (way === '账号密码') {
          this.isOther = false;
          this.isAccount = true;
        }
      },
      accountLogin() {
        let _this = this;
        this.$http.post('http://localhost:7766/api/login', {
          name: this.username,
          password: this.password
        })
          .then(function (response) {
            console.log(response);
            let result = response.data;
            if(result.success) {
              setCookie('token', result.token, 1000*60*60);
              _this.setUsername(_this.username);
              _this.isAccount = false;
              _this.$router.push('/user');
            }
          })
          .catch(function (error) {
            console.log('error: ', error);
          });
      },
      agree() {
        this.isAgree = true;
        this.checkNextStep();
      },
      checkNextStep: _.debounce(function () {
        if (!this.isAgree) {
          return;
        }
        let mobileNum = this.mobile;
        let checkMobile = new RegExp('^1\\d{10}$');
        if (checkMobile.test(mobileNum)) {
          this.btnEnable = true;
        } else {
          this.btnEnable = false;
        }
      }),
      step1To2() {
        this.stepActive = 1;
      },
      step2To3() {
        if (this.verifyCode === '') {
          this.isDialog = true;
          this.dialogText = '验证码输入有误，请重新输入';
          return;
        }
        this.stepActive = 2;
      },
      register() {
        if (this.registerPassword !== this.verifyPassword) {
          this.isDialog = true;
          this.dialogText = '验证码输入有误，请重新输入';
          return;
        }

        let params = {
          username: this.mobile,
          mobile: this.mobile,
          email: '',
          password: this.verifyPassword
        };
        let _this = this;

        this.$http.post('http://localhost:7766/api/register', params)
          .then(function (response) {
          let result = response.data;
          _this.dialogText = result.message;
          _this.isDialog = true;
          if (result.status) {
            setTimeout(function() {
              _this.isDialog = false;
              window.history.back();
            }.bind(_this), 1000)
          }
        }).catch(function (error) {
          console.log('error: ', error);
        });
      },
      ...mapMutations({
        setUsername: 'SET_USERNAME',
      })
    },
    mounted() {
    //   let token = getCookie('token');
    //   if (token) {
    //     this.$http.post('http://localhost:7766/api/isLogin', {
    //     token: token
    //   })
    //     .then(function (response) {
    //       console.log(response);
    //     })
    //     .catch(function (error) {
    //       console.log('error: ', error);
    //     });
    //   }
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
    width: 750px;
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
  .eyes {
    position: absolute;
    top: 110px;
    right: 80px;
    font-size: 44px;
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
    background: #388E8E;
    border-radius: 8px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
    color: #eee;
  }
  .login-body-account button:disabled {
    background: #ddd;
    color: #bbb;
    cursor: default;
  }
  .login-body-account span {
    padding: 30px 10px 0 0;
    color: #388E8E;
    text-align: right;
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
    display: inline-block;
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
  .register-wrapper {
    background: #eee;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
  .register-step-head {
    background: #fff;
    position: relative;
    top: 112px;
    display: flex;
    height: 80px;
    align-items: center;
    border-bottom: 1px solid #ddd;
  }
  .register-step {
    flex: 1;
    width: 250px;
    font-size: 26px;
    color: #666;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    padding: 0 10px 0 20px;
  }
  .register-step i {
    font-size: 24px;
  }
  .step-active {
    color: #3CB371;
  }
  .register-step-main {
    position: relative;
    top: 132px;
    display: flex;
    flex-direction: column;
  }
  .input-text {
    background-color: #fff;
    border: none;
    height: 70px;
    width: 100%;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    box-sizing: border-box;
    padding-left: 30px;
  }
  .register-statement {
    display: flex;
    font-size: 26px;
    margin: 20px 10px 36px 10px;
    color: #666;
  }
  .register-statement a {
    text-decoration: underline;
    color: #3CB371;
  }
  .btn-affirm {
    text-align: center;
  }
  .btn-affirm button {
    width: 700px;
    height: 70px;
    text-align: center;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    border-radius: 8px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
    color: #fff;
    background: rgba(60, 179, 113, 0.7);
  }
  .enabled-btn {
    background: #3CB371 !important;
  }
  .verify-tip {
    height: 40px;
    line-height: 40px;
    font-size: 24px;
    box-sizing: border-box;
    color: #666;
    text-align: center;
  }
  .input-verify {
    margin: 20px 0;
  }
  .input-password {
    margin: 10px 0;
  }
  .password-btn {
    margin-top: 24px;
  }
</style>
