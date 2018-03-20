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
          <tab-item id="0">享美食</tab-item>
          <tab-item id="1">住酒店</tab-item>
          <tab-item id="2">爱玩乐</tab-item>
          <tab-item id="3">全部</tab-item>
        </Navbar>
        <tab-container v-model="selected">
          <tab-container-item id="0">
            <div class="category-wrapper">
              <div v-for="i,index in 8">
                <button :class="{'selected-btn': index === 0}" >测试</button>
              </div>
            </div>
            <div class="item-wrapper" v-for="i in 4">
              <div class="item-top">
                <div class="item-top-left"></div>
                <div class="item-top-right">
                  <div class="item-top-right-name">
                    <h4>素虎净素餐厅（上地店）</h4>
                  </div>
                  <div class="item-top-right-rate">
                    <rate count="4.5"></rate>
                  </div>
                  <div class="item-top-right-location">
                    <span>素食|海淀区</span>
                    <div class="location-distance">54m</div>
                  </div>
                  <div class="item-top-right-sales">
                    <i class="iconfont icon-dianzan"></i>
                    <p>174人消费</p>
                  </div>
                </div>
              </div>
              <div class="item-bottom">
                <div class="item-bottom-item">
                  <i class="iconfont icon-icon-test"></i>
                  <span>双人餐176元，4人餐296元起</span>
                </div>
              </div>
              <div class="item-gap"></div>
            </div>
            <div class="tab-bottom"></div>
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
  import Rate from '../components/commons/rate'

  export default {
    data() {
      return {
        selected: '0',
        isLocation: false,
      }
    },
    components: {CommonFoot, Navbar, TabItem, TabContainer, TabContainerItem, Rate},
    methods: {
      toSearch() {
        this.$router.push('searchMain');
      }
    },
    mounted() {
      this.$http.post('http://localhost:7766/api/store/findNearby', {
        })
        .then(function (response) {
          console.log('response: ', response);
        })
        .catch(function (error) {
          console.log('error: ', error);
        });
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
    background: #fff;
    z-index: 100;
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
    font-size: 28px;
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
  .item-top {
    height: 260px;
    display: flex;
  }
  .item-top-left {
    box-sizing: border-box;
    width: 260px;
    background: url("../assets/mdl.jpg") no-repeat;
    background-size: 210px;
    background-position: center center;
  }
  .item-top-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    margin: 25px 10px 0 30px;
    border-bottom: 1px solid #ddd;
  }
  .item-top-right-name, .item-top-right-rate {
    margin-bottom: 6px;
  }
  .item-top-right h4 {
    margin: 0;
  }
  .item-top-right-location {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 26px;
    color: #666;
  }
  .location-distance {
    height: 40px;
    line-height: 40px;
    border-radius: 4px;
    background: #ddd;
    font-size: 26px;
    color: #888;
    box-sizing: border-box;
    padding: 0 8px;
  }
  .item-top-right-sales {
    flex: 1;
    display: flex;
    align-items: center;
  }
  .item-top-right-sales i {
    color: gold;
    font-size: 28px;
  }
  .item-top-right-sales p {
    margin: 0;
    display: inline-block;
    font-size: 26px;
  }
  .item-bottom {
    box-sizing: border-box;
    padding-left: 290px;
    margin: 8px 0;
  }
  .item-bottom-item {
    padding: 4px 0;
  }
  .item-bottom-item i {
    font-size: 28px;
    color: #388E8E;
  }
  .item-bottom-item span {
    font-size: 26px;
    color: #666;
  }
  .item-gap {
    background: #eee;
    height: 24px;
  }
  .tab-bottom {
    height: 76px;
  }
</style>
