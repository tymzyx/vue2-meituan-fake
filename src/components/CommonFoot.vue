<template>
  <div class="foot-wrapper">
    <div v-for="item in footList" @click="changePage(item.url, item.key)">
      <i :class="[item.icon, {isActive: item.key===activeKey}]"></i>
      <span :class="{isActive: item.key===activeKey}">{{item.name}}</span>
    </div>
  </div>
</template>

<script>
  let footList = [
    {key: '0', name: '首页', icon: 'iconfont icon-home', url: '/'},
    {key: '1', name: '附近', icon: 'iconfont icon-Location', url: '/'},
    {key: '2', name: '发现', icon: 'iconfont icon-find', url: '/'},
    {key: '3', name: '订单', icon: 'iconfont icon-note', url: '/'},
    {key: '4', name: '我的', icon: 'iconfont icon-peoplefill', url: '/user'}
  ]

  export default {
    data() {
      return {
        footList: footList
      }
    },
    props: ['activeKey'],
    methods: {
      changePage(url, key) {
        this.activeKey = key;
        this.$router.push(url);
      }
    }
  }
</script>

<style lang="css" scoped>
  .foot-wrapper {
    display: flex;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100px;
    z-index: 1;
    background: #fff;
    border-top: 1px solid #ccc;
  }
  .foot-wrapper div {
    flex: 1;
    height: 100%;
    position: relative;
    color: #666;
  }
  .foot-wrapper i {
    font-size: 40px;
    position: absolute;
    top: 36%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .foot-wrapper span {
    font-size: 26px;
    text-align: center;
    position: absolute;
    top: 72%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .isActive {
    color: 	#3CB371;
  }
</style>
