<template>
  <div class="wrapper">
    <my-head text="设置"></my-head>
    <div class="main-top">
      <item v-for="item in editInfo" :brief="item.info" :name="item.name"></item>
    </div>
    <div class="main-bottom">
      <item v-for="item in baseInfo" :brief="item.info" :name="item.name"></item>
    </div>
    <button @click="logout">退出账号</button>
  </div>
</template>

<script>
  import MyHead from '../../components/commons/Head'
  import Item from '../../components/commons/Item'
  import {delCookie} from '../../assets/js/cookie'
  import {mapMutations} from 'vuex'

  let editInfo = [
    {name: '个人信息', info: ''},
    {name: '换绑手机', info: '186****0703'},
    {name: '社交账号绑定', info: '绑定/解绑'},
    {name: '登录密码', info: '修改'},
    {name: '支付设置', info: ''}
  ]

  let baseInfo = [
    {name: '安全中心', info: ''},
    {name: '通用', info: ''},
    {name: '关于美团', info: ''}
  ]

  export default {
    data() {
      return {
        baseInfo: baseInfo,
        editInfo: editInfo
      }
    },
    components: {MyHead, Item},
    methods: {
      logout() {
        this.setUsername('');
        delCookie('token');
        this.$router.push('/user');
      },
      ...mapMutations({
        setUsername: 'SET_USERNAME',
      })
    }
  }
</script>

<style scoped>
  .wrapper {
    background-color: #eee;
    height: 100%;
  }
  .main-top {
    position: absolute;
    top: 130px;
    box-sizing: border-box;
    padding-left: 20px;
    background: #fff;
  }
  .main-bottom {
    position: absolute;
    top: 555px;
    box-sizing: border-box;
    padding-left: 20px;
    background: #fff;
  }
  .wrapper button {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 830px;
    width: 680px;
    height: 76px;
    text-align: center;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    background: #fff;
    border-radius: 8px;
    padding: 6px 13px;
    font-size: 28px;
    outline: none;
    color: #111;
  }
</style>
