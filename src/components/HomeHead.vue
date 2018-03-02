<template>
  <div class="homeHead">
    <div class="homeContainer">
      <i class="fa fa-sun-o weather-icon"></i>
      <p class="city">北京</p> <i class="fa fa-chevron-down"></i>
      <i class="fa fa-search search-icon"></i>
      <input class="search" type="text" placeholder="搜索" focu>
      <i class="fa fa-plus plus-icon"></i>
    </div>
  </div>
</template>

<script>
  export default {
  }
</script>

<style>
  .homeHead {
    width: 750px;
    height: 80px;
    margin-top: 10px;
    /*background-color: yellow;*/
  }
  .homeContainer {
    width: 100%;
    height: 100%;
    line-height: 70px;
  }
  .weather-icon {
    margin-left: 20px;
  }
  .city {
    display: inline;
    margin-left: 10px;
    font-size: 30px;
  }
  .search-icon {
    position: relative;
    left: 54px;
  }
  .search {
    margin-left: 0;
    background-color: #dddddd;
    border: none;
    border-radius: 27px;
    height: 54px;
    padding-left: 54px;
    width: 380px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }
  .plus-icon {
    position: relative;
    font-size: 40px;
    left: 20px;
    top: 4px;
  }
</style>
