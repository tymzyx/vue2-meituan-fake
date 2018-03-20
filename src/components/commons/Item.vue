<!--item for user info-->
<template>
  <div class="item">
    <div class="item-left">
      <span>{{name}}</span>
    </div>
    <div class="item-right">
      <span>{{brief}}</span>
      <i class="iconfont icon-left rotate"></i>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['name', 'brief']
  }
</script>

<style scoped>
  .item {
    display: flex;
    height: 80px;
    width: 730px;
    background: #fff;
    line-height: 80px;
    border-bottom: 1px solid #eee;
  }
  .item div {
    width: 50%;
  }
  .item-left {
    text-align: left;
    font-size: 28px;
  }
  .item-right {
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
</style>
