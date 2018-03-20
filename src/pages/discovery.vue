<template>
  <div>
    <div class="head-wrapper">
      <span>发现</span>
    </div>
    <div class="body-wrapper">
      <Navbar v-model="selected">
        <tab-item id="0">精选</tab-item>
        <tab-item id="1">关注</tab-item>
        <tab-item id="2">爱美食</tab-item>
        <tab-item id="3">出去浪</tab-item>
        <tab-item id="4">生活控</tab-item>
      </Navbar>
      <tab-container v-model="selected">
        <tab-container-item id="0">
          <span>i am 0</span>
        </tab-container-item>
        <tab-container-item id="1">
          <span>i am 1</span>
        </tab-container-item>
        <tab-container-item id="2">
          <span>i am 2</span>
        </tab-container-item>
        <tab-container-item id="3">
          <span>i am 3</span>
        </tab-container-item>
        <tab-container-item id="4">
          <span>i am 4</span>
        </tab-container-item>
      </tab-container>
    </div>
    <common-foot activeKey="2"></common-foot>
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
        selected: '0'
      }
    },
    components: {CommonFoot, Navbar, TabItem, TabContainer, TabContainerItem}
  }
</script>

<style lang="css" scoped>
  .head-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 90px;
    line-height: 90px;
    border-bottom: 1px solid #ccc;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    background: #f5f5f5;
  }
  .body-wrapper {
    position: relative;
    top: 90px;
  }
</style>
