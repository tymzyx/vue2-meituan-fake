<template>
  <div class="wrapper">
    <i v-for="i,index in 5" class="iconfont icon-star1" :class="{'rating': index+1 <= count}"></i>
  </div>
</template>

<script>
  export default {
    props: ['count']
  }
</script>

<style scoped>
  .wrapper i {
    margin-right: 8px;
    color: #ccc;
  }
  .rating {
    color: gold !important;
  }
</style>
