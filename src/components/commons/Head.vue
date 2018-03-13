<template>
  <div class="head">
    <div class="head-left">
      <i class="iconfont icon-left" @click="goBack"></i>
    </div>
    <div class="head-middle">
      <h4>{{text}}</h4>
    </div>
    <div class="head-right">
      <span></span>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['text'],
    methods: {
      goBack() {
        window.history.back();
      }
    }
  }
</script>

<style scoped>
  .head {
    height: 112px;
    border-bottom: 1px solid #ddd;
    display: flex;
    width: 750px;
    line-height: 112px;
    justify-content: space-between;
    position: absolute;
    top: 0;
    background: #fff;
  }
  .head div {
    width: 250px;
    box-sizing: border-box;
  }
  .head-left {
    text-align: left;
    padding-left: 20px;
  }
  .head-left i {
    font-size: 40px;
    color: #3CB371;
  }
  .head-middle {
    text-align: center;
  }
  .head-middle h4 {
    margin: 0;
  }
</style>
