<template>
  <div class="item-wrapper">
    <div class="item-wrapper-left"></div>
    <div class="item-wrapper-right">
      <div class="item-first">
        <h4>测试测试</h4>
        <span>已完成</span>
      </div>
      <div class="item-second">
        <span>下单时间：2017-12-13 12:32:12</span>
      </div>
      <div class="item-third">
        <span>总价：162元</span>
        <div class="item-action">再来一单</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
  }
</script>

<style scoped>
  .item-wrapper {
    display: flex;
    height: 200px;
    border-bottom: 1px solid #ddd;
  }
  .item-wrapper-left {
    width: 140px;
    background: url("../../assets/mdl.jpg") no-repeat;
    background-size: 100px;
    background-position: center center;
  }
  .item-wrapper-right {
    display: flex;
    flex: 1;
    flex-direction: column;
    box-sizing: border-box;
    margin: 20px 30px 0 30px;
    padding: 0 0 30px 0;
  }
  .item-first, .item-third {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .item-first h4 {
    display: inline-block;
    margin: 16px 0;
    font-size: 30px;
  }
  .item-first span {
    color: #388E8E;
    font-size: 26px;
  }
  .item-second {
    font-size: 26px;
    color: #aaa;
  }
  .item-third span {
    font-size: 26px;
    color: #aaa;
  }
  .item-action {
    display: inline-block;
    margin: 4px 0;
    padding: 6px;
    border: 1px solid orange;
    color: orange;
    font-size: 26px;
  }
</style>
