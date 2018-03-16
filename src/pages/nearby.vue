<template>
  <div>
    <div class="head-wrapper">
      <div class="head-left">
        <i class="iconfont icon-location"></i>
        <span>测试测试测试测试测试</span>
        <i class="iconfont icon-bottom"></i>
      </div>
      <div class="head-right">
        <i class="iconfont icon-search search-icon"></i>
        <input type="text" placeholder="找附近的吃喝玩乐">
      </div>
    </div>
    <div class="body-wrapper">
      <Navbar v-model="selected">
        <tab-item id="0">第一个aa</tab-item>
        <tab-item id="1">第二个bb</tab-item>
        <tab-item id="2">第三个cc</tab-item>
      </Navbar>
    </div>
    <common-foot activeKey="1"></common-foot>
  </div>
</template>

<script>
  import CommonFoot from '../components/CommonFoot'
  import Navbar from '../components/commons/tab/Navbar'
  import TabItem from '../components/commons/tab/TabItem'

  export default {
    data() {
      return {
        selected: '0'
      }
    },
    components: {CommonFoot, Navbar, TabItem}
  }
</script>

<style>
  .head-wrapper {
    display: flex;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 90px;
    border-bottom: 1px solid #ccc;
  }
  .head-left {
    width: 40%;
    line-height: 90px;
    display: flex;
    justify-content: center;
  }
  .head-left span {
    width: 160px;
    margin: 0 0 0 10px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    -o-text-overflow: ellipsis;
    display: inline-block;
  }
  .head-left i {
    font-size: 36px;
  }
  .head-right {
    width: 60%;
    line-height: 90px;
    position: relative;
  }
  .head-right i {
    position: absolute;
    left: 48px;
    top: 2px;
  }
  .head-right input {
    font-size: 28px;
    background-color: #eeeeee;
    border: none;
    border-radius: 27px;
    height: 54px;
    width: 400px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }
  .head-right input::-ms-input-placeholder{text-align: center;}
  .head-right input::-webkit-input-placeholder{text-align: center;}
  .body-wrapper {
    position: relative;
    top: 90px;
  }
</style>
