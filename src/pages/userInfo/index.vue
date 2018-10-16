<template>
  <div class="wrapper">
    <my-head text="个人信息"></my-head>
    <div class="main">
      <div class="item-head">
        <div class="item-left">
          <span>头像</span>
        </div>
        <div class="item-right">
          <div class="head-wrapper">
          </div>
          <i class="iconfont icon-left rotate"></i>
        </div>
      </div>
      <item v-for="(item,index) in userInfo" :key="index" :name="item.name" :brief="item.info">
      </item>
    </div>
  </div>
</template>

<script>
  import MyHead from '../../components/commons/Head'
  import Item from '../../components/commons/Item'

  let userInfo = [
    {name: '昵称', info: 'tymzyx'},
    {name: '生日', info: ''},
    {name: '收货地址', info: '修改/添加'},
  ]

  export default {
    data() {
      return {
        userInfo: userInfo
      }
    },
    components: {MyHead, Item}
  }
</script>

<style scoped>
  .wrapper {
    background-color: #eee;
    height: 100%;
  }
  .main {
    position: absolute;
    top: 130px;
    box-sizing: border-box;
    padding-left: 20px;
    background: #fff;
  }
  .item-head {
    display: flex;
    height: 106px;
    width: 730px;
    background: #fff;
    line-height: 110px;
    border-bottom: 1px solid #eee;
    position: relative;
  }
  .item-left {
    width: 50%;
    text-align: left;
    font-size: 28px;
  }
  .item-right {
    width: 50%;
    text-align: right;
    box-sizing: border-box;
    padding-right: 20px;
    color: #888;
  }
  .item-right span {
    font-size: 20px;
  }
  .item-right i {
    font-size: 20px;
  }
  .rotate:before {
    display: inline-block;
    transform: rotate(180deg);
  }
  .head-wrapper {
    position: absolute;
    width: 80px;
    height: 80px;
    background: aqua;
    border-radius: 40px;
    top: 50%;
    right: 70px;
    transform: translateY(-50%);
  }
</style>
