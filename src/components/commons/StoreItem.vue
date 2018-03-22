<template>
  <div class="item-wrapper">
    <div class="item-top">
      <div class="item-top-left"></div>
      <div class="item-top-right">
        <div class="item-top-right-name">
          <h4>{{itemInfo.name}}</h4>
        </div>
        <div class="item-top-right-rate">
          <rate :count="itemInfo.rank"></rate>
        </div>
        <div class="item-top-right-location">
          <span>素食|海淀区</span>
          <div class="location-distance">54m</div>
        </div>
        <div class="item-top-right-sales">
          <i class="iconfont icon-dianzan"></i>
          <p>{{itemInfo.comment_info['好评']}}人消费</p>
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
</template>

<script>
  import Rate from './rate'

  export default {
    props: ['itemInfo'],
    components: {Rate}
  }
</script>

<style scoped>
  .item-top {
    height: 260px;
    display: flex;
  }
  .item-top-left {
    box-sizing: border-box;
    width: 260px;
    background: url("../../assets/mdl.jpg") no-repeat;
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
</style>
