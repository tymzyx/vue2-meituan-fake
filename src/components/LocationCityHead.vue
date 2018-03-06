<template>
  <div class="lc-head">
    <i class="fa fa-close close-icon" @click="returnHome"></i>
    <i class="fa fa-search search-icon" @click="toSearch"></i>
    <input class="search" type="text" placeholder="城市名/拼音" @click="toSearch">
  </div>
</template>

<script scoped>
  export default {
    methods: {
      returnHome() {
        this.$router.push('/')
      },
      toSearch() {
        this.$router.push('/searchCity')
      }
    }
  }
</script>

<style scoped>
  .lc-head {
    width: 750px;
    height: 80px;
    padding-top: 10px;
    line-height: 80px;
  }
  .close-icon {
    margin-left: 20px;
    font-size: 40px;
  }
  .search-icon {
    position: relative;
    left: 110px;
    z-index: 1;
  }
  .search {
    position: relative;
    left: 56px;
    background-color: #eeeeee;
    border: none;
    border-radius: 27px;
    height: 54px;
    padding-left: 54px;
    width: 380px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }
</style>
