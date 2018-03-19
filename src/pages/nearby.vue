<template>
  <div>
    <div>
      <div class="head-wrapper">
        <div class="head-left" @click="isLocation=true">
          <i class="iconfont icon-location"></i>
          <span>测试测试测试测试测试</span>
          <i class="iconfont icon-bottom"></i>
        </div>
        <div class="head-right" @click="toSearch">
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
        <tab-container v-model="selected">
          <tab-container-item id="0">
            <div class="category-wrapper">
              <div v-for="i,index in 8">
                <button :class="{'selected-btn': index === 0}" >测试</button>
              </div>
            </div>
            <span>i am 0</span>
          </tab-container-item>
          <tab-container-item id="1">
            <span>i am 1</span>
          </tab-container-item>
          <tab-container-item id="2">
            <span>i am 2</span>
          </tab-container-item>
        </tab-container>
      </div>
      <common-foot activeKey="1"></common-foot>
    </div>

    <transition name="location-animation">
      <div class="location-wrapper" v-if="isLocation">
        <div class="location-head">
          <div class="location-head-top">
            <i class="iconfont icon-close" @click="isLocation=false"></i>
            <span>切换地址</span>
          </div>
          <div class="location-head-bottom">
            <i class="iconfont icon-search"></i>
            <input type="text" placeholder="请输入地址"/>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
  import CommonFoot from '../components/CommonFoot'
  import Navbar from '../components/commons/tab/Navbar'
  import TabItem from '../components/commons/tab/TabItem'
  import TabContainer from '../components/commons/tab/TabContainer'
  import TabContainerItem from '../components/commons/tab/TabContainerItem'

  export default {
    data() {
      return {
        selected: '0',
        isLocation: false,
      }
    },
    components: {CommonFoot, Navbar, TabItem, TabContainer, TabContainerItem},
    methods: {
      toSearch() {
        this.$router.push('searchMain')
      }
    }
  }
</script>

<style scoped>
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
  .category-wrapper {
    display: flex;
    background: #eee;
    height: 180px;
    flex-wrap: wrap;
  }
  .category-wrapper div {
    width: 25%;
    height: 50%;
    text-align: center;
  }
  .category-wrapper button {
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    width: 150px;
    height: 65px;
    text-align: center;
    background: white;
    border: 1px solid #dcdfe6;
    border-radius: 35px;
    padding: 6px 13px;
    font-size: 28px;
    outline: none;
    color: #999;
  }
  .selected-btn {
    color: #fff !important;
    background: #FF7256 !important;
  }
  .location-wrapper {
    z-index: 10;
    background: #eee;
    position: fixed;
    width: 100%;
    top: 0;
    bottom: 0;
  }
  .location-head {
    height: 200px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    background: #fff;
    display: flex;
    flex-direction: column;
  }
  .location-head-top {
    text-align: center;
    height: 100px;
    line-height: 120px;
  }
  .location-head-top i {
    position: absolute;
    left: 30px;
    font-size: 36px;
    color: #388E8E;
  }
  .location-head-top span {
    font-size: 34px;
    letter-spacing: 0.04em;
  }
  .location-head-bottom {
    height: 100px;
    line-height: 100px;
    text-align: center;
  }
  .location-head-bottom i {
    position: absolute;
    left: 36px;
  }
  .location-head-bottom input {
    font-size: 28px;
    background-color: #eeeeee;
    border: none;
    border-radius: 18px;
    height: 60px;
    width: 650px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    padding-left: 50px;
  }
  .location-animation-enter-active, .location-animation-leave-active {
    transition: all .4s;
  }
  .location-animation-enter, .location-animation-leave-to {
    transform: translateY(100%);
  }
</style>
