<template>
  <div class="homeHead">
    <div class="homeContainer">
      <i class="fa fa-sun-o weather-icon"></i>
      <p class="city" @click="selectCity">{{locatingCity}}</p> <i class="fa fa-chevron-down" @click="selectCity"></i>
      <i class="fa fa-search search-icon"></i>
      <input class="search" type="text" placeholder="搜索">
      <i class="fa fa-plus plus-icon"></i>
    </div>
  </div>
</template>

<script>
  const $ =require('jquery')

  export default {
    data() {
      return {
        locatingCity: '',
      }
    },
    methods: {
      selectCity() {
        this.$router.push('/locationCities');
      }
    },
    created() {
      let _this = this;
      $.getScript('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js',
        function() {
          if (remote_ip_info.ret === 1) {
            let cityName = remote_ip_info.province;
            _this.locatingCity = cityName;
          }
        }
      );
    }
  }
</script>

<style scoped>
  .homeHead {
    width: 750px;
    height: 80px;
    padding-top: 10px;
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
    background-color: #eeeeee;
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
